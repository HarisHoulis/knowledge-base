---
domain: ai-workflows
subdomain: llm-assisted-development
concept: structured-prompt-driven-development
title: Structured-Prompt-Driven Development (SPDD)
sources:
  - title: "Structured-Prompt-Driven Development (SPDD)"
    url: "https://martinfowler.com/articles/structured-prompt-driven/"
    author: "Martin Fowler"
---

# Structured-Prompt-Driven Development (SPDD)

Structured-Prompt-Driven Development (SPDD) is a workflow developed by Thoughtworks' internal IT organization for using LLM programming assistants effectively in team settings. The method, described by Wei Zhang and Jessie Jie Xia, treats prompts as first-class artifacts that are kept with the code in version control, ensuring that the AI-assisted development process remains aligned with business needs. This approach addresses the limitation that LLM assistants often provide value mainly to individual developers, by formalizing prompt management as part of the development lifecycle.

The workflow emphasizes three key skills for developers: alignment, abstraction-first, and iterative review. Alignment ensures that prompts and generated code reflect business goals; abstraction-first encourages designing high-level structures before diving into details; and iterative review involves continuously refining both prompts and code outputs. By integrating prompts into version control, teams can track changes, collaborate more effectively, and maintain consistency. A simple example of this workflow is available on GitHub, illustrating its practical application (Fowler, 'Structured-Prompt-Driven Development').

- Treat prompts as first-class artifacts, stored in version control alongside code.
- SPDD aligns LLM-assisted development with business needs through structured workflows.
- Three essential developer skills: alignment, abstraction-first, and iterative review.
- Thoughtworks' internal IT organization developed SPDD for team-based LLM usage.
- A working example of the workflow is available on GitHub.