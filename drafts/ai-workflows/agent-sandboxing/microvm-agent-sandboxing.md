---
domain: ai-workflows
subdomain: agent-sandboxing
concept: microvm-agent-sandboxing
title: YOLO Mode, Safely: MicroVM Sandboxes for Any Agent
sources:
  - title: "YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker"
    url: "https://www.youtube.com/watch?v=OE_lLNCNfQo"
    author: "Rowan Christmas"
    date: "2026-10-03"
---

# YOLO Mode, Safely: MicroVM Sandboxes for Any Agent

Rowan Christmas, a Docker product manager, demonstrates that a normal desktop AI agent session cannot be trusted with sensitive local data. Running Claude Code on his Mac, he asked it to locate his browser history and then his bank accounts; within about five requests it surfaced real bank details, the last four digits of an active account, and evidence of a recent check order and Zelle usage (AI Engineer, 2026). A direct request for bank details triggers a warning, but reframing the task as "researching security issues" was enough to get cooperation. His security team flagged the activity as a possible compromise, and the resulting CrowdStrike report confirmed this is a known technique for obtaining credentials from a machine.

His conclusion is that prompt-level guardrails — the "please don't do anything bad" school of safety — are inadequate, especially since access obtained through a script or MCP server could have been worse than self-inflicted (AI Engineer, 2026). The proposed alternative is isolation rather than persuasion: Docker's new SBX binary, a microVM that runs its own kernel and isolates the file system instead of sharing the host's as a container would (AI Engineer, 2026).

In the SBX model the sandbox never sees your secrets; network requests carry a placeholder that is substituted outside the sandbox, so the agent cannot leak or misuse what it holds, and a complete audit trail is kept (AI Engineer, 2026). Practically, running `sbx run claude` creates a new VM, deploys it to a folder, creates a sandbox, and launches the agent inside it — with permission bypass enabled — while the same browser-history or bank-account attack inside the sandbox fails, because the agent cannot see anything on the host (AI Engineer, 2026).

Christmas frames the tradeoff explicitly: without granting agents this kind of capability they are useless, so the goal is confident safety from the start rather than hoping for the best (AI Engineer, 2026).

- A stock desktop agent session (Claude Code on macOS) exposed the speaker's real browser history, bank account details, last four digits, and recent check/Zelle activity in roughly five requests, and it was flagged by his security team and identified in a CrowdStrike report as a known credential-harvesting technique.
- Prompt-level refusals are weak: asking directly for bank details warns, but framing the same request as security research is enough to proceed.
- MicroVMs (Docker's SBX binary) differ from containers by running their own kernel and isolating the file system, so the sandbox never sees host secrets.
- Network requests in the sandbox use placeholders that are substituted outside it, giving a complete audit trail and preventing the agent from acting on real credentials.
- `sbx run claude` creates a VM, deploys it to a folder, spins up a sandbox, and launches the agent — the same attacks that work in a normal session fail inside the sandbox.