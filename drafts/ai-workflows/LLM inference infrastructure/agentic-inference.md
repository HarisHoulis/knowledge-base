---
domain: ai-workflows
subdomain: LLM inference infrastructure
concept: agentic-inference
title: The Frontier AI Inference Cloud for Agents
sources:
  - title: "The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI"
    url: "https://www.youtube.com/watch?v=Hvb2LfMH58c"
    author: "Byung-Gon (Gon) Chun (AI Engineer)"
    date: "2026-09-19"
---

# The Frontier AI Inference Cloud for Agents

Byung-Gon (Gon) Chun, founder and CEO of FriendliAI, argues that agentic workloads are a fundamentally different inference problem than chat (Chun, FriendliAI talk). In chat, the unit of work is a single request and latency means how fast one response returns; in agents, the unit is a task made of many model calls and tool calls running in a loop — plan, act, observe, repeat — potentially with parallel sub-agents. Users therefore do not care about the latency of an individual request, only when the whole task completes, so the optimization target becomes end-to-end task latency rather than per-request latency.

The speaker traces this shift to two converging trends: agents spreading across software operations and knowledge work, and open-weight models reaching frontier quality, which makes frontier-quality agents economically viable at much lower token cost. He illustrates with the same coding task (building a tower defense game) run by an agent against GLM 5.2 on FriendliAI versus Anthropic's Opus 4.8: both produced usable results for many agentic workflows, but the claimed cost was $150 for Opus 4.8 versus 27 cents for GLM 5.2 on FriendliAI (described in the talk as about 5.6x cheaper).

Agent inputs are also structurally different from chat. Prompt and completion lengths are much longer and grow as the task progresses, because every observation is appended back into the context. Consecutive agent steps share a huge prefix, so recomputing that prefix every time burns compute on work already done — Chun calls prefix reuse one of the biggest opportunities in agentic inference. Long-horizon tasks such as deep research may run tens or hundreds of inference steps over minutes or hours while the shared context keeps growing.

Because context grows over time, work is interleaved between model calls, and the number of model calls depends on the input, the workload cannot be planned around a fixed request rate. FriendliAI positions itself as a frontier inference cloud rebuilt specifically for these agentic workloads, and notes its research roots — the team invented continuous batching, now standard across the industry, and its Orca work inspired a widely used open-source framework.

- Agentic workloads shift the unit of work from a single request to a multi-step task, so the metric that matters is end-to-end task latency, not single-request latency.
- Agent steps share large context prefixes that grow over time; recomputing them wastes compute, making prefix reuse a major optimization opportunity.
- Open-weight models have crossed the quality threshold for real agentic workflows and can run frontier-quality agents at a fraction of closed-model token cost.
- Agent traffic is unpredictable — model call count depends on input and work interleaves with tool calls — so fixed request-rate planning does not apply.
- FriendliAI claims research heritage in inference optimization: continuous batching originated with the team, and its Orca work inspired a widely used open-source framework.