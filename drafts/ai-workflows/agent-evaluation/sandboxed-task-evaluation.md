---
domain: ai-workflows
subdomain: agent-evaluation
concept: sandboxed-task-evaluation
title: Testing Agents on Real Tasks with Harbor
sources:
  - title: "How to Test Your Agents on Real Tasks With Harbor - Xander Song, Arize AI"
    url: "https://www.youtube.com/watch?v=kRJjSOYqW0I"
    author: "AI Engineer"
    date: "2026-10-26"
---

# Testing Agents on Real Tasks with Harbor

Harbor is an open source framework from Arize AI for evaluating agents on real tasks with real data in isolated sandboxes, presented by engineer Xander Song. The core premise is releasing products based on evidence rather than intuition: define realistic tasks, run your agent against them, and get a signal about whether a change improved or regressed behavior.

Each task consists of natural-language instructions in a markdown file plus an environment (typically a Dockerfile) containing task-relevant data such as SQLite files or a git repository at a specific commit. Harbor is agnostic about the data provided. Each task also defines verifiers—scripts that run in the environment after the agent finishes and check whether the expected side effects occurred, producing rewards (e.g., binary pass/fail) written to a reward file.

Tasks are collected into datasets, and Harbor runs a configurable number of attempts per task to account for the stochasticity of LLMs and agents. Each attempt spins up a fresh Docker container with the task data, places the agent inside with the instruction file, lets it act (e.g., modifying source files or databases), then launches verifiers. Because tasks and verifiers stay fixed while the agent implementation changes, running the pipeline end-to-end yields a quick signal of improvement or regression, and many tasks covering a wide range of capabilities close the iteration loop with more confidence than intuition alone.

An optional feature lets agents emit trajectories in ATIF (Agent Trajectory Exchange Format), Harbor's JSON-based trace specification for inspecting the internal steps of an agent's run.

- Harbor defines tasks as markdown instructions plus a Dockerized environment with real data (SQLite, git repos) and task-specific verifier scripts that check for expected side effects.
- Verifiers produce rewards (e.g., binary pass/fail) written to a reward file; keeping tasks and verifiers fixed while swapping agent implementations isolates the effect of changes.
- Datasets of many tasks with configurable attempts per task account for LLM/agent stochasticity, each attempt running in a fresh Docker container.
- Optional ATIF-format trajectories provide JSON traces of an agent's internal steps for inspection.