---
domain: ai-workflows
subdomain: coding-agents
concept: grill-with-docs-skill
title: Shipping a 21,000-Line Feature with mattpocock/skills
sources:
  - title: "Watch me ship a 21,000-line feature with mattpocock/skills"
    url: "https://www.youtube.com/watch?v=jVBlkOF8sHk"
    author: "Matt Pocock"
    date: "2026-11-18"
---

# Shipping a 21,000-Line Feature with mattpocock/skills

Matt Pocock walks through his end-to-end AI-assisted development process for a real feature in his video/thumbnail editor: integrating a drawing surface directly onto the thumbnail image so diagrams no longer need a separate screenshot-and-paste step. He frames each new piece of work as a decision about what diff to produce, and picks a skill accordingly—small diffs can be one-shot, while larger ones start with the 'grill with docs' skill (Pocock, 2026).

Grilling is treated as an art form centered on domain modeling: by working out the language of the application (classic DDD-style thinking), he effectively figures out what the app should be. If the work turns out bigger than expected, he can bail out into 'wayfinder' to spread grilling across many sessions; starting with grill-with-docs avoids wayfinder's overhead when the feature is smaller than feared (Pocock, 2026).

After roughly 30 sessions, he runs the 'retro' skill to review the whole chunk of work and suggest improvements, then does real human review on a ~25,000-line PR and shows how that review feeds back into the system going forward (Pocock, 2026). The walkthrough runs inside his personal wiki/home repo and uses Claude as the agent.

- Choose a skill based on the size of the intended diff: one-shot small changes, grill-with-docs for larger features, wayfinder when scope balloons
- Grilling is domain modeling—nailing the app's language is how you figure out what to build
- The retro skill reviews ~30 sessions of work and proposes concrete improvements
- Human review of a huge PR (~25,000 lines) is fed back into the system to improve future sessions