---
domain: ai-workflows
subdomain: ai-coding-practices
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Bliki: Vibe Coding

Vibe coding is a technique where users build software by prompting an LLM, iterating based on results, but never inspecting the generated code. The term was coined by Andrej Karpathy in February 2025, emphasizing that the coder 'forgets that the code even exists.' This approach allows non-programmers to create applications, but it carries significant risks to maintainability, correctness, and security, making it suitable only for disposable software used by a limited audience (Fowler).

Fowler distinguishes vibe coding from agentic programming, where programmers do review and care about the code even though it's AI-generated. Vibe coding's key limitation is that low-quality, unstructured code becomes difficult for both humans and LLMs to modify or enhance. Additionally, LLM hallucinations and non-determinism can produce incorrect behavior without obvious signs, and security vulnerabilities can expose sensitive information. Therefore, vibe coding is best reserved for prototypes or throwaway projects, not critical or widely used software (Fowler).

- Vibe coding means building software purely by prompting an LLM and never looking at the code it generates.
- It enables non-programmers to create apps, but the results often suffer from maintainability, correctness, and security issues.
- Vibe coding should not be confused with agentic programming, where programmers still review and manage the AI-generated code.
- Because of the risks, it's only advisable for disposable, low-stakes software used by a small group.
- LLM capabilities are improving, but well-structured software still matters for effective AI collaboration.