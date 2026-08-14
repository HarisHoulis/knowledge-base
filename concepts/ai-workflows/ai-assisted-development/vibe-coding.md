---
domain: ai-workflows
subdomain: ai-assisted-development
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Bliki: Vibe Coding

Vibe coding is a software development approach where the developer prompts an LLM to build or modify an application but never reads or reviews the generated code. The term was coined by Andrej Karpathy in February 2025, who described fully relinquishing control to the AI: "forget that the code even exists." Martin Fowler explains that this enables people with no programming knowledge to create software, but it also introduces significant risks around maintainability, correctness, and security. Because the coder does not inspect the code, issues are easily overlooked, making the approach best suited for disposable software used by a limited audience [1](https://martinfowler.com/bliki/VibeCoding.html).

Fowler distinguishes vibe coding from agentic programming, another AI-driven workflow where programmers still care about the code, review diffs, and maintain internal structure. In vibe coding, the developer may not even know how the software works internally. The term has suffered from semantic diffusion, with many using it for any LLM-driven development, but Fowler argues the distinction is important because the consequences differ greatly. Experienced programmers might use vibe coding for prototypes or throwaway projects, but they would not use it for production systems where reliability matters [1](https://martinfowler.com/bliki/VibeCoding.html).

The limitations of vibe coding are closely tied to the nature of LLMs. Security is a major concern: LLM-generated applications can expose sensitive information or create backdoors, and users may unintentionally enable the "lethal trifecta" of agents, permissions, and exposed secrets. Code quality is often poor, making future changes difficult even for AI. Hallucinations can produce incorrect behavior, and non-determinism means adding features can introduce bugs in unrelated areas. Consequently, vibe coding should be reserved for low-stakes, disposable software; any code with broader usage, complexity, or significant risk demands human oversight [1](https://martinfowler.com/bliki/VibeCoding.html).

- Vibe coding means building software entirely by prompting an LLM without reading or reviewing the code it generates.
- The approach is accessible to non-programmers but is best for disposable prototypes or personal projects, not production software.
- Distinct from agentic programming, where developers still engage with and maintain the codebase.
- Major risks include security vulnerabilities, poor maintainability, hallucinated behavior, and non-deterministic regressions.