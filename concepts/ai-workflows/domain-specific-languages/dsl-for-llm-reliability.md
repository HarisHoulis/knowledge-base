---
domain: ai-workflows
subdomain: domain-specific-languages
concept: dsl-for-llm-reliability
title: DSLs Enable Reliable Use of LLMs
sources:
  - title: "DSLs Enable Reliable Use of LLMs"
    url: "https://martinfowler.com/articles/llm-and-dsls.html"
    author: "Martin Fowler"
---

# DSLs Enable Reliable Use of LLMs

LLMs can generate code with remarkable speed, but without clear boundaries, they are prone to producing unintended results. According to the article 'DSLs Enable Reliable Use of LLMs' [1], abstractions and Domain-Specific Languages (DSLs) offer a strong harness that guides LLMs from the outset, ensuring that generated output aligns precisely with the intended behavior.

Unmesh Joshi's example of Tickloom, a domain model and DSL for illustrating distributed system behavior, demonstrates how an LLM can be used as a partner to iteratively build a DSL and serve as a natural language interface for interacting with it. This approach transforms the DSL into the key source of truth for software systems in the context of LLM-driven development, providing both structure and clarity for code generation.

- LLMs need clear boundaries to generate exactly what is intended, and DSLs provide that harness.
- Abstractions and DSLs guide LLMs right from the start, increasing reliability of generated code.
- Tickloom illustrates using an LLM to iteratively build a DSL for distributed system behavior.
- A DSL can act as the key source of truth for software systems when working with LLMs.
- The LLM can serve as a natural language interface to the DSL, improving accessibility.