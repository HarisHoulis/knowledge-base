---
domain: ai-workflows
subdomain: llm-assisted-development
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Bliki: Vibe Coding

Vibe coding is a term coined by Andrej Karpathy in February 2025 for building software by prompting an LLM without reading or reviewing the generated code. The practitioner describes what they want, runs the result, and iterates based on errors or changes, effectively treating the LLM as a black box. This approach allows people without programming knowledge to create working applications, but it carries significant risks related to maintainability, correctness, and security. Martin Fowler distinguishes vibe coding from agentic programming, where programmers still care about and review LLM-generated code, emphasizing that vibe coding specifically means "forget that the code even exists."

- Vibe coding involves prompting an LLM to build software without reviewing the generated code.
- The term was coined by Andrej Karpathy in February 2025.
- It enables non-programmers to create applications but leads to poor maintainability and security risks.
- Vibe coding is best suited for disposable software used by a small, risk-accepting audience.
- It should be distinguished from agentic programming, where developers review and care about generated code.