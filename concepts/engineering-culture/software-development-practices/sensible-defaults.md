---
domain: engineering-culture
subdomain: software-development-practices
concept: sensible-defaults
title: Sensible Default
sources:
  - title: "Bliki: Sensible Default"
    url: "https://martinfowler.com/bliki/SensibleDefault.html"
    author: "Martin Fowler"
---

# Sensible Default

A Sensible Default is a practice that should be used for a kind of task absent overriding context, such as “use version control”, “separate UI logic from domain logic”, or “automate deployment pipelines”. The term deliberately contrasts with “best practice”: best practice implies a general presumption that it should always be done, while a sensible default is a known-good starting point that can and should be reassessed and overridden when circumstances change.

Martin Fowler first heard the term popularized within Thoughtworks by Evan Bottcher, who got it from talking to James Ross and found the phrasing captured the nuance of a known-good starting point. Bottcher describes it as what is expected if there are no hard constraints: do these practices, or do better, and be prepared to explain why you chose another way.

Thoughtworks has made much of the concept, including publishing a playbook of defaults. People are expected to be familiar with them, ready to use them on new work, while also knowing their limitations and judging whether circumstances require change. Defaults are reassessed regularly, consistent with the twelfth agile principle, and the Thoughtworks Technology Radar is cited as the heart of that reassessment. Fowler also notes a post from Steve Bennett on sensible defaults written around the time Evan talked to James, though he does not know whether it was the source of the name or appeared in parallel.

- Sensible defaults are practices to apply unless context overrides them, in contrast to “best practice” as a universal expectation.
- They are known-good starting points that should be overridden and explained when circumstances change.
- Thoughtworks maintains a playbook of sensible defaults and expects teams to know both their value and limitations.
- Defaults are regularly reassessed, for example through the Thoughtworks Technology Radar and agile reflection.