#!/usr/bin/env python3
"""
ingest.py — Gemini-powered raw → wiki/sources pipeline
Matches the schema and AI lens defined in CLAUDE.md

Usage (run from anywhere):
    python3 ingest.py raw/books/my-book.pdf
    python3 ingest.py raw/books/my-book.md
    python3 ingest.py raw/articles/my-article.md
    python3 ingest.py raw/videos/my-video.md
    python3 ingest.py raw/games/my-game.md
    python3 ingest.py raw/videos/          ← ingest a whole folder

BOOKS are processed chapter by chapter:
  1. The book is split into chapters — from the PDF's table of contents,
     from markdown headings, or into fixed-size chunks as a fallback.
  2. One Gemini call per chapter: its argument, key points, and verbatim quotes.
  3. Every quote is checked word-for-word against the book text. Quotes that
     cannot be found are dropped. Page numbers are assigned by this script,
     never by the model.
  4. One final call writes the book-level Summary, Key Ideas and My Take
     from the chapter notes.
  Chapter results are cached in .ingest-cache/, so if a run fails midway
  (billing, network), re-running resumes without paying for finished chapters.

OTHER TYPES (articles, videos, game articles) use a single call, as before,
with quotes verified afterwards.

Safety:
  - Never overwrites an existing source page — saves <name>-v2.md alongside.
  - Stops if a PDF has no extractable text (scanned) instead of letting the
    model invent a summary.
  - Clear error messages for billing / API-key problems; retries on
    temporary failures.
"""

import sys
import os
import re
import json
import time
import hashlib
import pathlib
import datetime
import unicodedata

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Missing dependency. Run: pip install google-genai")
    sys.exit(1)

try:
    import pymupdf
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False


# ── Config ────────────────────────────────────────────────────────────────────

VAULT_ROOT  = pathlib.Path("/Users/alekozoranov/Library/Mobile Documents/iCloud~md~obsidian/Documents")
SOURCES_DIR = VAULT_ROOT / "wiki" / "sources"
CACHE_DIR   = VAULT_ROOT / ".ingest-cache"

# Check AI Studio for current model names and prices; change here if needed.
MODEL = "gemini-2.5-pro"

MIN_TEXT_CHARS    = 500        # less than this after extraction → treat as scanned / empty
CHUNK_PAGES       = 15         # fallback chunk size when a PDF has no usable table of contents
MAX_CHAPTER_CHARS = 150_000    # longer chapters are split into parts
MIN_CHAPTER_CHARS = 800        # shorter sections are skipped (title pages, blank sections)
MIN_QUOTE_CHARS   = 20         # quotes shorter than this are not trusted as verifiable

SKIP_TITLES = ("contents", "copyright", "index", "acknowledg", "bibliography",
               "references", "about the author", "also by", "dedication")

TAG_LIST = ("ai, ml, llm, agents, memory, emergence, behavior, game-design, narrative, "
            "physics, biology, history, philosophy, psychology, engineering, space, "
            "economics, identity, consciousness, creativity, systems, 2d, design, music, "
            "film, language, mathematics, medicine, fiction, comics, visual-storytelling")

AI_LENS = """The AI Lens — apply to every source regardless of topic:
1. How could AI change, advance, or be applied to this topic?
2. What problems in this domain could AI help solve?
3. What does this source reveal about human cognition, behavior, or systems relevant to building AI?
4. Does this source contain patterns or frameworks that could transfer to AI agent design?
5. Where does this source's domain intersect with current AI research or capabilities?"""


class IngestError(Exception):
    pass


# ── API key ───────────────────────────────────────────────────────────────────

