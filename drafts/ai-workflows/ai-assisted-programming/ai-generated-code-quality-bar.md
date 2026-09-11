---
domain: ai-workflows
subdomain: ai-assisted-programming
concept: ai-generated-code-quality-bar
title: Holding AI-Written Production Code to a Higher Bar
sources:
  - title: "Quoting Boris Cherny"
    url: "https://simonwillison.net/2026/Sep/11/boris-cherny/"
    author: "Boris Cherny (quoted by Simon Willison)"
    date: "2026-09-11"
---

# Holding AI-Written Production Code to a Higher Bar

Boris Cherny argues that production code written by Claude should be held to a higher standard than code written by a human. The justification is that AI-generated code without sufficient verification and tooling risks accumulating into a codebase that is hard to maintain.

To enforce that higher bar, Anthropic relies on a set of layered guardrails: extensive lint rules, extensive tests, Claude-driven end-to-end tests, Claude-powered fuzzers that run daily, automated code reviews and security reviews, and automated code refactoring. Cherny frames these as necessary measures rather than optional niceties — without them, the output degrades into a maintenance burden.

- Production code written by Claude should meet a higher bar than human-written code.
- Anthropic enforces this with layered guardrails: lint rules, tests, Claude-driven end-to-end tests, and daily Claude-powered fuzzers.
- Automated code reviews, security reviews, and automated refactoring are part of the same safety net.
- Without such guardrails, AI-generated code can become a mess that is hard to maintain.