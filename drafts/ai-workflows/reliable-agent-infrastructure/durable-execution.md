---
domain: ai-workflows
subdomain: reliable-agent-infrastructure
concept: durable-execution
title: Every Step You Take, Every Call You Make: The Reliable Agent Stack
sources:
  - title: "Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate"
    url: "https://www.youtube.com/watch?v=cI7zfqusmFU"
    author: "AI Engineer"
    date: "2026-09-14T15:30:30+00:00"
---

# Every Step You Take, Every Call You Make: The Reliable Agent Stack

Giselle van Dongen (Restate) argues that running agents in production requires an infrastructure layer beyond the LLM itself, framing the evolution of LLM interaction in three waves: an LLM used like a website you query, then agents as downloadable apps with tools, and finally agents as persistent, asynchronous, long-running entities in your infrastructure with access to tools, other agents, and organizational context ("Every step you take, every call you make"). As use cases move from single agents to agentic platforms connecting parts of an organization, the infrastructure layer must evolve with them.

She notes that most innovation so far has focused on agent SDKs and memory: SDKs are good for quick prototypes but do not address connecting distributed components across an organization. Complex agentic systems also require deploying extra infrastructure and writing retry and recovery logic, which is complex to get right but necessary for long-running, stateful, distributed processes in production.

Restate is presented as an open-source framework — a flexible durable foundation for building any backend, including agents — with ideas drawn from Apache Flink and from architects behind Meta-scale event infrastructure. It has four ingredients: durable execution (a crashed agent resumes exactly where it failed rather than starting over), running thousands of concurrent agent sessions in parallel with consistent state and no interference, communication between agents, MCP servers and other tools, and control (the ability to cancel or kill an execution that is stuck or doing something unwanted).

Architecturally, Restate runs as a server in front of your agent service, similar to a message broker or proxy: it proxies each request to the service, opens a connection that acts as a lifeline, and the agent sends events over that connection which Restate journals and uses to recover the process after a failure. This effectively turns a normal function into a long-running, durable, stateful one without the otherwise-required complexity. The talk is mainly a demo of a Slack-connected research agent, with the Restate UI acting as a cockpit showing a registry of registered agents and currently executing invocations (transcript ends mid-sentence).

- LLM usage is evolving from website-like Q&A to tool-using agents to persistent, asynchronous, long-running agents embedded in organizational infrastructure.
- Agent SDKs help you start fast but don't solve the distributed infrastructure problems — retries, recovery, and stateful long-running processes — needed for complex agentic systems.
- Restate is an open-source durable foundation (inspired by Apache Flink and Meta-scale event infrastructure) built on four ingredients: durable execution, concurrent session isolation, inter-agent/tool communication, and execution control.
- Restate runs as a server proxying requests to your agent service, journaling events over a persistent connection so a failed run resumes exactly where it left off.