def get_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        zshrc = pathlib.Path.home() / ".zshrc"
        if zshrc.exists():
            for line in zshrc.read_text().splitlines():
                if line.startswith("export GEMINI_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not key:
        print("Error: GEMINI_API_KEY not set in environment or ~/.zshrc")
        sys.exit(1)
    return key


# ── Gemini call with retries and clear errors ─────────────────────────────────

def strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```[a-zA-Z]*\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)
    return text.strip()


def call_gemini(client, prompt: str, json_mode: bool = False, retries: int = 3):
    config = types.GenerateContentConfig(response_mime_type="application/json") if json_mode else None
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            response = client.models.generate_content(model=MODEL, contents=prompt, config=config)
            text = (response.text or "").strip()
            if not text:
                raise IngestError("Gemini returned an empty response")
            text = strip_fences(text)
            return json.loads(text) if json_mode else text
        except json.JSONDecodeError as e:
            last_error = f"response was not valid JSON ({e})"
        except IngestError as e:
            last_error = str(e)
        except Exception as e:
            last_error = str(e)
            low = last_error.lower()
            if any(k in low for k in ("billing", "prepay", "credit", "permission_denied",
                                      "api key not valid", "api_key_invalid")):
                raise IngestError(
                    "Gemini refused the request — this looks like a billing or API-key problem.\n"
                    f"    Error: {last_error[:300]}\n"
                    "    Check AI Studio → Billing: prepay must be set up and the balance above zero."
                )
        if attempt < retries:
            wait = 5 * attempt * attempt
            print(f"      attempt {attempt} failed ({last_error[:120]}) — retrying in {wait}s")
            time.sleep(wait)
    raise IngestError(f"Gemini call failed after {retries} attempts: {last_error[:300]}")


# ── Quote verification ────────────────────────────────────────────────────────

def _loose(s: str) -> str:
    """Letters and digits only, lowercased, single spaces. Survives PDF line breaks,
    curly quotes, dashes and ligatures."""
    s = unicodedata.normalize("NFKC", s).replace("\u00ad", "")
    s = re.sub(r"[^\w\s]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def _loose_joined(s: str) -> str:
    """Same, but first rejoins words hyphenated across a line break ("exam-\\nple")."""
    return _loose(re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s))


def locate_quote(quote: str, pages):
    """pages: list of (page_no or None, text).
    Returns (found, page_no). page_no is None for sources without pages."""
    q = _loose(quote)
    if len(q) < MIN_QUOTE_CHARS:
        return False, None
    for variant in (_loose_joined, _loose):
        parts, starts, pos = [], [], 0
        for _, text in pages:
            t = variant(text)
            starts.append(pos)
            parts.append(t)
            pos += len(t) + 1
        idx = " ".join(parts).find(q)
        if idx >= 0:
            page_no = None
            for (p_no, _), start in zip(pages, starts):
                if start <= idx:
                    page_no = p_no
            return True, page_no
    return False, None


# ── Source loading ────────────────────────────────────────────────────────────

def detect_type(path: pathlib.Path) -> str:
    parts = [p.lower() for p in path.parts]
    if "videos" in parts:   return "video"
    if "books" in parts:    return "book"
    if "articles" in parts: return "article"
    if "games" in parts:    return "game-article"
    if "comics" in parts:   return "book"
    return "article"


def load_pdf(path: pathlib.Path):
    if not HAS_PYMUPDF:
        raise IngestError("pymupdf not installed. Run: pip install pymupdf --break-system-packages")
    doc = pymupdf.open(str(path))
    pages = [(i + 1, page.get_text()) for i, page in enumerate(doc)]
    toc = doc.get_toc()
    meta = {k: v for k, v in (doc.metadata or {}).items() if v and k in ("title", "author", "creationDate")}
    doc.close()
    return pages, toc, meta


def pseudo_pages(text: str, size: int = 3000):
    """Group paragraphs of a text file into ~size-char blocks with no page numbers."""
    blocks, current = [], ""
    for para in re.split(r"\n\s*\n", text):
        if current and len(current) + len(para) > size:
            blocks.append((None, current))
            current = ""
        current += para + "\n\n"
    if current.strip():
        blocks.append((None, current))
    return blocks


def chars(pages) -> int:
    return sum(len(t) for _, t in pages)


# ── Chapter splitting ─────────────────────────────────────────────────────────

def pdf_chapters(pages, toc):
    n = len(pages)
    entries = []
    if toc:
        for level in sorted({lvl for lvl, _, _ in toc}):
            candidate = [(title.strip(), p) for lvl, title, p in toc if lvl == level and 1 <= p <= n]
            if len(candidate) >= 3:
                entries = sorted(candidate, key=lambda e: e[1])
                break

    chapters = []
    if entries:
        first_start = entries[0][1]
        if first_start > 1:
            front = pages[:first_start - 1]
            if chars(front) > 3000:
                chapters.append({"title": "Front matter", "pages": front, "from_toc": False})
        for i, (title, start) in enumerate(entries):
            end = entries[i + 1][1] - 1 if i + 1 < len(entries) else n
            if end >= start:
                chapters.append({"title": title, "pages": pages[start - 1:end], "from_toc": True})
    else:
        for s in range(0, n, CHUNK_PAGES):
            chunk = pages[s:s + CHUNK_PAGES]
            chapters.append({"title": f"Pages {chunk[0][0]}–{chunk[-1][0]}", "pages": chunk, "from_toc": False})
    return chapters


def md_chapters(text: str):
    for marker in (r"^#\s+(.+)$", r"^##\s+(.+)$"):
        heads = list(re.finditer(marker, text, flags=re.M))
        if len(heads) >= 3:
            chapters = []
            if heads[0].start() > 3000:
                chapters.append({"title": "Front matter", "pages": pseudo_pages(text[:heads[0].start()]), "from_toc": False})
            for i, h in enumerate(heads):
                end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
                chapters.append({"title": h.group(1).strip(), "pages": pseudo_pages(text[h.start():end]), "from_toc": True})
            return chapters
    blocks = pseudo_pages(text)
    chapters, group = [], []
    for b in blocks:
        group.append(b)
        if chars(group) >= 40_000:
            chapters.append({"title": f"Part {len(chapters) + 1}", "pages": group, "from_toc": False})
            group = []
    if group:
        chapters.append({"title": f"Part {len(chapters) + 1}", "pages": group, "from_toc": False})
    return chapters


def finalize_chapters(chapters):
    """Drop front/back matter and near-empty sections; split oversized chapters."""
    result = []
    for ch in chapters:
        title_low = ch["title"].lower()
        if ch["from_toc"] and any(title_low.startswith(s) or title_low == s for s in SKIP_TITLES):
            continue
        if chars(ch["pages"]) < MIN_CHAPTER_CHARS:
            continue
        if chars(ch["pages"]) <= MAX_CHAPTER_CHARS:
            result.append(ch)
            continue
        part, part_no = [], 1
        for page in ch["pages"]:
            part.append(page)
            if chars(part) >= MAX_CHAPTER_CHARS:
                result.append({**ch, "title": f"{ch['title']} (part {part_no})", "pages": part})
                part, part_no = [], part_no + 1
        if part:
            result.append({**ch, "title": f"{ch['title']} (part {part_no})", "pages": part})
    return result


def page_label(pages) -> str:
    nums = [p for p, _ in pages if p is not None]
    if not nums:
        return ""
    return f"p. {nums[0]}" if nums[0] == nums[-1] else f"pp. {nums[0]}–{nums[-1]}"


# ── Book prompts ──────────────────────────────────────────────────────────────

CHAPTER_PROMPT = """You are reading one section of a book so it can be summarized faithfully for a personal knowledge base.

Book file: {book}
Section {num} of {total}: {title}

Read the whole section, then return JSON with exactly these keys:

"argument": one paragraph (3-6 sentences) stating what this section actually argues or establishes — its specific claims, not a list of topics it "discusses". If the section has no substantive content (copyright page, contents, index, acknowledgements), return an empty string.

"key_points": 3-8 strings. The specific points a reader must not lose: claims, mechanisms, examples, names, numbers, definitions. Keep concrete details — do not generalize them away.

"quotes": up to 3 strings. Each must be copied EXACTLY, character for character, from the section text below — 10 to 60 words, one continuous passage, no ellipses, no edits, no added quotation marks. Choose passages that capture the section's central idea. If none qualify, return an empty list.

Rules: use only what is in this section. No outside knowledge. No invented facts. Do not evaluate the book here — only record what it says.

Section text:
{text}
"""

BOOK_PROMPT = """You are writing the book-level parts of a source note for a personal knowledge base. Its organizing lens is AI.

{ai_lens}

Below are faithful notes for every section of the book, in order, plus the book's opening pages (to identify title and author) and a numbered list of verified quotes.

Return JSON with exactly these keys:
"title": the book's title
"author": the author's name, or "unknown"
"published": publication year as YYYY if stated in the opening pages or metadata, else "unknown"
"tags": 3-6 tags chosen only from: {tags}
"summary": 2-4 paragraphs, plain language, own words, following the book's arc in order. Every section that makes a distinct argument must be represented — do not skip sections or blur distinct arguments together. No invented facts.
"key_ideas": 6-12 strings — the book's most important ideas, each specific enough to be useful on its own.
"quote_ids": a list of the numbers of the 3-6 verified quotes that best represent the whole book.
"my_take": 1-3 paragraphs of analysis. ALWAYS include at least one specific observation about how AI intersects with the ideas in this book, using the AI lens above.

Use only the section notes and opening pages. Do not add facts about the book from outside knowledge.

Opening pages:
{opening}

File metadata: {meta}

Section notes:
{notes}

Verified quotes:
{quotes}
"""


# ── Output helpers ────────────────────────────────────────────────────────────

def safe_out_path(stem: str) -> pathlib.Path:
    """Never overwrite: returns <stem>.md, or <stem>-v2.md, -v3.md … if taken."""
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    path = SOURCES_DIR / f"{stem}.md"
    version = 2
    while path.exists():
        path = SOURCES_DIR / f"{stem}-v{version}.md"
        version += 1
    return path


def yaml_str(value) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def bullet_list(items) -> str:
    return "\n".join(f"- {str(i).strip()}" for i in items if str(i).strip())


def cite(page_no, chapter_title) -> str:
    return f"(p. {page_no})" if page_no is not None else f"({chapter_title})"


# ── Book ingest ───────────────────────────────────────────────────────────────

def ingest_book(raw_path: pathlib.Path, client, today: str) -> pathlib.Path:
    if raw_path.suffix.lower() == ".pdf":
        pages, toc, meta = load_pdf(raw_path)
        if chars(pages) < MIN_TEXT_CHARS:
            raise IngestError("PDF has no extractable text — probably scanned images. "
                              "Run OCR on it first (or use a text version); stopping so nothing gets invented.")
        chapters = pdf_chapters(pages, toc)
        opening = "\n".join(t for _, t in pages[:4])[:6000]
    else:
        text = raw_path.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) < MIN_TEXT_CHARS:
            raise IngestError("File is empty or nearly empty — stopping.")
        chapters = md_chapters(text)
        meta = {}
        opening = text[:6000]

    chapters = finalize_chapters(chapters)
    if not chapters:
        raise IngestError("No usable chapters found after splitting.")

    print(f"    {len(chapters)} sections to process")

    # Cache so a failed run can resume
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    fingerprint = hashlib.sha1(raw_path.read_bytes()).hexdigest()[:12]
    cache_path = CACHE_DIR / f"{raw_path.stem}-{fingerprint}.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    notes = []
    for i, ch in enumerate(chapters, start=1):
        key = str(i)
        label = page_label(ch["pages"])
        if key in cache:
            print(f"    [{i}/{len(chapters)}] {ch['title'][:60]}  (cached)")
            result = cache[key]
        else:
            print(f"    [{i}/{len(chapters)}] {ch['title'][:60]}  {label}")
            section_text = "\n".join(t for _, t in ch["pages"])
            result = call_gemini(client, CHAPTER_PROMPT.format(
                book=raw_path.name, num=i, total=len(chapters),
                title=ch["title"], text=section_text), json_mode=True)
            cache[key] = result
            cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1))

        argument = str(result.get("argument", "")).strip()
        if not argument:
            continue

        verified, dropped = [], 0
        for q in result.get("quotes", []) or []:
            q = str(q).strip().strip('"“”')
            found, page_no = locate_quote(q, ch["pages"])
            if found:
                verified.append({"text": q, "page": page_no})
            else:
                dropped += 1
        if dropped:
            print(f"        dropped {dropped} quote(s) not found word-for-word in the text")

        notes.append({"title": ch["title"], "label": label, "argument": argument,
                      "key_points": result.get("key_points", []) or [], "quotes": verified})

    if not notes:
        raise IngestError("Every section came back empty — nothing substantive to summarize.")

    # Global numbered quote pool for the book-level call
    pool = []
    for n in notes:
        for q in n["quotes"]:
            pool.append({**q, "chapter": n["title"]})

    notes_text = "\n\n".join(
        f"SECTION {i}: {n['title']} {n['label']}\nArgument: {n['argument']}\nKey points:\n{bullet_list(n['key_points'])}"
        for i, n in enumerate(notes, start=1))
    quotes_text = "\n".join(
        f"{i}. \"{q['text']}\" {cite(q['page'], q['chapter'])}" for i, q in enumerate(pool, start=1)) or "(none)"

    print("    writing book-level summary…")
    book = call_gemini(client, BOOK_PROMPT.format(
        ai_lens=AI_LENS, tags=TAG_LIST, opening=opening, meta=json.dumps(meta, ensure_ascii=False),
        notes=notes_text, quotes=quotes_text), json_mode=True)

    ids = [i for i in book.get("quote_ids", []) if isinstance(i, int) and 1 <= i <= len(pool)]
    if not ids:
        ids = list(range(1, min(len(pool), 5) + 1))
    top_quotes = "\n".join(
        f"> \"{pool[i-1]['text']}\" {cite(pool[i-1]['page'], pool[i-1]['chapter'])}" for i in ids)

    chapter_blocks = []
    for i, n in enumerate(notes, start=1):
        block = f"### {i}. {n['title']}" + (f" ({n['label']})" if n["label"] else "")
        block += f"\n{n['argument']}\n"
        if n["key_points"]:
            block += "\n" + bullet_list(n["key_points"]) + "\n"
        for q in n["quotes"]:
            block += f"\n> \"{q['text']}\" {cite(q['page'], n['title'])}\n"
        chapter_blocks.append(block)

    tags = [t.strip() for t in book.get("tags", []) if str(t).strip()]
    page = f"""---
type: book
title: {yaml_str(book.get('title', raw_path.stem))}
author: {yaml_str(book.get('author', 'unknown'))}
published: {book.get('published', 'unknown')}
ingested: {today}
tags: [{', '.join(tags)}]
concepts: []
---
## Summary
{str(book.get('summary', '')).strip()}
## Key Ideas
{bullet_list(book.get('key_ideas', []))}
## Chapter Notes
{chr(10).join(chapter_blocks).strip()}
## Quotes
{top_quotes}
## My Take
{str(book.get('my_take', '')).strip()}
"""
    out_path = safe_out_path(raw_path.stem)
    out_path.write_text(page, encoding="utf-8")
    print(f"    quotes verified: {len(pool)} kept across all sections")
    return out_path


# ── Single-call ingest (articles, videos, game articles) ─────────────────────

SCHEMAS = {
    "video": """\
---
type: video
title: {title}
url: {url}
channel: {channel}
published: {published}
ingested: {today}
duration: {duration}
tags: {tags}
concepts: []
---
## Summary
{summary}
## Key Ideas
{key_ideas}
## Timestamps
{timestamps}
## My Take
{my_take}""",

    "article": """\
---
type: article
title: {title}
url: {url}
author: {author}
published: {published}
ingested: {today}
tags: {tags}
concepts: []
---
## Summary
{summary}
## Key Points
{key_points}
## Quotes
{quotes}
## My Take
{my_take}""",

    "game-article": """\
---
type: game-article
title: {title}
url: {url}
game: {game}
author: {author}
published: {published}
ingested: {today}
tags: {tags}
concepts: []
---
## Summary
{summary}
## Notable Points
{notable_points}
## What It Attempted
{attempted}
## Where It Succeeded / Where It Failed
{succeeded_failed}
## My Take
{my_take}""",
}

QUOTE_RULE = ("copied EXACTLY, character for character, from the source — one continuous passage, "
              "no ellipses, no edits (use \"> \" prefix)")

INSTRUCTIONS = {
    "video": f"""
Fill every field. For fields you cannot determine from the content, write "unknown".
- title: infer from content
- url: write "unknown" if not present
- channel: infer if possible, else "unknown"
- published: YYYY-MM-DD if mentioned, else "unknown"
- duration: HH:MM if mentioned, else "unknown"
- tags: 3-6 lowercase tags from: {TAG_LIST}
- summary: one paragraph, plain language, own words, no invented facts
- key_ideas: bullet list of main ideas (use "- " prefix)
- timestamps: notable moments with approximate timestamps if available, else key section markers (use "- " prefix)
- my_take: your analytical take including ALWAYS at least one specific observation about how AI intersects with this topic
""",

    "article": f"""
Fill every field. For fields you cannot determine from the content, write "unknown".
- title: infer from content
- url: write "unknown" if not present
- author: infer if possible, else "unknown"
- published: YYYY-MM-DD if mentioned, else "unknown"
- tags: 3-6 lowercase tags from: {TAG_LIST}
- summary: one paragraph, plain language, own words, no invented facts
- key_points: bullet list (use "- " prefix)
- quotes: 1-3 notable direct quotes, each {QUOTE_RULE}, or leave blank
- my_take: analytical take including ALWAYS at least one specific AI intersection observation
""",

    "game-article": f"""
Fill every field. For fields you cannot determine from the content, write "unknown".
- title: infer from content
- url: write "unknown" if not present
- game: name of the game discussed
- author: infer if possible, else "unknown"
- published: YYYY-MM-DD if mentioned, else "unknown"
- tags: 3-6 lowercase tags from: {TAG_LIST}
- summary: one paragraph, plain language, own words, no invented facts
- notable_points: bullet list (use "- " prefix)
- attempted: what design goal or idea the source describes
- succeeded_failed: honest assessment of what worked and what didn't
- my_take: analytical take including ALWAYS at least one specific AI intersection observation
""",
}


def build_prompt(content: str, source_type: str, today: str) -> str:
    return f"""You are ingesting a raw source into a personal knowledge base wiki. Its organizing lens is AI.

Source type: {source_type}
Today's date: {today}

{AI_LENS}

Instructions:
{INSTRUCTIONS[source_type]}

Output ONLY the completed source note in this exact schema — no preamble, no commentary, no markdown fences:

{SCHEMAS[source_type]}

---
Raw source content:

{content}
"""


def verify_quote_lines(note: str, pages):
    """Remove '> ' quote lines that can't be found word-for-word in the source."""
    kept, dropped = [], 0
    for line in note.splitlines():
        if line.startswith(">"):
            q = line.lstrip("> ").strip().strip('"“”')
            if q and not locate_quote(q, pages)[0]:
                dropped += 1
                continue
        kept.append(line)
    return "\n".join(kept), dropped


def ingest_single(raw_path: pathlib.Path, client, source_type: str, today: str) -> pathlib.Path:
    if raw_path.suffix.lower() == ".pdf":
        pages, _, _ = load_pdf(raw_path)
        content = "\n\n".join(f"[Page {p}]\n{t}" for p, t in pages if t.strip())
    else:
        content = raw_path.read_text(encoding="utf-8", errors="replace")
        pages = [(None, content)]

    if len(content.strip()) < MIN_TEXT_CHARS:
        raise IngestError("Source has no usable text (empty or scanned) — stopping so nothing gets invented.")

    note = call_gemini(client, build_prompt(content, source_type, today))
    note, dropped = verify_quote_lines(note, pages)
    if dropped:
        print(f"    dropped {dropped} quote(s) not found word-for-word in the source")

    out_path = safe_out_path(raw_path.stem)
    out_path.write_text(note + "\n", encoding="utf-8")
    return out_path


# ── Entry point ───────────────────────────────────────────────────────────────

def ingest_file(raw_path: pathlib.Path, client):
    source_type = detect_type(raw_path)
    today = datetime.date.today().isoformat()
    print(f"\n  → {raw_path.name}  [{source_type}]")
    try:
        if source_type == "book":
            out = ingest_book(raw_path, client, today)
        else:
            out = ingest_single(raw_path, client, source_type, today)
    except IngestError as e:
        print(f"  ✗ {raw_path.name}: {e}")
        return None
    note = "  (existing file kept — saved as new version)" if "-v" in out.stem[len(raw_path.stem):] else ""
    print(f"  ✓ Saved: wiki/sources/{out.name}{note}")
    return out


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ingest.py raw/books/my-book.pdf")
        print("       python3 ingest.py raw/videos/my-video.md")
        print("       python3 ingest.py raw/videos/")
        sys.exit(1)

    target = pathlib.Path(sys.argv[1])
    if not target.is_absolute():
        target = VAULT_ROOT / target

    if target.is_dir():
        files = sorted(list(target.glob("*.md")) + list(target.glob("*.pdf")))
    elif target.is_file():
        files = [target]
    else:
        print(f"✗ Not found: {target}")
        sys.exit(1)

    if not files:
        print("No .md or .pdf files found.")
        sys.exit(0)

    client = genai.Client(api_key=get_api_key())

    print(f"\nIngesting {len(files)} file(s) with Gemini ({MODEL})...")
    ingested = [r for r in (ingest_file(f, client) for f in files) if r]

    print(f"\nDone — {len(ingested)}/{len(files)} ingested.")
    if ingested:
        print("\nNext step in Claude Code (concept extraction, log, index):")
        for p in ingested:
            print(f"  run concept extraction for wiki/sources/{p.name}")


if __name__ == "__main__":
    main()
