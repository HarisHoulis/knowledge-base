---
domain: ai-workflows
subdomain: agent-runtime
concept: event-driven-agents
title: Agent Frameworks Considered Harmful: Building a Custom Agent Runtime
sources:
  - title: "Agent Frameworks Considered Harmful — Rémi Louf, .txt"
    url: "https://www.youtube.com/watch?v=KHudyx5wW3U"
    author: "AI Engineer"
    date: "2026-08-22T16:30:39+00:00"
---

# Agent Frameworks Considered Harmful: Building a Custom Agent Runtime

Rémi Louf describes his journey building a custom agent runtime after experiencing failures with existing agent frameworks. In the first week, his daily brief posted to Slack twice, a voice note vanished, and a market brief turned to garbage due to unversioned prompt edits. These failures motivated him to design a runtime with three key components: an append-only log where nothing is discarded and events are causally linked, a queue that counts attempts to handle duplicates, and a content-addressed store for prompts (Louf, 2026).

The content-addressed store hashes every part of a prompt separately—system message, skill descriptions, tool definitions, user question—so a prompt becomes a list of hashes rather than a rendered string. This enables diffs between runs and exact replays against different models, addressing the problem that live chat sessions with compaction and unshared reasoning hide what the model actually saw (Louf, 2026).

Agents are intentionally kept simple: they are markdown files dropped into a folder, allowing non-coders to add agents. They subscribe to events instead of living in a graph with edges to maintain. Typed tool calls and typed events serve as the two boundaries, because roughly 20% of his events were malformed and rejected before typing was enforced. Louf took two weeks away from his 15-person company to build it, and twenty agents now run there (Louf, 2026).

- Existing agent frameworks fail in production: duplicated posts, lost voice notes, and untraceable prompt edits.
- An append-only log with causal linking ensures no event is lost and every action is traceable.
- Content-addressing prompts enables diffing and replaying exactly what the model saw.
- Agents as markdown files lower the barrier for non-coders to create agents.
- Typed tool calls and events are critical boundaries; untyped events caused ~20% malformed data.