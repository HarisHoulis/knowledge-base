---
domain: ai-workflows
subdomain: ai-development-workflow
concept: prototype-over-spec
title: Don't waste time on specs: /prototype instead
sources:
  - title: "Don't waste time on specs: /prototype instead"
    url: "https://www.youtube.com/watch?v=n0VhIVtviC0"
    author: "Matt Pocock"
    date: "2026-07-23T14:00:35+00:00"
---

# Don't waste time on specs: /prototype instead

Matt Pocock argues that many developers waste effort creating detailed specs for AI-assisted coding when they should be prototyping instead. He observes that people default to spec-driven development, trying to specify everything upfront so AI output matches expectations. However, this ignores the agility of writing code during the process. Prototyping and spikes, popular since Agile, are being neglected even though the cost of producing code has dropped dramatically with AI, making throwaway prototypes cheaper and more effective than ever (Pocock, 2026).

Pocock introduces the concept of fidelity to decide when to prototype. Simple questions about basic structure can be resolved through discussion, but questions about how something looks or behaves often need a higher fidelity artifact. Building a quick, rough prototype allows the team to react to something concrete rather than abstract spec text. He advocates using AI to quickly create these prototypes during planning discussions, raising the fidelity of the conversation only where needed (Pocock, 2026).

This idea is built into his Wayfinder planning skill, which includes a dedicated 'prototype' ticket type. The prototype skill is used when the key question is 'how should it look or how should it behave?' He demonstrates this with an example: searching old diagrams in a TLDraw-based app. Instead of writing a spec, he ran the prototype skill, which generated a working picker with three different options to evaluate behavior visually (Pocock, 2026).

- Don't default to spec-driven development with AI; use throwaway prototypes to answer uncertain questions.
- The cost of producing code has fallen sharply, making prototypes and spikes exceptionally cheap.
- Match fidelity to the question: basic scope via discussion, look/behavior via concrete prototypes.
- Integrate prototyping into planning workflows, as with the Wayfinder prototype skill.
- A prototype is throwaway code that answers a specific question, not a stepping stone to production code.