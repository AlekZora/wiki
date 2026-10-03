---
title: A Playful Production Process for Game Designers
type: book
status: processed
source_path: raw/books/A Playful Production Process For Game Designers - Richard Lemarchand.pdf
created: 2026-05-11
tags:
  - game-design
  - project-management
  - creative-process
  - production-methodology
concepts:
  - concentric-development
  - vertical-slice
  - experience-goals
  - whole-game-learning
  - elegance-game-design
  - game-design-roles
  - flow-state
  - paranoid-contained-narrative
---

# Summary

Richard Lemarchand's *A Playful Production Process* provides a comprehensive methodology for designing and producing video games and other complex interactive projects. The book's primary purpose is to offer a structured, sustainable, and creativity-fostering alternative to the chaotic and often harmful practices (like "crunch") prevalent in the game industry. Lemarchand argues that by integrating design and production into a unified, iterative process, teams can effectively manage the inherent uncertainty of creating novel experiences, resulting in higher-quality work and healthier developers.

The book's structure follows a four-phase chronological model for game development. Phase One, "Ideation," focuses on generating and exploring core concepts through activities like blue-sky thinking, research, and rapid, low-fidelity prototyping. The goal is not to build a demo, but to discover compelling player activities and establish high-level "Project Goals," particularly "Experience Goals" that define the desired emotional journey for the player.

Phase Two, "Preproduction," is identified as the most critical part of the entire process. Here, the team engages in "designing by doing," creating a high-quality, playable "Vertical Slice" that proves out the core gameplay loop, aesthetics, and technology. This phase introduces key mechanisms like "Concentric Development"—building and polishing the most fundamental mechanics first before layering on more complex systems. The other key deliverables are the "Game Design Macro," a lightweight spreadsheet that maps out the entire game's scope and flow without excessive detail, and a production schedule based on the learnings from building the slice.

Phase Three, "Full Production," is the process of building the full game based on the preproduction plan. This phase is driven by milestones (Alpha and Beta) and guided by the macro schedule. Lemarchand details practical techniques for formal playtesting, using game metrics, and managing the build-out process in a structured way that still allows for micro-level creative discoveries.

Finally, Phase Four, "Postproduction," covers the period after the game is content-complete (Beta). This phase is dedicated to bug fixing, polishing, and balancing, culminating in a "Release Candidate" and then the final "Gold Master" build. Throughout all phases, Lemarchand emphasizes the importance of "soft skills" like communication, collaboration, respect, trust, and consent as foundational to a successful and healthy creative environment.

# Key Claims

- A structured, four-phase production process (Ideation, Preproduction, Full Production, Postproduction) can harness creative chaos to produce excellent games sustainably.
- Preproduction is the most critical phase of development; skipping or rushing it is the root cause of most project failures and crunch.
- The "Vertical Slice"—a polished, playable demo of the core game loop—is the central activity of preproduction, serving to design-by-doing, prove the core concept, and inform scoping.
- "Concentric Development," which involves fully implementing and polishing core (primary) mechanics before moving to secondary ones, creates a stable foundation and manages complexity.
- A "Game Design Macro," a high-level spreadsheet plan, is a vastly superior tool for scoping and project planning compared to traditional, monolithic game design documents.
- Crunch is an unsustainable and counter-productive symptom of a flawed process, not a requirement for excellence, and can be avoided through proper planning and scoping.
- "Soft skills" like communication, collaboration, respect, and consent are as fundamental to successful game development as technical or design expertise.
- Constant, iterative playtesting is the most effective way to discover what makes a game compelling and to refine the player experience.
- Establishing clear "Project Goals," especially "Experience Goals" focused on player emotion, provides an essential creative compass for the entire project.
- Every member of a development team is a game designer, as their moment-to-moment decisions collectively shape the final player experience.

# Mechanisms

