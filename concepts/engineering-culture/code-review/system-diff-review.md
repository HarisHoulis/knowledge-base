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

In this video, Kent C. Dodds argues that traditional line-by-line diff review is becoming less central, and reviewers should instead focus on system-level changes. He acknowledges that the right approach depends on the project's risk and context, but sees a clear trend toward reviewing how the entire system is affected. He references Steve from builder.io, who built a skill that generates a 'system diff' — a visual representation of how a PR changes the system at large, not just the UI or individual components (source: video).

- Code review is a spectrum: how much you read every line depends on the project's importance and risk.
- AI tools can generate system recaps that classify risk based on 'primitives' (e.g., adding/removing a primitive is high risk).
- System recaps include a system map and change flow, showing how the user experience is affected and what the agent was thinking.
- Reviewing systems instead of diffs helps humans guide AI agents more effectively when they make questionable decisions.
- While you could manually derive the same insights from files changed, system recaps make the review faster and more comprehensible.