---
domain: ai-workflows
subdomain: llm-coding-practices
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Bliki: Vibe Coding

Vibe coding is a technique for building software by prompting an LLM, then trying it out and prompting for changes, without ever looking at the generated code. The term was coined by Andrej Karpathy in February 2025, and the key characteristic is to 'forget that the code even exists.' This allows people without programming knowledge to build applications, but it also introduces significant trade-offs in maintainability, correctness, and security, making it best suited for disposable software with a limited audience.

According to Martin Fowler's article, vibe coding is distinct from agentic programming, where programmers use LLMs to write code but still review and care about its internal structure. The rapid adoption of the term has led to semantic diffusion, but Fowler emphasizes the importance of keeping these concepts separate because they differ both in use and consequences.

Fowler highlights several risks: LLMs provide a large attack surface, making vibe-coded applications vulnerable to security breaches and credential exposure. The lack of attention to code can lead to poor-quality, spaghetti-like code that is hard for both humans and LLMs to modify. Additionally, LLMs are prone to hallucinations and non-deterministic behavior, which can introduce errors even in unrelated parts of the software when changes are requested.

Given these limitations, Fowler advises that vibe coding is appropriate for throwaway projects or prototypes used by a small group who accept the risks. More complex, widely-used, or security-sensitive software should not be built with this approach, as the consequences of errors are too severe.

- Vibe coding means building software by prompting an LLM and not reading the generated code.
- Coined by Andrej Karpathy in February 2025, it enables non-programmers to create applications.
- It differs from agentic programming, where developers still review and care about the code.
- Major risks include security vulnerabilities, poor maintainability, hallucinated behavior, and non-deterministic errors.
- Best used for disposable software with a limited audience; avoid for complex or sensitive systems.