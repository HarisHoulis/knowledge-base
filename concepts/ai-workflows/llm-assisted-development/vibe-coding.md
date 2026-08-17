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

Vibe coding is a software development approach where a user builds an application by prompting an LLM, testing it, and requesting changes—without ever reading or reviewing the generated code. Coined by Andrej Karpathy in February 2025, the essence is to "forget that the code even exists." This allows people with no programming knowledge to create functional software, and experienced programmers may use it for rapid prototypes or disposable projects. However, because the code is never inspected, it often suffers from maintainability, correctness, and security problems, making it unsuitable for widely-used or sensitive applications.

The article distinguishes vibe coding from agentic programming (or agentic coding), where programmers actively review and care about the code structure produced by LLMs. While the term "vibe coding" has caught on broadly, Fowler emphasizes keeping the two concepts separate due to their different practices and consequences. Vibe coding's risks include a large attack surface for security exploits, potentially exposing credentials or sensitive data, as well as low-quality code that becomes hard for even LLMs to modify later. Additionally, LLM hallucination and non-determinism can introduce incorrect behavior or new errors in code that should have remained unchanged.

Given these limitations, vibe coding is best reserved for disposable software used by its author or a small, risk-aware group. Applications that are more complex, widely-used, or carry serious consequences should not be "forgotten about."

- Vibe coding means building software by prompting an LLM without examining the generated code, as coined by Andrej Karpathy in 2025.
- It separates from agentic programming, where programmers actively review and manage LLM-generated code.
- Major risks include security vulnerabilities, poor maintainability, and hallucination-induced incorrect behavior.
- Best suited for disposable software with a limited, risk-aware audience, not for complex or sensitive systems.