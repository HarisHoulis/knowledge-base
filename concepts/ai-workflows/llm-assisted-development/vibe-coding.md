---
domain: ai-workflows
subdomain: llm-assisted-development
concept: vibe-coding
title: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Vibe Coding

Vibe coding is a software development technique where the developer prompts an LLM to build an application, tests it, and requests changes, all without inspecting the generated code. The term was coined by Andrej Karpathy in February 2025, who described it as "forgetting that the code even exists." This approach enables people without programming knowledge to create software, but it carries significant risks for maintainability, correctness, and security, making it suitable mostly for disposable software with a limited audience.

Martin Fowler distinguishes vibe coding from agentic programming, where developers actively review and manage LLM-generated code. He notes that while many programmers now use LLMs to write code, vibe coding specifically involves no code review and no concern for internal structure. This distinction matters because the consequences of the two practices differ: vibe coding is accessible to non-programmers but yields low-quality code that is hard to maintain, while agentic programming retains human oversight.

The article highlights serious limitations of vibe coding: LLMs are vulnerable to security attacks and can expose sensitive data; they produce large amounts of low-quality code that is hard for even LLMs to modify later; and they hallucinate, leading to incorrect behavior that may go unnoticed. Additionally, LLM non-determinism means enhancements can introduce errors in unrelated parts of the code. Therefore, vibe-coded software should be limited to disposable projects or small trusted groups, and developers must be aware of risks like the "Lethal Trifecta."

- Vibe coding means building software by prompting an LLM without reading or reviewing the generated code.
- The term was coined by Andrej Karpathy in February 2025 and emphasizes 'forgetting that the code even exists.'
- It enables non-programmers to create apps but results in low-quality, insecure, and hard-to-maintain code.
- It differs from agentic programming, where developers actively oversee and care about the code structure.
- Vibe coding is best reserved for disposable or low-stakes software with a small, risk-aware audience.