- **The Four-Phase Process:** A chronological framework (Ideation -> Preproduction -> Full Production -> Postproduction) with specific deliverables at each milestone (Prototypes -> Vertical Slice/Macro/Schedule -> Alpha/Beta Builds -> Release Candidate). This structures the project from maximum ambiguity to final completion.
- **Concentric Development:** A hierarchical implementation strategy. First, fully build and polish primary mechanics (e.g., core movement). Then, build secondary mechanics (e.g., combat) on that stable foundation. Finally, add tertiary mechanics (e.g., environmental interactions). This prevents building complex systems on an unstable, unproven base.
- **Iterative Design Loop:** A core feedback cycle of `Design -> Implement -> Playtest -> Analyze -> Revise`. This is the engine for discovering and refining gameplay through a playcentric approach, emphasizing frequent, early, and diverse forms of testing.
- **The Game Design Macro Chart:** A spreadsheet that maps the game's chronological flow (rows) against key design dimensions (columns like Location, Player Goal, Design Goal, Emotional Beat, Mechanics). It forces high-level planning of scope, pacing, and variety without getting bogged down in micro-details that will inevitably change.
- **Vertical Slice Construction:** The process of creating a high-quality, shippable-quality demo of a core section of the game. This integrates final-quality art, sound, and mechanics for a small portion of the game to prove the target experience is achievable and to learn about production costs.
- **Structured Feedback Techniques:** Specific communication methods like "Sandwiching" (compliment, critique, compliment) and "I Like, I Wish, What If..." are proposed to structure feedback sessions, fostering a culture of respect and constructive criticism.
- **Burndown Chart Scheduling:** A project management tool used in full production that tracks remaining work-hours against time. It provides a visual forecast of project velocity, enabling early, objective decisions about cutting scope to avoid crunch.

# Useful Examples

- **Uncharted Series:** Used extensively as a case study for the book's methods. Specific examples include the "What is Uncharted?" document as a model for Experience Goals, the use of index cards to create the *Uncharted 2* Game Design Macro, the opening train-wreck sequence in *Uncharted 2* as an integrated tutorial, and the "bad jumps" metrics system from *Uncharted 3* which visualized where players were failing to traverse, providing objective data for level design refinement.
- **Mark Cerny's "Method":** The development process used for *Crash Bandicoot* and *Jak and Daxter*, which forms the philosophical basis for Lemarchand's preproduction phase, particularly the focus on a "publishable first playable" (Vertical Slice) and the Game Design Macro.
- ***Cloud* (USC Game Innovation Lab):** An example of a project that began with a clear, non-traditional Experience Goal ("to evoke the feeling of relaxation and joy that you get when you ... look up at the clouds").
- ***Super Mario Bros.* World 1-1:** Analyzed as a masterclass in onboarding, teaching the player core mechanics (jumping, hitting blocks, stomping enemies) through environmental design without an explicit tutorial.
- **Pixar's Braintrust:** Cited as a model for a healthy, non-hierarchical peer review process where feedback is candid but constructive, and the work (not the person) is the subject of critique.
- **The "Door Problem" (Liz England):** Referenced to illustrate the hidden complexity and cascade of design decisions required for even seemingly simple game elements.

# Possible Relevance

- **AI Agent Design:** The book's production process, especially concentric development and stubbing, is directly applicable to building complex AI agents. An agent's "primary mechanics" (e.g., perception, basic locomotion) must be solidified before adding "secondary" (pathfinding, object interaction) or "tertiary" (complex social behaviors) capabilities. The distinction between "Player Goal" and "Design Goal" in the Macro Chart provides a framework for modeling an agent's internal goals versus the system designer's objectives for the agent's behavior.
- **Narrative Systems:** The Game Design Macro chart is a powerful tool for structuring and scoping serialized or complex interactive narratives. The columns for `Player Goal`, `Design Goal`, and `Emotional Beat` offer a concrete framework for mapping a player's journey, the system's dramatic interventions, and the desired emotional arc on a beat-by-beat basis. This is highly relevant for designing and managing a "serialized narrative experiment."
- **Game Mechanics:** The entire book provides a practical guide to implementing and refining game mechanics. The "concentric development" model offers a core strategy, prioritizing the polish of fundamental mechanics before building outward. The concept of prototyping "toys, not games" is a useful heuristic for focusing on the intrinsic quality of an interaction mechanic before layering on extrinsic goals and rules.
- **Knowledge Management:** The methodology's preference for lightweight, practical documentation (the Game Design Macro) over monolithic "design bibles" is a valuable lesson for personal knowledge management. It advocates for creating just enough structure to guide complex, long-term work without creating a burdensome documentation overhead. The macro itself is analogous to a Map of Content (MOC) for a knowledge domain.
- **Industrial/Ruhr region context:** Lemarchand explicitly frames his creative process as a post-industrial model, contrasting it with the industrial assembly line (Henry Ford, waterfall model) which was perfected in regions like the Ruhr. He argues that creating novel, interactive systems is fundamentally different from mass-producing known objects, requiring an iterative, feedback-driven process of discovery rather than rigid, top-down execution. This provides a direct point of comparison between modes of production.

