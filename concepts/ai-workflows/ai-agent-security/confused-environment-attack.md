---
domain: ai-workflows
subdomain: ai-agent-security
concept: confused-environment-attack
title: Breaking Claude Code Opus 5 Auto Mode
sources:
  - title: "Breaking Claude Code Opus 5 Auto Mode"
    url: "https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/"
    author: "Simon Willison"
    date: "2026-08-27T22:50:25+00:00"
---

# Breaking Claude Code Opus 5 Auto Mode

Johann Rehberger discovered an attack against Claude Code's auto mode that succeeds about 80% of the time by tricking the agent into downloading and extracting a zip archive, then executing code that imports base64 but inadvertently loads a malicious local struct.py from the archive. In several runs, once Claude detected the compromise and tried to terminate the malware, auto mode denied the cleanup command, meaning the safety classifier itself became part of the failure. Simon Willison agrees with Rehberger's conclusion that the only safe way to run agents against adversarial inputs is with a sandbox: use containers or VMs, restrict network egress, monitor agent behavior, and avoid exposing home directories, SSH keys, or cloud credentials. In a later update, Willison notes that this is not a classic prompt injection attack because no malicious instructions from a website are followed; rather, it is a confused environment attack where the agent's environment leads to an exploit.

- Attack exploits agent's environment: tricking Claude Code into extracting a zip that shadows a standard library module (struct.py) leads to code execution.
- Auto mode's safety classifier can block the agent's own cleanup commands, making the safety mechanism part of the failure.
- Recommended mitigations: sandbox agents in containers/VMs, restrict network egress, monitor actions, and don't expose sensitive credentials to the agent runtime.
- This attack is better classified as a confused environment attack, not a classic prompt injection, because no external instruction is directly followed.