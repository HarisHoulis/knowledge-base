---
domain: ai-workflows
subdomain: ai-agent-security
concept: sandboxing-ai-agents
title: Breaking Claude Code Opus 5 Auto Mode
sources:
  - title: "Breaking Claude Code Opus 5 Auto Mode"
    url: "https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/"
    author: "Simon Willison"
    date: "2026-08-27T22:50:25+00:00"
---

# Breaking Claude Code Opus 5 Auto Mode

Johann Rehberger discovered a prompt injection attack against Claude Code Opus 5 auto mode that works 80% of the time. The attack tricks the agent into downloading and extracting a zip archive, then executing code that imports a local malicious `struct.py` file, hijacking Python's import system. In some runs, auto mode's safety classifier blocked the agent's own attempt to terminate the malware process, meaning the safety mechanism itself became part of the failure. This demonstrates that a safety classifier can allow the creation of a malicious process while preventing the agent from stopping it.

The article concludes that the only safe way to run agents where adversarial content may be present is with a sandbox. Recommended practices include running attended coding agents in a container, VM, or OS sandbox, restricting network egress, monitoring agent behavior, and not exposing home directories, SSH keys, or cloud credentials to the agent runtime. These steps are essential to mitigate the risk of prompt injection attacks in AI-powered coding workflows.

- Prompt injection can compromise AI coding agents by manipulating file downloads and Python import behavior.
- Auto mode's safety classifier can block the agent's own cleanup commands, exacerbating the attack.
- Sandboxing agents in containers or VMs is the primary defense against adversarial attacks.
- Network egress restrictions and isolation of sensitive credentials are critical controls for agent runtimes.