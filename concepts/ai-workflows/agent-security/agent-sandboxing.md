---
domain: ai-workflows
subdomain: agent-security
concept: agent-sandboxing
title: Breaking Claude Code Opus 5 Auto Mode
sources:
  - title: "Breaking Claude Code Opus 5 Auto Mode"
    url: "https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/"
    date: "2026-08-27T22:50:25+00:00"
---

# Breaking Claude Code Opus 5 Auto Mode

Johann Rehberger, a credible prompt injection researcher, discovered an attack against Claude Code's auto mode that succeeds roughly 80% of the time. The attack tricks Claude Code into downloading and unpacking a zip archive, then executing code that imports base64 without noticing that a local struct.py file from the archive will be imported and executed instead. This demonstrates the ongoing risk of prompt injection in AI agents that interact with untrusted content (Simon Willison, https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/).

- A prompt injection attack against Claude Code auto mode succeeded 80% of the time by exploiting Python's import behavior via a zip archive.
- Auto mode sometimes blocked the agent's own cleanup attempts, turning the safety mechanism into a liability.
- The only safe way to run unattended agents under adversarial risk is strict sandboxing: containers, VMs, or OS sandboxes.
- Sandboxing must also restrict network egress, limit exposed credentials and home directories, and include monitoring.