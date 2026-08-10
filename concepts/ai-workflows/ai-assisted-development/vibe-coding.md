---
domain: ai-workflows
subdomain: ai-assisted-development
concept: vibe-coding
title: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Vibe Coding

Vibe coding is a software development approach where the user prompts an LLM to build an application, tries it out, and iterates based on feedback, but never inspects the generated code. The term was coined by Andrej Karpathy in February 2025, emphasizing 'forgetting that the code even exists' (Fowler). This technique enables people without programming knowledge to create functional software, but it introduces significant risks related to maintainability, correctness, and security.

Martin Fowler distinguishes vibe coding from 'agentic programming,' where programmers also rely heavily on LLMs but still review and care about code structure. He notes that the term 'vibe coding' has undergone semantic diffusion, but keeping the concepts separate is useful because they differ in use and consequences (Fowler).

Key risks include security vulnerabilities due to the large attack surface of LLMs, low-quality code that becomes difficult to modify, hallucinated behaviors, and non-deterministic regressions introduced during enhancements. Fowler recommends vibe coding only for disposable software used by a small, risk-aware audience, while more complex or widely-used software should not be 'forgotten about' (Fowler).

- Vibe coding means building software by prompting an LLM without reading the generated code.
- It enables non-programmers to create apps but is best for disposable or prototype software.
- Fowler distinguishes vibe coding from agentic programming, where programmers still review code.
- Major risks include security vulnerabilities, poor maintainability, hallucinations, and non-deterministic errors.