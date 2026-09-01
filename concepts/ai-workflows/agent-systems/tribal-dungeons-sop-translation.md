---
domain: ai-workflows
subdomain: agent-systems
concept: tribal-dungeons-sop-translation
title: Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk
sources:
  - title: "Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk"
    url: "https://www.youtube.com/watch?v=dQ-_i1tZiws"
    author: "AI Engineer"
    date: "2026-08-29T17:30:21+00:00"
---

# Tribal Dungeons of Global Shipping: AI Agents at Global Scale — Dmitry Buykin, Maersk

Maersk's standard operating procedures were screenshots—a sequence of images showing what a person sees and where they click, which is useful to a human but useless to an agent. Dmitry Buykin calls this gap "tribal dungeons": the knowledge exists, just not in a form anything can execute safely. An agent version of the same procedure needs preconditions, decisions, identifiers, backend calls, validation, recovery, and evidence that it actually worked. Most of the project was that translation, negotiated with the people who own the process, because experts own the what and agents own the how (Dmitry Buykin, AI Engineer, 2026).

- SOPs as screenshots are not executable; agents require structured procedures with preconditions, decisions, backend calls, validation, recovery, and evidence.
- The agent loop is not the system—the refining loop around it is, with the procedure corpus outweighing the runtime roughly twenty to one.
- Accuracy was earned through more than 100,000 corrections over nine months, with heat maps turning traces into priorities; a single cell often cost the team a month or two.
- A correction only counts once it becomes an executable change—that is the line between an opinion and a production fix.
- Discovery needs agent freedom, but production needs a cage; a harness exists to make dumb mistakes impossible rather than to give the model more room.