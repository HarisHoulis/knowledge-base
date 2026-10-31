---
domain: ai-workflows
subdomain: self-hosted-inference
concept: owning-ai-inference-stack
title: When Running Your Own AI Models Beats Paying for APIs
sources:
  - title: "When Running Your Own AI Models Beats Paying for APIs - Steven Latré, imec"
    url: "https://www.youtube.com/watch?v=9-Y_oS9OBLc"
    author: "AI Engineer"
    date: "2026-10-31"
---

# When Running Your Own AI Models Beats Paying for APIs

Steven Latré, who heads the AI department at imec, describes a maturity path organizations move through when adopting AI. Early on, teams chase the latest and greatest models and pay per subscription or token; then they shift to model routing, picking the best model for each task. Model routing, he argues, is only the first low-hanging fruit of optimization, and as token consumption grows there is a need to take control of your own stack.

He frames this as a progression from closed APIs, to cost optimization, to hosting open-scale models and leasing or buying your own infrastructure. The first phase only requires choosing a model suited to a task's accuracy or complexity; once you own infrastructure, the design space expands rapidly to model choice and trust, testing tools, hardware architecture, CPU/GPU balance, and KV cache optimization.

To quantify the tradeoff, imec ran thousands of launches comparing API use against their own infrastructure, focused on agentic AI and long-term tasks, which they see as the number one reason to own your AI stack. They used SWE-bench coding tasks and varied coding environments such as Codex and Claude Code along with different model types.

The core shift is from paying for tokens to understanding the full cost of ownership, including how to configure infrastructure, which inference engine to choose, and what equipment is needed.

- Organizations progress from closed APIs, to cost optimization, to hosting open-scale models and owning infrastructure
- Model routing is only the first optimization step; growing token consumption pushes teams to control their own stack
- Owning infrastructure expands the design space to hardware, CPU/GPU balance, KV cache, and inference engine choice
- Long-term agentic tasks are the strongest case for self-hosting; interactive workloads may have different economics
- The shift is from paying per token to understanding full cost of ownership