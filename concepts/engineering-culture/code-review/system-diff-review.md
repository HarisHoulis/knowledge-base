---
domain: engineering-culture
subdomain: code-review
concept: system-diff-review
title: Stop Reviewing Diffs. Start Reviewing Systems.
sources:
  - title: "Stop Reviewing Diffs. Start Reviewing Systems."
    url: "https://www.youtube.com/watch?v=Xs-U7SY2uNE"
    author: "Kent C. Dodds"
    date: "2026-07-28T13:57:05+00:00"
---

# Stop Reviewing Diffs. Start Reviewing Systems.

Kent C. Dodds argues that code review should shift from line-by-line diff inspection to system-level review. He notes that the appropriate level of review lies on a spectrum depending on project importance and risk, but the trend is moving toward system-level understanding. He references Steve from builder.io who built a skill that generates a 'system diff' or visual change of the system at large, and Kent built his own version where the agent that did the work also generates a 'system recap' [1].

Kent's system recap classifies risk based on whether primitives are added or removed, provides a system map, and describes the change flow. He used it to review a 3,000-line change adding MCP support to Cody, which helped him understand the agent's interpretation of his prompt and the overall user experience without reading every line. He still uses AI code reviewers for code-level issues, but the system-level perspective lets him guide the bot and catch weird decisions more effectively [1].

- Reviewing code on a spectrum: line-by-line diffs are not always necessary; system-level review is increasingly valuable.
- System recaps classify risk by primitives touched (added/removed) and provide a system map and change flow.
- A system-level view helps reviewers understand large changes (e.g., 3,000 lines) and the agent's reasoning.
- AI code reviewers are still useful, but system-level review offers a higher-level understanding to guide development.
- The approach was inspired by Steve at builder.io and implemented by Kent for his own workflow.