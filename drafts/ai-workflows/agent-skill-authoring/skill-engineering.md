---
domain: ai-workflows
subdomain: agent-skill-authoring
concept: skill-engineering
title: The Dark Arts of Skill Engineering
sources:
  - title: "The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)"
    url: "https://www.youtube.com/watch?v=SQMCtZX3trg"
    author: "AI Engineer"
    date: "2026-09-21"
---

# The Dark Arts of Skill Engineering

Paul Bakaus (author of the open-source "Impeccable" design skill) describes how he moved from a naive system prompt plus a long prose prompt to a more engineered approach for making coding agents produce good design. He built Impeccable while working on a large enterprise app with many views and states, where agents (Claude Code, Codex) could quickly produce something viewable but normalizing it back to his design system was difficult. His first skill, "normalize," brought agent-generated output back to the design system; from there it expanded into a set of design skills, eventually open sourced at impeccable.style [1].

- Naive prompt-level instructions (like the ~55-line front-end design skill with only prose and no scripts) sometimes worked and mostly didn't; adding scripts and structure was the escalation that followed
- Ban lists backfire: telling the model not to use a font just relocates it to the next-best option in its latent space, so it isn't actually more creative
- AI slop is a moving target — the aesthetic marker shifted from purple gradients (traceable to Tailwind's default purple theme) to what Bakaus calls "claw beige"
- A practical first skill was "normalize," which converts whatever the agent designed back into the existing design system