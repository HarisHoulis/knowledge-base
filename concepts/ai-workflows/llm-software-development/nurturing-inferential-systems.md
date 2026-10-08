---
domain: ai-workflows
subdomain: llm-software-development
concept: nurturing-inferential-systems
title: Fragments: Nurturing Inferential Systems and the Future of Code
sources:
  - title: "Fragments: October 4"
    url: "https://martinfowler.com/fragments/2026-10-04.html"
    author: "Martin Fowler"
---

# Fragments: Nurturing Inferential Systems and the Future of Code

Martin Fowler reflects on the shift from building deterministic computational systems to nurturing inferential LLMs, drawing on the 1956 film Forbidden Planet to illustrate the risks of creating thinking machines with unintended behavior. Unlike bugs in deterministic software, which can usually be fixed or disabled, inferential LLMs lack simple fixes or disablement, echoing the fate of the Krell [Fowler, 2026-10-04].

A recurring theme is the changing role of code. Geoffrey Huntley argues code need not be human-readable, while Fowler notes this resembles projectional editing—the editable representation need not match the storage representation. Sam Ruby counters that higher-level representations like Rails remain valuable as compact specifications even when agents write code, asking what sits at the top of the drill and what we trust as source of truth. Unmesh Joshi's argument that code serves both as machine instructions and as a conceptual model of the problem domain is cited: as code generation becomes cheaper, making the conceptual model explicit and refining vocabulary becomes more important [Fowler, 2026-10-04].

Fowler also shares news of Ola Bini's deportation from Ecuador under obscure accusations, and a DDD Europe interview with Eric Evans where they discuss how AI may reinvigorate programming while causing frustration. Sam Ruby's parable of the blind men and the elephant frames the practical question: for the task in front of you this week, where will the information come from, and what will check the result? Finally, Fowler notes Gemini 4 Argon's low hallucination rate (15%) and its willingness to say when it doesn't know, a trade-off he prefers [Fowler, 2026-10-04].

- Building deterministic software differs fundamentally from nurturing inferential LLMs, which lack simple fixes or disablement for unintended behavior.
- Code serves dual purposes—machine instructions and conceptual model—and the latter becomes more important as LLM code generation cheapens the mechanical act of writing.
- Higher-level representations like Rails remain valuable as compact specifications even when agents write code, addressing token size and context window constraints.
- A practical framing for agents: for the task at hand, where will the information come from, and what will check the result?
- A model that admits uncertainty at the cost of fewer correct answers may be preferable to one that hallucinates.