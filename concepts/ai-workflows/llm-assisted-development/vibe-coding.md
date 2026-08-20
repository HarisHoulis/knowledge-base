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

Vibe coding, as defined by Martin Fowler in his Bliki article, is a software development technique where the developer prompts an LLM to build an application and then interacts with it through outputs and error messages, without ever examining the generated code. The term was coined by Andrej Karpathy in February 2025, who described it as 'forgetting that the code even exists.' This approach enables people without programming knowledge to create software, but it also introduces significant risks.

Fowler distinguishes vibe coding from what he calls 'agentic programming,' where programmers also delegate code generation to LLMs but remain actively involved in reviewing and structuring the code. In vibe coding, the code is entirely ignored, making it a different practice with different consequences. The article warns that vibe-coded software often suffers from maintainability, correctness, and security issues, including the exposure of sensitive information or credentials.

Because of these limitations, Fowler suggests that vibe coding is best suited for disposable software used only by a small audience, such as the author or close collaborators who accept the risks. The lack of code oversight makes it difficult for even LLMs to modify the software later, and the models' tendency to hallucinate can lead to incorrect behavior that goes unnoticed. While LLM capabilities are improving, the article emphasizes treating such software with skepticism.

- Vibe coding means building apps by prompting an LLM without reviewing the generated code, a term coined by Andrej Karpathy.
- It differs from agentic programming, where programmers still oversee code quality and structure.
- Risks include security vulnerabilities, poor maintainability, and incorrect behavior due to LLM hallucinations and non-determinism.
- Best used for disposable software intended for a limited audience who understand and accept the risks.