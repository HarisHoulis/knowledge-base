---
domain: ai-workflows
subdomain: llm-coding-practices
concept: vibe-coding
title: Vibe Coding: Prompt-Driven Development Without Reading Code
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Vibe Coding: Prompt-Driven Development Without Reading Code

Vibe coding, a term coined by Andrej Karpathy in February 2025, refers to building software by prompting an LLM and iterating on the results without ever reading the generated code. As Martin Fowler explains, the key point is to 'forget that the code even exists'. This approach allows people without programming knowledge to build applications for their own use, and experienced programmers may use it for rapid prototyping or disposable software. However, because the coder does not review or understand the code, the resulting software often has maintainability, correctness, and security issues.

- Vibe coding means building applications by prompting an LLM and ignoring the generated code, relying entirely on the model's output.
- It differs from agentic programming, where programmers still review and care about the code structure even if LLMs write most of it.
- Security is a major concern, as LLM-generated code can expose sensitive information or credentials, especially when used widely.
- Vibe-coded software is best for disposable, low-risk applications, not for complex or widely-used systems.