---
domain: ai-workflows
subdomain: llm-coding
concept: vibe-coding
title: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Vibe Coding

Vibe coding is a software development approach where an individual builds applications by prompting an LLM and following its output without inspecting the generated code. The term was coined by Andrej Karpathy in February 2025, who described it as fully giving in to the vibes, forgetting that the code exists, and accepting all changes blindly (source: https://martinfowler.com/bliki/VibeCoding.html). This method enables people with no programming knowledge to create functional software for their own use or for small, trusted groups. However, because the code is never reviewed, it often suffers from serious maintainability, correctness, and security problems.

- Vibe coding means building software by prompting an LLM and never reading the code it generates.
- It lowers the barrier for non-programmers but introduces significant risks, such as security vulnerabilities and incorrect behavior.
- Fowler distinguishes vibe coding from agentic programming, where developers actively review and manage the AI-generated code.
- Vibe coding is best suited for disposable software with a limited audience that accepts the associated risks.