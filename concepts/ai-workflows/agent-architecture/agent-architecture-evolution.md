---
domain: ai-workflows
subdomain: agent-architecture
concept: agent-architecture-evolution
title: We Kept Rebuilding Our AI Agent: Lessons from Two Years of Alex at Arize AI
sources:
  - title: "We Kept Rebuilding Our AI Agent. Here's What Survived - Fuad Ali, Arize AI"
    url: "https://www.youtube.com/watch?v=YIhvrvHtonk"
    author: "AI Engineer"
    date: "2026-10-27"
---

# We Kept Rebuilding Our AI Agent: Lessons from Two Years of Alex at Arize AI

Fuad Ali, an AI product manager at Arize AI, recounts two years of building and repeatedly rebuilding Alex, an internal product agent that reads traces, converts results into tests, datasets, and experiments, plans multi-step work, and generates synthetic data. The first prototype in late 2023, built on GPT-3.5-era models, was roughly 50% hallucinations and 50% useful; the agent has since evolved into a deeper planning flow with a clearer interface that explains what it does. Arize also runs agents on agents: Signal reads the traces of other agents, and Alex is used to debug Alex itself.

- Early agent prototypes on GPT-3.5-era models were about 50% hallucinations; reliability improved as models improved and the architecture matured.
- Arize moved math out of the model into binding code, then evolved from a skill-set router/decision tree to an iterative tool-call loop with a to-do list for self-planning.
- Alex 2.0 (Feb 2026) rebooted with Sonnet 4.5 as default; the June release merged specialized agents into one skill-loading agent and added long-term memory.
- Agents monitor agents: Signal reads traces to find retry loops and issues in Alex, and Alex is used to debug Alex.
- Human judgment remains essential—trace-reading agents surface problems but humans still participate in evaluation and decisions.