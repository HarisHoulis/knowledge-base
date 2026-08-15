---
domain: engineering-culture
subdomain: ai-assisted-development
concept: vibe-coding
title: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Vibe Coding

Vibe coding is a software development approach where the user prompts an LLM to build or modify an application, runs it, and iterates based on feedback, but never reviews the generated code. As Martin Fowler describes, the key point is to 'forget that the code even exists,' which makes the technique accessible to people without programming knowledge but also introduces significant risks. Because the code is not examined, it is best suited for disposable software used by a limited audience who accept the trade-offs.

The term was coined by Andrej Karpathy in February 2025, who described fully giving in to the vibes, accepting all changes without reading diffs, and working around bugs with random prompts. Fowler distinguishes vibe coding from his own concept of 'agentic programming,' where programmers still review and care about the code even when an LLM writes it. He notes that while 'vibe coding' has become a popular buzzword, it is worth keeping the two concepts separate because they lead to different practices and outcomes.

Fowler highlights several risks: security vulnerabilities from unexamined code, poor maintainability due to low-quality structure, and incorrect behavior from LLM hallucinations and non-determinism. These risks make vibe-coded software inappropriate for widely-used or sensitive applications. Instead, it is best reserved for throwaway projects or prototypes where the user understands and accepts the limitations.

- Vibe coding means telling an LLM what to build and iterating without ever reading the generated code.
- The term was coined by Andrej Karpathy in February 2025.
- It differs from agentic programming, where developers still review and care about the code.
- Major risks include security vulnerabilities, poor maintainability, and incorrect behavior due to LLM limitations.
- Best used for disposable software with a small, risk-accepting audience.