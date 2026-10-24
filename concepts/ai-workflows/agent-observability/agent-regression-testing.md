---
domain: ai-workflows
subdomain: agent-observability
concept: agent-regression-testing
title: Your Agent Fix Just Broke Something Else: Building Regression Loops for AI Agents
sources:
  - title: "Your Agent Fix Just Broke Something Else - Sofia Jakovcevic, Arize AI"
    url: "https://www.youtube.com/watch?v=v5tm5EAzsAs"
    author: "AI Engineer"
    date: "2026-10-24"
---

# Your Agent Fix Just Broke Something Else: Building Regression Loops for AI Agents

Sofia Jakovcevic of Arize AI argues that AI agents are hard to debug because much of their logic lives in an opaque "black box" of natural-language instructions rather than explicit low-level code. Observability is the remedy: it illuminates what the system actually does step by step, enabling evaluation metrics that track performance and drive gradual improvement. But she stresses that the harder problem is not identifying what's broken—it's ensuring a fix doesn't break ten other things.

Her central example: a security engineer adds a single line requiring the support agent to confirm before performing any action. A week later, evaluation on production data shows a 17-point improvement in safety—but task completion drops by 17 points, because agents waiting for confirmation leave tasks incomplete when users abandon sessions. The average of both metrics is zero, illustrating that improving one aspect of agent performance does not mean improving overall performance.

The root cause is a flawed assumption: that errors occur at the code level. In reality, agents fail at runtime. A one-line prompt change is local and easy to approve, but it alters execution—adding steps, changing how agents interact with subagents, and changing how tools are called across many possible trajectories. Jakovcevic therefore advocates programming based on numerical evaluation data rather than "by feel," and building a five-step regression loop that is automated and integrated into CI/CD rather than left to individual engineers.

- Agents fail at runtime, not at the code level, so code review alone cannot catch behavioral regressions.
- A one-line prompt change can improve one metric (safety +17) while degrading another (task completion -17), netting zero overall.
- Observability turns the agent's black box into step-by-step traces that can be evaluated with metrics.
- Regression testing should be an automated process integrated into CI/CD, not an ad hoc engineering task.
- Changes should be justified by numerical evaluation data rather than intuition or 'programming by feel'.