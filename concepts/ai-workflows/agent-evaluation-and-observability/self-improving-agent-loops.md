---
domain: ai-workflows
subdomain: agent-evaluation-and-observability
concept: self-improving-agent-loops
title: The Self-Improving OSS Agent Stack
sources:
  - title: "The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse"
    url: "https://www.youtube.com/watch?v=TeErpYBUIeM"
    author: "AI Engineer"
    date: "2026-10-06"
---

# The Self-Improving OSS Agent Stack

Marc Klingen, co-founder of Langfuse, describes how teams building agent applications are moving from manually running the agent improvement cycle to having AI automate parts of it. The core cycle he describes is: observe how users actually use the agent in production, turn those traces into datasets, run offline experiments and evaluations, deploy changes to production, then learn again from real user experiences [source]. Langfuse was created because these online and offline halves need to be combined — observational tooling (like DataDog) and ML-ops tooling (like MLflow or Weights & Biases) traditionally lived apart, leaving either datasets out of sync with production or production monitoring without offline testing [source].

The problem is that running this cycle manually is exhausting: reviewing traces, updating datasets, inventing new evaluators, forming hypotheses, and shipping changes is a lot of manual work. Klingen notes that teams have long asked how to get out of this process and automate it, and that improving models are what make such automation feasible [source]. He frames progress as a stack of nested loops: at the lowest level a token cycle, at the highest the abstract thinking where a human is still involved, with GitHub Copilot-era assistance occupying a low level around 2023, a third level becoming possible around 2024, and 2025–2026 moving to higher levels where agents themselves decide what to fix, propose solutions, and test whether they work [source].

Humans remain in the loop at two points: reviewing exactly what gets added to the dataset, and evaluating whether the agent is actually working properly [source]. Klingen flags risks in letting agents suggest and apply fixes — you still want to see what changed because of the risk of overtraining the agent on the dataset, and agents often surface failure patterns that fall outside what the agent is supposed to do at all, so those need monitoring rather than automatic adjustment [source]. He also notes the broader shift in how teams talk about the work, from "I don't write prompts" to "I have cycles," with automated research becoming popular [source].

- The agent improvement cycle combines online production observability with offline dataset building, experimentation, and evaluation — Langfuse exists to unify these two halves rather than leaving them in separate tools [source].
- Running this cycle manually is labor-intensive (reviewing traces, updating datasets, creating evaluators), which drives interest in letting agents automate parts of it [source].
- Improving models enable progressively higher-level loops: from token-level prediction and Copilot-style assistance toward agents that decide what to fix, propose solutions, and test them [source].
- Humans stay in the loop for two decisions: what gets added to the dataset, and whether the agent is working properly [source].
- Agent-proposed fixes carry risks of overtraining on the dataset, and agents may surface failure patterns that are out of scope for the use case and should be monitored rather than fixed [source].