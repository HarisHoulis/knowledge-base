---
domain: ai-workflows
subdomain: agent-sandbox-architecture
concept: cloud-hosted-agent-sandboxes
title: Cowork Moves Model Inference and Its VM to the Cloud
sources:
  - title: "Quoting Felix Rieseberg"
    url: "https://simonwillison.net/2026/Oct/5/felix-rieseberg/"
    author: "Simon Willison"
    date: "2026-10-05"
  - title: "Felix Rieseberg on X"
    url: "https://twitter.com/felixrieseberg/status/2107206431376334975"
    author: "Felix Rieseberg"
  - title: "Use Claude Cowork on web, desktop, and mobile"
    url: "https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile#h_f951c27c48"
    author: "Anthropic"
---

# Cowork Moves Model Inference and Its VM to the Cloud

Felix Rieseberg (Anthropic) describes an architectural shift in Cowork: the "old" version ran model inference in the cloud but executed tool calls in an Anthropic-provided VM shipped to the user's computer. That VM existed for capability, safety, and security reasons, mapping in only the data a user explicitly added to the session. Users liked what they could do with Claude but disliked the disk, battery, and performance cost of a local VM, and disliked that closing the laptop stopped the work.

The "new" version runs both model inference and the VM in the cloud. Each session gets its own sandbox and does not share state with other sessions. When the VM needs something on the user's device, such as a file, the desktop app is responsible for that file-access tool call.

Rieseberg frames this as solving several reported problems: using Cowork from a phone, keeping work running, and getting the same power without losing battery to the VM.

- Old Cowork: cloud inference + local Anthropic-provided VM executing tool calls, with only explicitly added session data mapped in.
- Motivation for change: local VM cost users disk, battery, and performance, and work stopped when the laptop closed.
- New Cowork: model inference and the VM both run in the cloud, with a separate sandbox per session sharing no state.
- Device access is delegated: the desktop app performs file-access tool calls when the cloud VM needs a user's file.
- Claimed benefits: phone usage, persistent work, and full capability without local battery drain.