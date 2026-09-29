---
domain: ai-workflows
subdomain: llm-agents
concept: agents-without-code
title: Agents Without Code: Skills, YAML, and Filesystems Replaced Python
sources:
  - title: "Agents Without Code: Skills, YAML, and Filesystems Replaced Python — Philipp Schmid, Google DeepMind"
    url: "https://www.youtube.com/watch?v=fjF8EKnxKCU"
    author: "AI Engineer"
    date: "2026-09-14"
---

# Agents Without Code: Skills, YAML, and Filesystems Replaced Python

Philipp Schmid (Google DeepMind) opens with Simon Willison's definition of an agent: an LLM that runs tools in a loop until it achieves a goal (AI Engineer, 2026). The talk's premise is to build the same GitHub PR review agent in three different ways, deleting code at each step — "each new version, less code, more files" (AI Engineer, 2026).

A centerpiece is the Gemini Interactions API, described as a unified interface for running models and agents, with a sandbox, server-side state management, and background execution (AI Engineer, 2026). Unlike turn-based chat APIs where a user role is reused to pass environment data back, the Interactions API models a flat steps timeline: user input, reasoning, function call, function result (AI Engineer, 2026).

The first, code-heavy version is a raw Python loop: define a JSON schema, write Python functions, inspect LLM output to distinguish function calls from text, match the call to a tool, handle errors, and append results (AI Engineer, 2026). It works but is limited to explicitly defined tools — if asked for a capability it lacks, the agent simply replies that it cannot do it (AI Engineer, 2026). Schmid notes the many moving parts: token generation, native function calling, loop execution, tool routing, schema creation, Python execution, and state management (AI Engineer, 2026). Agent frameworks such as ADK are introduced as an abstraction over some of that complexity (AI Engineer, 2026).

- An agent is an LLM running tools in a loop until it achieves a goal (Simon Willison's definition).
- The Gemini Interactions API replaces turn-based conversation history with steps: user input, reasoning, function call, function result.
- Raw-Python agents require JSON schemas, tool routing, state management, and manual error handling — and are restricted to predefined tools.
- Agent frameworks like ADK abstract away part of that complexity.
- The talk's structure is three implementations of the same GitHub PR review agent, each with less code and more files.