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

Vibe coding is a software development approach where the user prompts an LLM to build an application, iterates based on trial and error, and does not read or inspect the generated code. The term was coined by Andrej Karpathy in February 2025, who described it as fully giving in to the vibes, accepting all changes, and forgetting that the code even exists. This technique allows people without programming knowledge to create software, making it useful for personal or throwaway projects, but it often leads to maintainability, correctness, and security issues (Fowler, 2025).

Fowler distinguishes vibe coding from agentic programming, where programmers still care about and review the code produced by LLMs. While vibe coding is convenient and accessible, it carries significant risks: LLMs can generate insecure code, accumulate poorly structured software that is hard to modify, and hallucinate behaviors that result in incorrect functionality. Therefore, vibe-coded software is best suited for disposable applications used only by a small, risk-aware group, while more consequential software should not be left entirely to autopilot (Fowler, 2025).

- Vibe coding means building software by prompting an LLM without looking at the generated code.
- It was coined by Andrej Karpathy in early 2025 and enables non-programmers to create simple applications.
- It differs from agentic programming, where developers review and maintain the LLM-written code.
- Major risks include security vulnerabilities, poor code quality, and hallucinated behavior.
- Best use case is disposable software for a limited audience, not critical or widely used systems.