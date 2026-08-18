---
domain: ai-workflows
subdomain: ai-game-development
concept: intent-tagged-assets
title: The Next Game Engine Won't Have a Manual
sources:
  - title: "The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu"
    url: "https://www.youtube.com/watch?v=VBCDhRrvlYo"
    author: "AI Engineer"
    date: "2026-08-18T15:00:29+00:00"
---

# The Next Game Engine Won't Have a Manual

Arturo Nunez argues that AI coding agents fail in game development because the context they are given sits on the game engine's vocabulary rather than the game's intent. For example, controlling a character in a conventional engine requires a mesh, renderer, animator, rigid body, collider, audio source, and only then actual movement logic—boilerplate repeated across every character [1]. This causes agents to reinvent cameras from scratch each time, slightly differently, because they lack a shared understanding of the game's goals.

Nereu, the engine Nunez presents, inverts this by making everything an asset and attaching tags that describe intent rather than implementation. Tags like 'character', 'animated', and 'double jump' are attached to assets, and systems query by tag to move everything marked 'vehicle' and 'drivable'. This is Entity Component System thinking lifted from data-oriented design. A pleasant consequence is that nothing stops a user from tagging a building as drivable and dropping it into a Mario Kart-style race [1].

The engineering detail worth stealing is how context is assembled for the AI. Rather than feeding the whole scene to the model, Nereu borrows level of detail from rendering: assets near whatever is being edited arrive with full tag values, distant ones collapse to a position and type, and trivial elements like a hundred pieces of grass are simply left out [1]. This keeps the prompt small while preserving the most relevant context.

The assistant's role is to get the user unstuck rather than one-shot a finished game, and the vocabulary it expects is the one tutorials already use—press A to jump, press A again in the air [1]. This aligns the AI's mental model with the game designer's intent, making collaboration more natural.

- Conventional game engines flood AI agents with boilerplate (mesh, collider, animator) instead of game intent, causing repeated improvisation.
- Nereu treats everything as an asset with intent tags (character, drivable, double jump) and systems query by those tags.
- Tag-based design enables emergent recombinations, like making a building drivable in a Mario Kart-style race.
- Context assembly applies level-of-detail from rendering: nearby assets carry full tags, distant ones are reduced to position and type, and trivial objects are omitted.
- The AI assistant should help users get unstuck, using tutorial-style language like 'press A to jump in the air again'.