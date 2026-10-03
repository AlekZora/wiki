---
title: "What Makes Games Easy to Learn And Hard to Master"
source: "https://www.gamedeveloper.com/design/what-makes-games-easy-to-learn-and-hard-to-master"
author:
  - "[[Marcin Jóźwik]]"
published: 2023-08-21
created: 2026-05-22
description: "We hear it everywhere. Game descriptions, game pitches, marketing, reviews. I knew it by heart, but never truly thought what it meant from the perspective of game design. Let’s try to figure it out."
tags:
  - "clippings"
---
We hear it everywhere. Game descriptions, game pitches, marketing, reviews. I knew it by heart, but never truly thought what it meant from the perspective of game design. Let’s try to figure it out.

![Game Developer logo in a gray background | Game Developer](https://eu-images.contentstack.com/v3/assets/blt740a130ae3c5d529/bltba62518415cda0e2/652fe6ddbc479f8697ef691f/default-cubic.png?width=1280&auto=webp&quality=80&format=jpg&disable=upscale "Game Developer")

![](https://eu-images.contentstack.com/v3/assets/blt740a130ae3c5d529/blt4448485532d1d1ca/650f00af37493ce9e96ca361/image_1.png/?width=1280&auto=webp&quality=80&disable=upscale)

“Easy to learn, hard to master“

We hear it everywhere. Game descriptions, game pitches, marketing, reviews. An ultimate catch-all phrase for talking about games. I knew it by heart, but never truly thought what it meant from the perspective of game design. Let’s try to figure it out.

Easy To Learn

When exactly is a game easy to learn? I would think of it from four different angles:

- Inherent Simplicity — a matter of what — a game has a small number of rules and things to remember. The game strives to have a ruleset with as few exceptions, caveats as possible.
- Coherency — a matter of which — chosen rules have a logical correlation between each other. Players can draw analogies between rules and one’s prior experience. A game feels familiar.
- Progression — a matter of when — rules are introduced in the right order and time.
- Communication — a matter of how — a game communicates clearly its ruleset. A player can easily recognize what he can do because of a clear interface and understand the consequences of his actions due to proper feedback.

In other words, an easy to learn game has a thoughtful amount of logical rules to remember, rules are introduced progressively throughout the game and can be learned smoothly by providing good interface and feedback.

Then, on the contrary, a hard game to learn would have a lot of not intuitive rules with many exceptions (inherent complexity), players would have a hard time recognizing what they are able to do (interface problems), players would not be able to learn easily from their actions (poor feedback) and all the rules would be introduced at once (no progression).

<video src="https://cdn.spotible.com/creative/VwnV/hashed/6603d8e555fc39182528d6a47137bed9/GDC_NewsDesk_Helpshift_Snippet_v2.mp4" controls=""></video>

ADVERTISING

(…) an easy to learn game has a thoughtful amount of logical rules to remember, rules are introduced progressively throughout the game and can be learned smoothly by providing good interface and feedback.

Hidden Rules

One thing worth noting here is the visibility of the rules. In the world of digital games, we need to remember that there are systems and rules that are visible and need to be understood by the player, and those which are hidden and are used under the hood.

It’s an important distinction, because the hidden rules don’t necessarily affect the inherent simplicity. For example, a game about pushing color blocks could be very simple, but the hidden rules of when to spawn which color block could be really complex. The game does some crazy math, but the player just pushes blocks.

Hard To Master

How to approach mastery, then? For the sake of this article, let’s say that mastery boils down to finding “the right” and preferably one solution to a given problem. The game throws at us a problem, a master player knows the one and only solution to solve it right away.

Then, if something is hard to master, it takes time and many repeats to achieve that. The possibility space is so big that it takes significant effort to find the right solution in that space.

On the other hand, in a game that is easy to master, a universal pattern to beat it, a dominant strategy, would be clear from the start or after only a few attempts.

It’s worth noting that the mastery aspect can relate to either knowledge of the systems (strategy, memory) or proficiency in using the interface (skill).

I would think about mastering from two different perspectives:

- Complexity — the size of possibility space. A complex game has a lot of rules, players have multiple actions they can perform, the game has multiple moving parts that lead to having a plethora of possible game states.
- Uncertainty — players cannot be sure about exact implications of their actions, there are elements that make the learning process harder. That includes randomness (both input and output), opponent moves, dynamic change of a problem to solve and a tempo of game state changes.

Fun to Master

We need to draw a clear line between hard to master and fun to master though. Some games obfuscate the result of actions to the extent when everything seems random and players cannot learn at all. The game is, in fact, hard to master, but also frustrating in the implementation of it.

We need to be aware of how we balance the complexity/uncertainty ratio. We need to make space for the learning process to happen.

![](https://eu-images.contentstack.com/v3/assets/blt740a130ae3c5d529/blt2985fce959995669/650f090c26e3e217c94afb19/image_2.png/?width=1280&auto=webp&quality=80&disable=upscale)

Seeking Elegance

So, we have examined the criteria for making “easy to learn” games and “hard to master” games individually. What can we do to have it all in a single game?

The combination of clarity and mastery sounds like a Holy Grail.

Capture this perfect couple in your game and you would have what is often called an elegant design. Easy to understand rules that create complex deep systems. From a few carefully planted seeds emerge a beautiful and rich ecosystem.

In other words, a thoughtful mix of several systems leads to a gameplay full of interesting, unique decisions and gameplay situations. Simple actions performed by the player result in a plethora of complex game states.

From a few carefully planted seeds emerge a beautiful and rich ecosystem.

Framing Elegance

Elegance is a rather elusive thing. A game can feel elegant but recognizing exact things that make it that way can be challenging.

Nevertheless, here are several aspects that I think many elegant games share:

- Multi-purpose Systems — to avoid complexity, one action is used in many different contexts. It helps to learn faster — once the rule is learned in one context, it can be applied to the rest of contexts without a further do (it also speeds up the development process!).
- Trade-offs — an action by the player has both positive and negative consequences at the same time. Players do something to strengthen their position, but simultaneously, the same action weakens their position elsewhere. Players are left with constantly calculating if a given action is worth the accompanied disadvantage.
- Combo-friendly — rules are constructed in a way that promotes making combinations or sequences. Very often, a combination is worth more than the sum of its parts.
- Modularity — additional rules can be added or removed from the game without hurting the game’s core. Rules alter the possibility space forcing players to adapt and create new strategies.

Adding New Rules

In talking about “easy to learn, hard to master“ we won’t get definitive answers. I cannot imagine a single mechanic that would change one side of the equation without changing the other. Adding a new thing will always affect the way we learn and the way we master. So instead of seeking an impossible solution, we need to think of a ratio:

How to minimize the process of learning and maximize the process of mastering?

The better the ratio, the more our game is “easy to learn, hard to master “.

So, we added a new feature. It’s cool. But think of the ratio. What do I need to do to put it in a game to make it work? Is it simple? Does it work well with existing features? Do I have a place to introduce it? Does it need a lot of feedback? And what do I get in return? Does it enrich the gameplay? Does it give me enough new interesting scenarios and new interesting challenges?

Consider that every time you add something new to the game. Get better at answering those questions and, with time, your games will flourish by being more and more “easy to learn, hard to master “.

Summary

Let’s sum up what we have discovered:

1. An easy to learn game has a thoughtful amount of logical rules to remember, rules are introduced progressively throughout the game and can be learned smoothly by providing good interface and feedback.
2. A hard to master game consists of many actions the player can perform, lots of moving parts that sum up to a huge possibility space. Learning is obfuscated by uncertainty in a form of: randomness, an opponent's behavior, changing plans and tempo. At the same time, the game is fun to master.
3. We strive to minimize the process of learning and maximize the process of mastering at the same time.
4. Elegant design brings a thoughtful mix of several systems that leads to a gameplay full of interesting, unique decisions and gameplay situations.
5. Elegant games tend to include multi-purpose features, lots of trade-offs, combo-friendliness and modularity.
6. Adding a new feature will always affect the way players learn and the way players master. Be sure that the new feature improves the clarity/mastery ratio of the game or you have other good reasons to add it.

Your Turn

Now it’s your turn. Ask yourself these questions, summarizing all we have talked about, to make your game more “Easy to Learn, Hard to Master “.

Have a wonderful day!

![](https://eu-images.contentstack.com/v3/assets/blt740a130ae3c5d529/blt86dd6d06de140495/650f01033d26a149557d7dfd/image_3.png/?width=1280&auto=webp&quality=80&disable=upscale)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Easy to Learn, Hard to Master Template

1. Is my game inherently simple? How many rules do players need to remember? Are there many exceptions to the rules?
2. Is my game coherent? Do rules make logical sense together? Can players draw analogies from the real world to understand them?
3. What does the progression look like? Are the rules introduced in the right order and time?
4. How does my game communicate with players? How does the interface communicate possible actions? How does feedback communicate the result of an action?
5. Is my game complex enough? How big is the possibility space? How long does it take to master the game? How many actions does the player have? What are the moving parts?
6. Does my game include enough uncertainty? Do I make use of randomness, opponents moves, changing plans, tempo?
7. Is my game fun to master? Do I provide a fun environment for the learning process to happen?
8. Does my game use multi-purpose features? Can I combine some systems to do more than just one thing?
9. Are trade-offs present in my game? What are the actions that give advantage and disadvantage at the same time? Can I change some of them to include both good and bad? Can I spot a dominant strategy and find a counter for it?
10. Is my game combo-friendly? What are the actions that create sequences? Is the sequence more than a sum of its parts?
11. Is my game modular? Can I add and remove features without hurting the core? Do secondary features force players to think in new ways?
12. Is my game easy to learn, hard to master? Does the game provide enough complexity out of simplicity?

Read more about:

[Blogs](https://www.gamedeveloper.com/keyword/blogs)