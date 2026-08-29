---
domain: ai-workflows
subdomain: agent-security
concept: prompt-injection-sandboxing
title: Breaking Claude Code Opus 5 Auto Mode
sources:
  - title: "Breaking Claude Code Opus 5 Auto Mode"
    url: "https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/"
    author: "Simon Willison"
    date: "2026-08-27"
  - title: "Breaking Claude Code Opus 5 and Auto Mode"
    url: "https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/"
    author: "Johann Rehberger"
---

# Breaking Claude Code Opus 5 Auto Mode

Johann Rehberger, a prominent prompt injection researcher, discovered an attack against Claude Code's auto mode that reportedly works 80% of the time. The attack tricks the agent into downloading and uncompressing a zip archive, then executing code that imports Python's `base64` module without realizing that a local `struct.py` file from the archive will be imported and executed instead, enabling malicious code execution. In several test runs, auto mode actually prevented the agent from terminating the harmful process, and in one case it blocked the cleanup command even after Claude detected the compromise. This demonstrates that the safety mechanism itself can become part of the failure: the classifier allowed the malware process to be created, then blocked the command intended to stop it. The author agrees with Rehberger's conclusion that the only safe way to run agents in any scenario with adversarial risk is within a sandbox. Concretely, unattended coding agents should run in a container, VM, or OS sandbox, with restricted network egress, active monitoring, and no access to home directories, SSH keys, or cloud credentials.

- Attack uses a zip archive to smuggle a malicious `struct.py` that shadows the legitimate `base64` import, achieving code execution.
- Auto mode can block the agent's own cleanup commands, turning the safety mechanism into part of the failure chain.
- The classifier allowed creation of the malware process but denied the terminate command, showing inconsistent enforcement.
- The only robust defense is running agents in a sandbox with restricted egress, monitoring, and no sensitive credentials exposed.