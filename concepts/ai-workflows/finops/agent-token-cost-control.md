---
domain: ai-workflows
subdomain: finops
concept: agent-token-cost-control
title: FinOps for AI Agents: Who Spent All the Tokens?
sources:
  - title: "FinOps for AI Agents: Who Spent All the Tokens?"
    url: "https://www.youtube.com/watch?v=GJX19pNhmSw"
    author: "Tisha Chawla & Susheem Koul, Microsoft"
    date: "2026-08-22"
---

# FinOps for AI Agents: Who Spent All the Tokens?

The talk addresses the challenge of managing and attributing costs in AI agent workflows, where token consumption can become unbounded and difficult to trace. The authors observe a shift from 'token maxing'—optimizing for maximum token usage—to 'value maxing,' where every token spent must be justified by business value. They draw parallels to prior software eras: SaaS used UI and seat limits, cloud used pay-as-you-go with autoscaling, but the agentic era lacks a proper control plane for model calls, leading to runaway costs and exhausted budgets (e.g., Uber's AI budget depleted in four months). The core first principles are: (1) token is the unit of cost, so value must be measured in tokens; (2) cost is created at the LLM model-call boundary, so tracking must happen there; (3) without fine-grained attribution, it's impossible to control which agent or run caused the spend; and (4) policies must be in place to stop excessive loops or context growth before resorting to hard budget caps. The ideal platform should monitor at the 'run' level, not just the model-request level, and control the loop between agent, tools, and subagent spawning.

- Token is the unit of cost, so value must also be evaluated in token terms to move from token maxing to value maxing.
- Cost is incurred at the LLM call boundary; proper attribution is required to identify which agent run caused the spend.
- Existing model gateways offer hard caps and routing but lack control over the internal loop between agents and tools.
- An ideal control plane should monitor at the run level and apply policies to halt excessive loops or context growth before a budget cap is hit.
- Unbounded consumption is a real risk, with examples like Uber exhausting its AI budget in four months and companies incurring millions in costs from runaway loops.