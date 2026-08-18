---
domain: ai-workflows
subdomain: ai-assisted-development
concept: vibe-coding
title: Vibe Coding (Martin Fowler's Bliki)
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Vibe Coding (Martin Fowler's Bliki)

Vibe coding is a term coined by Andrej Karpathy in February 2025 to describe building software by prompting an LLM without looking at the generated code. As Martin Fowler explains, the key point is to "forget that the code even exists." This allows people without programming knowledge to create applications, but the resulting software often suffers from maintainability, correctness, and security issues, making it best suited for disposable software or limited-audience prototypes.

Fowler distinguishes vibe coding from agentic programming, where programmers also use LLMs to write code but still review and care about its internal structure. He argues that while the term "vibe coding" has experienced semantic diffusion and is often used broadly, it is worth keeping the two concepts separate because they differ in usage and consequences.

The article outlines multiple risks: security vulnerabilities due to LLMs' large attack surface, the generation of large amounts of low-quality code that is hard to modify, and hallucination-induced incorrect behavior. Fowler advises that vibe-coded software should only be used by the author or a small group who accept these risks, while more complex or widely-used software should not be forgotten about.

- Vibe coding means building software by prompting an LLM and ignoring the generated code entirely.
- The approach enables non-programmers to build applications but is best for throwaway or limited-use projects.
- Vibe coding should be distinguished from agentic programming, where programmers actively review and manage code.
- Key risks include security vulnerabilities, poor code quality, and hallucinated incorrect behavior.
- Widely-used or sensitive software should not be developed using vibe coding.