---
domain: ai-workflows
subdomain: agent-production
concept: tribal-dungeons
title: Tribal Dungeons of Global Shipping: AI Agents at Global Scale
sources:
  - title: "Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk"
    url: "https://www.youtube.com/watch?v=dQ-_i1tZiws"
    author: "AI Engineer"
    date: "2026-08-29"
---

# Tribal Dungeons of Global Shipping: AI Agents at Global Scale

Maersk's standard operating procedures were screenshots—sequences of images showing what a person sees and where they click. While perfectly good records for humans, these are useless to AI agents. Dmitry Buykin calls this gap 'tribal dungeons': the knowledge exists, but not in a form anything can execute safely. An agent version of the same procedure needs preconditions, decisions, identifiers, backend calls, validation, recovery, and evidence that it actually worked. Most of the project was this translation, negotiated with process owners, because experts own the 'what' and agents own the 'how' (AI Engineer, 2026).

The sharpest point is where the engineering actually lives. The agent loop is not the system; the refining loop around it is. The corpus of procedures outweighs the runtime roughly twenty to one, because the same shipping step means different things in different countries. Accuracy was not designed up front in a diagram—it was earned through more than 100,000 corrections over nine months, with heat maps turning traces into priorities and a single cell often costing the team a month or two. A correction only counts once it becomes an executable change, which is the line between an opinion and a production fix. Discovery needs agent freedom, production needs a cage, and a harness exists to make dumb mistakes impossible rather than to give the model more room (AI Engineer, 2026).

- SOPs as screenshots are 'tribal dungeons'—knowledge trapped in forms agents cannot execute; they must be translated into executable logic with validation and recovery.
- The refining loop is the real system, not the agent loop; the procedural corpus outweighs runtime code by ~20:1.
- Accuracy is earned through thousands of corrections (100k+ over nine months), not designed upfront; heat maps help prioritize fixes.
- A correction is real only when it becomes an executable change, separating opinions from production fixes.
- Balancing discovery freedom with production safety is essential; harnesses are built to prevent dumb mistakes, not to expand agent autonomy.