---
domain: ai-workflows
subdomain: coding-agents
concept: continuous-ai-code-review
title: Continuous AI Code Review at Anthropic's Claude Code Team
sources:
  - title: "How the Claude Code team does code review"
    url: "https://claude.dev/blog/solving-code-review-at-anthropic/"
    author: "Addy Osmani, Morgan Westlee Lunt, and Qing Wang"
---

# Continuous AI Code Review at Anthropic's Claude Code Team

Addy Osmani, Morgan Westlee Lunt, and Qing Wang argue that "did a human read the code?" is an imprecise proxy for the real question: what could go wrong with this change, and which check—automated or human—is the right one to catch it? [source](https://claude.dev/blog/solving-code-review-at-anthropic/)

Reframing review around that question also changed when review happens. Previously review was a gate at the end of the road: write the code, open a PR, wait for a colleague. Now review runs continuously, more like spellcheck while you write. [source](https://claude.dev/blog/solving-code-review-at-anthropic/)

In this workflow, most changes have been reviewed and fixed by Claude at least once before a human is asked to look. This catches most routine mistakes and saves team attention for higher-level questions and scrutiny. [source](https://claude.dev/blog/solving-code-review-at-anthropic/)

- "Did a human read the code?" is an imprecise proxy for asking what could go wrong and which check—automated or human—should catch it.
- AI-assisted review shifts from an end-of-road PR gate to continuous review, like spellcheck while writing.
- Most changes are reviewed and fixed by Claude at least once before a human looks, catching routine mistakes.
- Human attention is reserved for higher-level questions and scrutiny.