---
domain: ai-workflows
subdomain: agent-architecture
concept: agent-first-software-design
title: Why We Deleted Our MCP Server and Rebuilt It
sources:
  - title: "Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto"
    url: "https://www.youtube.com/watch?v=jJQoVkd5yLg"
    author: "AI Engineer"
    date: "2026-10-08"
---

# Why We Deleted Our MCP Server and Rebuilt It

Abhi Arya of Reducto describes rebuilding their MCP server after an initial version broke in production. Reducto is an agent-based document platform that has processed over 3 billion documents for clients like Harvey, Scale AI, top global technology companies, and hedge funds. The core difficulty is production data: while clean documents yield roughly 60% results with advanced models, messy real-world documents cause hallucination because most corporate data is unstructured.

Arya argues that agent-based software is fundamentally an architectural problem, reducible to one question: who pays for an agent's mistake? He outlines three possible answers. Auto mode optimizes autonomy, letting the agent act freely, but when it errs confidently the user or customer pays the price. User priority optimizes the interface and gives the user full control, but built on a shallow agent it collapses into a regular chatbot, limiting both user understanding and agent capability. The winning category, in his view, is the customer-service-agent experience: structuring the agent's capabilities to give the model rich, clear functionality so it performs what the user needs while a person can check its work.

Reducto builds tools that automate end-to-end document workflows via pipelines: analyze, classify, possibly split into sections, then extract data, for tasks like invoicing and contract management. Users, especially the sales team, were spending all their time on setup rather than results, so the obvious step was an MCP server letting the agent do the hard work. Arya built an MVP with Claude Code where each API endpoint became an MCP tool in one huge file; it worked well as a carefully curated demo, which showed him nothing.

The real test came when the whole team got access and it immediately broke. Given an incomplete description from a client conversation or a Notion page, the agent would build the entire workflow start to finish and confidently assure the user it had done everything.

- Agent-based software is an architectural problem centered on who pays for an agent's mistake, with three models: auto mode (autonomy), user priority (control), and the customer-service-agent experience (structured capability plus human verification).
- Reducto's MCP MVP mapped each API endpoint to an MCP tool in one huge file; it succeeded as a curated demo but revealed nothing about real usage.
- The MCP server broke once the whole team used it: incomplete descriptions from client conversations or Notion pages led the agent to build entire workflows and confidently claim completion.
- Reducto processes over 3 billion documents and positions itself as the layer between models and messy, unstructured corporate data where hallucination occurs.