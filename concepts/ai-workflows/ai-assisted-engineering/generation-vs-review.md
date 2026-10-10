---
domain: ai-workflows
subdomain: ai-assisted-engineering
concept: generation-vs-review
title: Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop
sources:
  - title: "Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop — Gabriel Martinez, G2i"
    url: "https://www.youtube.com/watch?v=6qkzlT962es"
    author: "AI Engineer"
    date: "2026-10-09"
---

# Generation Is Cheap, Review Is Expensive: How to Stop Shipping AI Slop

Gabriel Martinez argues that AI-generated code is not itself the problem; the problem is "hackwork" — work that appears complete before the thinking is complete, where uncertainty is resolved by guesswork and responsibility is not taken. The real danger is not that the machine makes a bad choice, but that the engineer never notices a choice was made at all, so unknown unknowns remain unknown. Software is a record of technical, product, operational, and user choices; if those choices are invisible, they cannot be managed, and the team is reduced to pressing the merge button.

Martinez does not claim AI is bad. Agents can write code, create wireframes, and build functions or systems, but they cannot replace human judgment: deciding what matters, interpreting ambiguity, owning the system long-term, exercising architectural restraint, and knowing what not to build. Hackwork is a lack of judgment, not the use of AI as a tool. The cost of writing code is falling, but the cost of understanding software is not, so the bill for added complexity — confusion, fragile processes, untouchable functions, maze-like interfaces — is ultimately paid by the team.

He notes that large systems have always contained more detail than one person can hold, but the main flows, boundaries, data model, and product behavior still need to be understood. AI works well in codebases with structure, patterns, and clear boundaries, but in a "big pile of mud" it only makes the pile bigger and faster. Drawing on Dijkstra, he suggests counting lines of code as lines spent rather than lines created, and insists teams be held accountable for the work they ship, with review and responsibility forcing greater attention to detail.

- Hackwork is work that appears complete before the thinking is complete — uncertainty resolved by guesswork and responsibility not taken, not simply AI-generated code.
- The core danger is that engineers never notice a choice was made, so unknown unknowns remain unknown and the codebase becomes unmanageable.
- AI can generate code but cannot supply judgment: deciding what matters, interpreting ambiguity, owning the system, and knowing what not to build.
- The cost of writing code is falling, but the cost of understanding software is not; added complexity is a bill the team eventually pays.
- Agents amplify existing structure — they help clean codebases but make a "big pile of mud" bigger and faster, so accountability and review are essential.