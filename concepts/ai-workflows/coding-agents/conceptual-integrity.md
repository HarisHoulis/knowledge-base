---
domain: ai-workflows
subdomain: coding-agents
concept: conceptual-integrity
title: Conceptual integrity and counting lines of code
sources:
  - title: "Conceptual integrity and counting lines of code"
    url: "https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/"
    author: "Simon Willison"
    date: "2026-08-19"
---

# Conceptual integrity and counting lines of code

Simon Willison argues that lines of code can be a meaningful productivity metric when using AI coding agents, contrary to common wisdom. He notes that humans have a hard limit of perhaps 50-200 lines of production-ready code per day, while agents can enable thousands of lines, provided the code matches human quality—maintainable, tested, and debugged. Achieving this requires substantial skill and experience, which is what makes senior engineers valuable. However, the new limiting factor becomes cognitive capacity: an engineer can generate far more code than they can effectively oversee, so teams remain essential to distribute that cognitive load across multiple people (35:01).

Willison then discusses the concept of conceptual integrity from *The Mythical Man-Month* (46:03). Well-designed software has an integrity where everything fits together without surprises. With coding agents, it's easy to add a feature in minutes, leading to software that grows 'little weird bumps' and loses coherence. Claire Giordano compares this to the Winchester Mystery House, where a widow kept adding rooms for 40 years based on a psychic's advice—resulting in a sprawling, incoherent structure. The cheapness of adding 'rooms' via AI undermines conceptual integrity and makes decisions harder. The discipline that was previously enforced by time cost (e.g., 'this would take a week, so I won't do it') is gone, so developers must deliberately impose their own discipline.

- Lines of code can be a useful productivity indicator for AI agents, since human output is bounded (~50-200 lines/day) and agents can multiply that significantly.
- The bottleneck shifts from code generation to cognitive capacity, so teams are still needed even if a single engineer can produce 100x more code.
- AI agents threaten conceptual integrity—the idea from The Mythical Man-Month that software should have no surprises and fit together coherently.
- The low cost of adding features via AI can lead to a 'Winchester Mystery House' of software, requiring deliberate discipline to maintain integrity.