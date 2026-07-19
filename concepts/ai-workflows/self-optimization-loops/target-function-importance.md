---
domain: ai-workflows
subdomain: self-optimization-loops
concept: target-function-importance
title: Stop Burning Tokens: Why self-improvement needs domain expertise first
sources:
  - title: "Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse"
    url: "https://www.youtube.com/watch?v=eAXxdtNlK04"
    author: "AI Engineer"
    date: "2026-07-18T20:15:06+00:00"
---

# Stop Burning Tokens: Why self-improvement needs domain expertise first

Annabell Schäfer argues that effective self-improvement loops for AI applications require investing in domain expertise to define clear target functions and evaluators early. Unlike coding, where 'does the code compile' provides a straightforward yes/no signal, many domains (e.g., healthcare, compliance) lack such clear metrics, making it critical to capture what the application should achieve. She presents a minimal self-optimization loop using arXiv paper classification (single-label classification) as a clear-cut example, where accuracy directly measures performance. The loop uses a small model (GPT-5 nano) for the agent and a frontier model (Claude 4.8) to propose prompt updates, demonstrating that even with a simple target function, continuous improvement is possible. The key takeaway: teams that invest in building robust target functions and evaluators are the ones who can ship with confidence and steadily improve their applications.

- Coding benefits from a clear target function (code compiles or not), but most AI domains lack such clarity, requiring deliberate design of evaluators.
- Investing early in domain expertise to define what 'good' looks like enables continuous improvement and confident shipping.
- A minimal self-optimization loop using classification (e.g., arXiv papers) with accuracy as the target function demonstrates how automation can work in clear-cut cases.
- Using a small, cheap model for the agent and a frontier model for optimization helps balance cost and performance.