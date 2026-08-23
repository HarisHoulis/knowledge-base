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

Vibe coding is a term coined by Andrej Karpathy in February 2025, describing a practice where developers build software by prompting an LLM and never reading or reviewing the generated code. The key idea is to "forget that the code even exists." This approach allows people without programming knowledge to create applications by iterating through prompts, accepting all suggestions, and pasting error messages back into the LLM. While convenient for throwaway weekend projects, it carries significant risks because the resulting code is often low-quality, hard to maintain, insecure, and prone to subtle errors (Fowler).

- Vibe coding means building software by prompting an LLM without looking at the code it generates.
- The term was coined by Andrej Karpathy in February 2025 and has since diverged from 'agentic programming,' where developers actively review and guide AI-generated code.
- It is best suited for disposable software for a limited audience, not for complex or widely used applications.
- Risks include security vulnerabilities, poor maintainability, hallucinated behavior, and non-deterministic regressions.
- Non-programmers using vibe coding should still be aware of security risks like the 'Lethal Trifecta.'