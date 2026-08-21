---
domain: ai-workflows
subdomain: vibe-coding
concept: vibe-coding
title: Bliki: Vibe Coding
sources:
  - title: "Bliki: Vibe Coding"
    url: "https://martinfowler.com/bliki/VibeCoding.html"
    author: "Martin Fowler"
---

# Bliki: Vibe Coding

Vibe coding is a software development technique where users build applications by prompting an LLM and accepting the generated code without reviewing it. Coined by Andrej Karpathy in February 2025, the term emphasizes 'forgetting that the code even exists,' enabling people without programming skills to create software. However, this approach carries significant risks, including poor maintainability, security vulnerabilities, and correctness issues due to LLM hallucination and non-determinism (Fowler, "Bliki: Vibe Coding", https://martinfowler.com/bliki/VibeCoding.html).

Fowler distinguishes vibe coding from agentic programming, where programmers review and care about the LLM-generated code despite heavy delegation. Vibe coding is best suited for disposable software used by a small, risk-aware audience. For more complex or widely used software, ignoring the code's structure and security can lead to serious problems, especially as LLMs struggle with poorly structured code and may introduce errors during enhancements (Fowler, "Bliki: Vibe Coding").

- Vibe coding means building software via LLM prompts without reading or reviewing the generated code.
- It lowers the barrier for non-programmers but risks maintainability, security, and correctness.
- Distinct from agentic programming, where developers actively oversee and structure LLM-generated code.
- Best used for throwaway or limited-audience projects; high-stakes software requires human oversight.