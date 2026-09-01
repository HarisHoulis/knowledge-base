---
domain: ai-workflows
subdomain: agent-design
concept: information-gain-agents
title: Multimodal Collaborative Agents for Next-Gen Commerce
sources:
  - title: "Multimodal Collaborative Agents for Next-Gen Commerce — Nidhi Kaushik Vyas, Google DeepMind"
    url: "https://www.youtube.com/watch?v=AhQpRalYlyg"
    author: "AI Engineer"
    date: "2026-09-01T17:00:27+00:00"
---

# Multimodal Collaborative Agents for Next-Gen Commerce

In this talk, Nidhi Kaushik Vyas (Google DeepMind) argues that typical shopping agents are wrappers around a search bar, assuming users already have well-formed goals and vocabulary. She introduces the 'articulation gap': users arrive with a vague vibe, and closing that gap is the agent's job, not the user's. The central tactic is choosing the next question by expected information gain—e.g., asking room width before making furniture recommendations—rather than following a fixed checklist.

- Agents should select questions by expected information gain to resolve fuzzy intent efficiently.
- The agent loop consists of discovery (state building), research (choosing how to ask), and response (format selection).
- An autorater grades each stage, including counterfactual checks that flip parts of the query to validate extracted constraints.
- Multimodal inputs like images and visual boards are used for subjective preferences, while real-time inventory variables are flagged for freshness.