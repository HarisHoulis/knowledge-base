---
domain: ai-workflows
subdomain: long-horizon-agents
concept: long-horizon-agents
title: Inside Arca's Long-Horizon Agents That Run the Business
sources:
  - title: "Inside Arca's Long-Horizon Agents That Run the Business - Aman Singh, Arca"
    url: "https://www.youtube.com/watch?v=oP2WLFpMoDY"
    author: "AI Engineer"
    date: "2026-10-23"
---

# Inside Arca's Long-Horizon Agents That Run the Business

Aman Singh, who leads the AI department at Arca, describes how the financial-services firm deploys AI agents that own long-term business outcomes end to end rather than acting as assistants. Arca provides financial planning, tax planning, asset management, and investment advice, and its agents execute the decisions that shape customer results rather than sitting in a side pilot.

Work in financial services is long-horizon: a single client goal can span about 10 days with many participants, decision points, and handoffs. The example given is a client, Jane, who owes $100,000 in taxes and needs the most tax-efficient way to raise the funds — a consultant analyzes the tax-optimal approach, a trader liquidates assets over several days to settle, and operations specialists initiate an ACH that itself takes days to clear. Scaling this across clients makes human effort grow exponentially, which motivated Arca's different approach.

Arca is not a SaaS company selling software; it is an applied AI company that happens to deliver services. Its agents own the whole long-term outcome from start to finish, supported by signals from the outside world (emails, phone calls, documents, meetings, custodian events, market movements), operational context on how to handle each situation, tools with protective shields, long-term memory retention, and the ability to collaborate with people. This removes people from the critical path — no one needs to babysit a goal for days while agents work on it.

The talk follows the path of Jane's tax email: it is one of many signals that agents constantly evaluate to advance their work, backed by deep customer memory (e.g., never raising Jane's Apple position because of something she said eight months ago) and a sandbox for financial calculations. After the analysis, agents create a plan that cannot be implemented without people; they lay it out in a shared space in the product where multiple people can communicate with the agent about the plan and where humans are brought in.

- Arca's agents own long-horizon client outcomes end to end (e.g., a ~10-day tax-funding workflow) rather than assisting from the sidelines.
- Financial-services work involves many participants, decision points, and handoffs — consultant analysis, multi-day asset settlement, and multi-day ACH — which scales poorly with human effort.
- Agents are equipped with external signals, operational context, tools with protective shields, long-term memory, and human collaboration.
- People are removed from the critical path so no one must monitor a goal for days while agents work.
- Agent-generated plans are surfaced in a shared product space where multiple humans can communicate with the agent to execute them.