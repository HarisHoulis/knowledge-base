---
domain: ai-workflows
subdomain: agent evaluation
concept: reusable-agent-eval-frameworks
title: Building Reusable Evaluation Frameworks for Agentic AI Products
sources:
  - title: "Presentation: Building Reusable Evaluation Frameworks for Agentic AI Products"
    url: "https://www.infoq.com/presentations/elastic-ai-agent-evaluations/"
    author: "Susan Chang"
    date: "2026-10-05"
---

# Building Reusable Evaluation Frameworks for Agentic AI Products

Susan Chang describes how Elastic moved from siloed, ad-hoc evaluations of AI agents to a single unified, production-grade evaluation framework (Chang, InfoQ). The starting problem was fragmentation: separate teams running their own inconsistent evals, which made regressions hard to detect and results hard to compare across products.

A central design decision is combining two complementary scoring strategies: LLM-as-a-judge for the open-ended, qualitative aspects of agent behavior, and deterministic rules for cases where exact, reproducible checks are possible. Balancing these gives coverage that neither approach provides alone (Chang, InfoQ).

The framework also has to span a language boundary: evaluation logic prototyped by data scientists in Python must connect to production code written in TypeScript. Bridging these preserves the speed of data-science iteration while keeping evals tied to what actually ships.

Finally, Chang emphasizes deep tracing as the mechanism for catching regressions in complex workloads such as RAG and cybersecurity, where generic metrics would lose the domain context needed to judge whether an agent's output is actually correct (Chang, InfoQ).

- Elastic replaced siloed, ad-hoc agent evaluations with one unified, production-grade evaluation framework.
- LLM-as-a-judge is balanced against deterministic rules rather than used exclusively.
- Python data-science evals are bridged with TypeScript production code.
- Deep tracing is used to catch regressions across complex RAG and cybersecurity workloads while preserving domain context.