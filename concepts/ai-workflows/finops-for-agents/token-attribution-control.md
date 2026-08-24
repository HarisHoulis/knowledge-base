---
domain: ai-workflows
subdomain: finops-for-agents
concept: token-attribution-control
title: FinOps for AI Agents: Who Spent All the Tokens?
sources:
  - title: "FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft"
    url: "https://www.youtube.com/watch?v=GJX19pNhmSw"
    author: "Tisha Chawla & Susheem Koul"
    date: "2026-08-22T14:30:07+00:00"
---

# FinOps for AI Agents: Who Spent All the Tokens?

The talk addresses the critical challenge of managing costs in AI agent workflows, where token spend can rapidly spiral out of control. The speakers, Tisha Chawla and Susheem Koul, highlight a shift from 'token maxing'—spending as many tokens as possible for exploration—to 'value maxing,' which requires visibility and control over where tokens are consumed. They draw parallels with past software eras, noting that while SaaS used usage caps and cloud used auto-scaling, the agentic era lacks a proper control plane for model calls. Real-world incidents like Uber exhausting its AI budget in four months and runaway loops causing massive costs underscore the urgency of this problem.

- Shift from token maxing to value maxing is essential as AI agent costs become unpredictable.
- Cost is created at the model call boundary, so attribution to specific agent runs is critical for control.
- Control policies should handle excessive loops and context growth inline, not just halt via budget caps.
- Existing token management tools act as model gateways but lack run-level monitoring and control.
- An ideal platform must control the agent-tool loop and sub-agent spawning at the run level.