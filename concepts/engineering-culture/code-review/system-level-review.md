---
domain: engineering-culture
subdomain: code-review
concept: system-level-review
title: Stop Reviewing Diffs. Start Reviewing Systems.
sources:
  - title: "Stop Reviewing Diffs. Start Reviewing Systems."
    url: "https://www.youtube.com/watch?v=Xs-U7SY2uNE"
    author: "Kent C. Dodds"
    date: "2026-07-28T13:57:05+00:00"
---

# Stop Reviewing Diffs. Start Reviewing Systems.

In this talk, Kent C. Dodds argues that code review practices are shifting from line-by-line diff inspection toward a more holistic, system-level review. He notes that the appropriate depth of review exists on a spectrum, depending on project importance and risk, but that AI tools are enabling a new approach: reviewing the system impact of changes rather than just the code (Dodds, 2026).

- Code review is a spectrum; not every change requires deep line-by-line reading.
- AI agents can generate 'system recaps' summarizing risk, touched primitives, and change flow.
- System-level review helps reviewers understand the agent's interpretation of a prompt and guide it effectively.
- Tools like Cursor and builder.io's system diff skill are driving the shift to system-oriented review.