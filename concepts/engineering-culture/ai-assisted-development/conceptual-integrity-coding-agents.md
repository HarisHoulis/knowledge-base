---
domain: engineering-culture
subdomain: ai-assisted-development
concept: conceptual-integrity-coding-agents
title: Conceptual integrity and counting lines of code with AI coding agents
sources:
  - title: "Conceptual integrity and counting lines of code"
    url: "https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/"
    author: "Simon Willison"
    date: "2026-08-19T22:46:07+00:00"
---

# Conceptual integrity and counting lines of code with AI coding agents

In his post, Simon Willison argues that lines of code can still be a meaningful productivity metric when using AI coding agents, because there is a hard limit to how much production-ready code a human can write in a day—historically a few hundred lines at most. If agents enable an engineer to produce a thousand lines of debugged, maintainable code, that is a real improvement, but it requires significant skill and experience to reach that quality. Willison also notes that while a single engineer can now generate code much faster, cognitive capacity becomes the new bottleneck, so teams remain necessary to distribute the mental load and avoid the bus factor (Willison, 2026).

Willison then applies the concept of conceptual integrity from *The Mythical Man-Month* to the age of coding agents. He warns that because agents make adding features so cheap and fast, software projects can easily accumulate what he calls 'little weird bumps'—inconsistent, surprising additions that erode the overall coherence of the system. He uses Claire Giordano's analogy of the Winchester Mystery House, a building continuously expanded for decades, to illustrate how easily software can become a sprawling, incoherent structure when the cost of each new 'room' is low. Willison concludes that discipline is more important than ever; previously, time constraints enforced restraint, but with agents, engineers must consciously decide not to add features to preserve conceptual integrity (Willison, 2026).

- Lines of code can be a useful productivity metric with coding agents because there is a hard human output limit; a thousand lines of quality code per day is a meaningful improvement.
- Agents increase code output but not cognitive capacity, so teams are still needed to distribute the cognitive load and avoid the bus factor.
- Cheap and fast feature addition can destroy conceptual integrity, leading to software that resembles the Winchester Mystery House—a structure with no coherent design.
- Discipline becomes the key factor in maintaining software integrity; with agents, engineers must actively resist adding unnecessary features.