---
domain: ai-workflows
subdomain: finops-ai-agents
concept: ai-agent-cost-attribution
title: FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft
sources:
  - title: "FinOps for AI Agents: Who Spent All the Tokens?"
    url: "https://www.youtube.com/watch?v=GJX19pNhmSw"
    author: "Tisha Chawla & Susheem Koul, Microsoft"
    date: "2026-08-22T14:30:07+00:00"
---

# FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft

The talk addresses the critical challenge of cost management in agentic AI systems, marking a shift from 'token maxing' to 'value maxing.' The speakers compare control surfaces across software eras: SaaS relied on UIs and usage caps, cloud on pay-as-you-go and autoscaling, but the agentic era lacks a proper control plane for model calls. They highlight real-world incidents of unbounded consumption, such as AI budgets exhausted within months, and argue for a first-principles approach to design systems that solve cost problems at the root (Chawla & Koul, 2026).

Three core principles are outlined: token as the unit of cost, the model call boundary as the point where cost is created, and the necessity of attribution to know which agent or run caused spending. Without attribution, control is impossible. The ideal platform should monitor at the run level—controlling the loop between agents and tools—rather than just acting as a model gateway. Policies should prevent runaway loops and excessive context growth, with hard budget caps only as a last resort (Chawla & Koul, 2026).

- Token is the unit of cost, so value must be measured in tokens too.
- Cost is created at the LLM boundary; track and attribute every model call.
- Existing model gateways handle routing and caps but miss run-level control.
- Implement policies to stop runaway loops and context bloat before hitting budget caps.
- Shift from token maxing to value maxing by designing a control plane for agentic calls.