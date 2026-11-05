---
domain: ai-workflows
subdomain: coding-agents
concept: resumable-agent-orchestration
title: Inkitt Builds a One-Shot PR Creator with Resumable Agent Orchestration
sources:
  - title: "Inkitt Builds a One-Shot PR Creator with Resumable Agent Orchestration"
    url: "https://www.infoq.com/news/2026/11/inkitt-one-shot-pr-creator-agent/"
    author: "Leela Kumili"
    date: "2026-11-04"
---

# Inkitt Builds a One-Shot PR Creator with Resumable Agent Orchestration

Inkitt developed a one-shot pull request creator that automates small, low-risk code changes, taking a task from intake all the way to draft PR creation. The system is built around an event-driven orchestrator that persists workflow state, so long-running agent workflows can resume rather than restart from scratch.

The orchestrator coordinates short-lived coding agent containers, bounding retries and enforcing permission restrictions on what the agents can do. Despite the automation, human review and approval remain mandatory before any change can be merged, keeping a human in the loop for the final decision.

This design combines durable workflow state with ephemeral agent execution, limiting the blast radius of each agent run while keeping the overall process resilient to failures.

- Event-driven orchestrator persists workflow state to enable resumable agent runs.
- Coding agents run in short-lived containers with bounded retries and permission restrictions.
- Automation covers small, low-risk changes from task intake to draft PR creation.
- Human review and approval are still required before merging.