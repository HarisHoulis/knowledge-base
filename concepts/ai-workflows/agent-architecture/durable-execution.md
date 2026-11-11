---
domain: ai-workflows
subdomain: agent-architecture
concept: durable-execution
title: Long-horizon agents and durable execution
sources:
  - title: "Long-horizon agents and durable execution"
    url: "https://martinfowler.com/articles/durable-execution-agents.html"
    author: "Martin Fowler"
---

# Long-horizon agents and durable execution

Long-horizon agents automate complex tasks that can take days or weeks, involving multiple exchanges with people and external systems. Over such durations, many things can go wrong, including process crashes, network failures, and unanticipated real-world behavior (martinfowler.com).

Kiran Prakash describes durable execution as an emerging pattern that helps agents recover from these failures and keep moving toward their goal. In this programming model, the runtime records the result of each step that interacts with the outside world. When a failure occurs, the program runs again, completed steps are skipped, and the program's state is rebuilt from that record (martinfowler.com).

- Long-horizon agents run for days or weeks and interact with people and external systems, making failures likely.
- Durable execution records the outcome of each externally interacting step in the runtime.
- On failure, the program re-runs, skips completed steps, and rebuilds state from the recorded results.