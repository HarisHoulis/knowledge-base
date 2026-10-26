---
domain: ai-workflows
subdomain: agentic-architecture
concept: agentic-harness-evolution
title: The Evolution of Agentic Harnesses: From Chains to Graph to Code
sources:
  - title: "The Evolution of Agentic Harnesses: From Chains to Graph to Code"
    url: "https://www.infoq.com/articles/agentic-ai-architecture-harness-evolution/"
    author: "Karthik Ramgopal"
    date: "2026-10-26"
---

# The Evolution of Agentic Harnesses: From Chains to Graph to Code

Karthik Ramgopal traces how agentic LLM systems have progressed through three architectural stages: linear prompt chains, graph-based workflows, and code-executing harnesses. Chains are the simplest form but are fragile, since a failure at any step propagates through the sequence. Graphs add branching, retries, and validation, making workflows more robust and controllable.

The most recent stage, code-executing harnesses, verifies model outputs through actual execution rather than relying on the model's own claims. This shifts validation from inspection to runtime evidence.

The article's central guidance is to validate model outputs and to choose the least complex design that still meets the system's reliability, speed, and cost requirements, rather than defaulting to the most sophisticated harness.

- Agentic architectures evolved from linear chains to graphs to code-executing harnesses
- Chains are simple but fragile; graphs add branching, retries, and validation
- Code harnesses verify outputs through execution
- Pick the least complex design that meets reliability, speed, and cost needs
- Always validate model outputs