---
domain: ai-workflows
subdomain: coding-agents
concept: conceptual-integrity
title: Conceptual integrity and counting lines of code
sources:
  - title: "Conceptual integrity and counting lines of code"
    url: "https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/"
    author: "Simon Willison"
    date: "2026-08-19T22:46:07+00:00"
---

# Conceptual integrity and counting lines of code

In a post on his blog, Simon Willison argues that counting lines of code can be a meaningful productivity metric when using AI coding agents, contrary to common belief. He explains that unaided engineers can only produce 'a few hundred lines of production-ready code per day'—200 lines is a very good day—and agents can increase that to a thousand lines of debugged code, provided quality is maintained. However, doing so requires 'a huge amount of skill and knowledge and experience' (https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/).

Willison also highlights the new limiting factor: cognitive capacity. Even if an engineer can churn out code a hundred times faster, they cannot stay on top of 100 times the amount of code, so teams remain necessary to load-balance cognitive load. He then discusses the concept of 'conceptual integrity' from The Mythical Man-Month, which is hard to maintain with coding agents because new features can be added cheaply and quickly, leading to a software 'Winchester Mystery House' with many disconnected rooms. Discipline becomes the counterweight, as the cost of adding a feature used to enforce restraint but now does not.

- Lines of code can be a useful productivity metric for AI coding agents, since human output has a hard limit.
- Agents can dramatically increase output, but only with experienced engineers maintaining quality.
- Cognitive capacity, not code production, is the new bottleneck, so teams are still needed.
- Conceptual integrity suffers when features are added too cheaply, creating a 'Winchester Mystery House' codebase.
- Discipline and engineering judgment are more important than ever.