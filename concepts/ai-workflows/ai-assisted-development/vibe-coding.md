---
domain: ai-workflows
subdomain: ai-assisted-development
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Bliki: Vibe Coding

Vibe coding, a term coined by Andrej Karpathy in February 2025, refers to building software by prompting an LLM and not looking at the generated code. Martin Fowler highlights that the key point is to "forget that the code even exists," which makes it accessible to non-programmers but introduces significant risks. Fowler distinguishes vibe coding from agentic programming, where developers still review and care about the code structure, even if they don't write it line by line. Vibe coding is best suited for disposable software for a limited audience, as the resulting code often suffers from maintainability, correctness, and security issues. Risks include security vulnerabilities, low-quality code that is hard even for LLMs to modify, and LLM hallucinations leading to incorrect behavior. Non-determinism can also introduce errors in unrelated parts of the code when changes are requested. Therefore, more complex, widely-used software with higher consequences should not be vibe coded.

- Vibe coding is building software by prompting an LLM without reviewing the generated code.
- The term was coined by Andrej Karpathy in February 2025 and popularized by Martin Fowler's analysis.
- Vibe coding differs from agentic programming: in the latter, programmers still review and care about the code.
- Major risks include security vulnerabilities, poor maintainability, hallucinations, and non-determinism-induced errors.
- Best used for disposable, low-stakes software; not for complex or widely-used systems.