# Links

- **People:** Amy Hennig, Richard Lemarchand, Charles Baxter, Mark Cerny, Tracy Fullerton, Tom Wujec, Chaim Gingold, Richard Bartle, Walt Disney, Anna Anthropy, Ian Bogost, Steve Swink, Randy Thom, Austin Wintory, Ira Glass, Walter Murch, Brian Allgeier, Clinton Keith, Grant Shonkwiler, Ed Catmull, Amy Wallace, Mary Scannell, Evan Wells, Blaise Pascal, Matthew Frederick, Jason Rubin, Andy Gavin, Michael "MJ" John, Jaime Griesemer, Donald A. Norman, James J. Gibson, Tanya X. Short, Alissa McAloon, Marc Tattersall, Dennis Ramirez, Alice Rawsthorn, Herbert A. Simon, Michael Sellers, Buckminster Fuller, Andrew Stanton, Aristotle, Gustav Freytag, Ellen Lupton, Paul Joseph Gulino, Ursula K. Le Guin, Joseph Campbell, Christopher Vogler, Blake Snyder, J.R.R. Tolkien, Mihaly Csikszentmihalyi, Matthew Luhn, Jesse Schell, Rami Ismail, Emily Morganti, Jim Huntley, Ashley Davis, Adam Single, Ken Schwaber, Jeremy Gibson Bond, Jesse Vigil, Brenda Romero, Ian Schreiber, Ava Duvernay, Robin Hunicke.
- **Books:** *Game Design Workshop*, *A Book of Surrealist Games*, *Rise of the Videogame Zinesters*, *Play Anything*, *Game Feel*, *Creative Agility Tools*, *Creativity, Inc.*, *The Design of Everyday Things*, *Advanced Game Design*, *Thinking in Systems*, *An Architectural Approach to Level Design*, *101 Things I Learned in Architecture School*, *A Practical Guide to Indie Game Marketing*, *Video Game Marketing*, *A Game Design Vocabulary*, *The Art of Game Design*, *Poetics*, *Design Is Storytelling*, *The Hero with a Thousand Faces*, *Agile Game Development*, *The Game Production Toolbox*, *Challenges for Game Designers*, *Introduction to Game Design, Prototyping, and Development*.
- **Concepts/Sources:** Playful Production Process, Four Phases (Ideation, Preproduction, Full Production, Postproduction), Vertical Slice, Game Design Macro, Concentric Development, Project Goals (Experience Goals, Design Goals), Agile Development, Waterfall Model, Mark Cerny's "Method," Crunch, Playcentric Design, "The Gap" (Ira Glass), Sandwiching (feedback), "I Like, I Wish, What If...", MDA Framework, Plutchik's Wheel of Emotions, The Three Cs (Character, Camera, Control), Core Loop, "30 seconds of fun," Blockmesh/Whitebox, Burndown Chart, Scrum, Stand-up Meetings, Alpha Milestone, Beta Milestone, Release Candidate, Gold Master, QA (Quality Assurance), Game Metrics/Analytics, Stubbing, "The Door Problem" (Liz England), The Pixar Braintrust, Post-mortem, Certification Process (TRC, TCR).
- **Games:** *Uncharted* series, *Gex*, *Soul Reaver*, *Jak* series, *Cloud*, *Flow*, *Flower*, *Journey*, *The Last of Us*, *Crash Bandicoot*, *Killer Queen*, *Problem Attic*, *Spore*, *Minecraft*, *Apex Legends*, *The Legend of Zelda* series.