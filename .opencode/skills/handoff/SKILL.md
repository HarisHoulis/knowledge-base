---
name: handoff
description: Compact the current conversation into a handoff document when context nears capacity. Saves to `.handoffs/<issue-num>-<timestamp>.md` inside the repo so the file can be committed and pushed to the branch for headless CI resumption.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

Determine the current issue number from context (e.g., `#57`). Save to `.handoffs/<issue-num>-<timestamp>.md` where `<timestamp>` is `YYYY-MM-DD-HHMMSS`.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
