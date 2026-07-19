---
domain: ai-workflows
subdomain: llm-dsl-integration
concept: dsl-llm-harness
title: DSLs Enable Reliable Use of LLMs
sources:
  - title: "DSLs Enable Reliable Use of LLMs"
    url: "https://martinfowler.com/articles/llm-and-dsls.html"
    author: "Martin Fowler"
---

# DSLs Enable Reliable Use of LLMs

LLMs generate code rapidly but require clear boundaries to produce intended output reliably. Domain-Specific Languages (DSLs) provide a constrained syntax that reduces ambiguity, guiding LLMs from the start. Unmesh Joshi's Tickloom example demonstrates iteratively building a DSL with LLM assistance and using it via natural language. Such a DSL acts as a single source of truth for system behavior, enabling reliable code generation.

- LLMs produce unpredictable code without clear boundaries; DSLs offer a structured vocabulary that minimizes ambiguity.
- The Tickloom example shows how to co-create a DSL with an LLM, using the LLM both as a developer aid and a natural language interface.
- A well-designed DSL can become the authoritative representation of system behavior, ensuring consistency across LLM-generated outputs.