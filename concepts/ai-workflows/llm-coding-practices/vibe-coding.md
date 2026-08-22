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

Vibe coding is a technique for building software by prompting an LLM with natural language, running the result, and iterating based on feedback, without inspecting the generated code. The term was coined by Andrej Karpathy in February 2025, and the key defining aspect is to 'forget that the code even exists'. This allows people without programming knowledge to create applications, as they only interact with the LLM through prompts and outputs, not by reading or editing code directly.

Martin Fowler distinguishes vibe coding from agentic programming, where developers also have LLMs write code but still review and care about its internal structure. He notes that the term 'vibe coding' has semantically diffused and is often used for agentic programming, but argues that keeping them separate is useful since they differ in practice and consequences. Vibe coding is especially suited for disposable software, prototypes, or personal tools, and experienced programmers may use it for rapid, low-stakes development.

However, vibe coding carries significant risks. LLM-generated software often has poor maintainability, correctness, and security. Because the code is not reviewed, it can accumulate low-quality structure that even LLMs struggle to modify later. Security risks are particularly serious, as vibe-coded applications may expose sensitive information or credentials, and the 'lethal trifecta' of LLM vulnerabilities can threaten broader systems. LLM hallucination and non-determinism can also introduce subtle bugs that users may not notice. Therefore, vibe coding is best reserved for disposable, limited-audience software, while complex or consequential code should be handled with more care.

- Vibe coding is building software by prompting an LLM without reading or understanding the generated code, enabling non-programmers to create simple applications.
- It differs from agentic programming, which involves developers reviewing and caring about LLM-generated code, despite the popular conflation of the two terms.
- Vibe-coded software often suffers from poor maintainability, correctness, and security, and is best used for disposable or low-stakes projects.
- Security risks include exposing sensitive data or credentials, amplified by the inherent vulnerabilities of LLMs and the 'lethal trifecta'.
- LLM hallucination and non-determinism can introduce invisible errors, making it essential to treat vibe-coded software with skepticism.