---
domain: ai-workflows
subdomain: llm-coding
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
    date: "2025"
---

# Bliki: Vibe Coding

Vibe coding, a term coined by Andrej Karpathy in February 2025, refers to building software by prompting an LLM and not looking at the generated code (Karpathy). Martin Fowler notes that this approach lets people without programming knowledge create applications, but the resulting software often has maintainability, correctness, and security issues. He emphasizes that the key point is 'forget that the code even exists' (Fowler).

Fowler distinguishes vibe coding from agentic programming: the latter involves programmers who still care about the code, review it, and pay attention to structure. While 'vibe coding' has caught on broadly, Fowler argues for keeping the concepts separate because they differ in use and consequences.

Risks include a large attack surface for security threats, the likelihood of low-quality code that is difficult to modify, and LLM hallucinations that produce incorrect behavior. Non-determinism can also introduce errors in unrelated parts of the code. Consequently, Fowler recommends using vibe coding only for disposable software with a limited, risk-accepting audience.

- Vibe coding is building software by prompting LLMs without examining the generated code.
- It's accessible to non-programmers but poses risks in maintainability, correctness, and security.
- Fowler distinguishes vibe coding from agentic programming, where programmers still engage with code.
- Risks include security vulnerabilities, low-quality code, hallucination, and non-deterministic errors.
- Best suited for disposable software with a limited audience and low risk.