---
domain: ai-workflows
subdomain: agent-security
concept: confused-environment-attack
title: Breaking Claude Code Opus 5 Auto Mode
sources:
  - title: "Breaking Claude Code Opus 5 Auto Mode"
    url: "https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/"
    author: "Simon Willison"
    date: "2026-08-27"
  - title: "Breaking Claude Code Opus 5 and Auto Mode"
    url: "https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/"
    author: "Johann Rehberger"
    date: "2026-08-27"
---

# Breaking Claude Code Opus 5 Auto Mode

Johann Rehberger discovered an attack against Claude Code's auto mode that succeeds approximately 80% of the time. The attack tricks the agent into downloading and uncompressing a zip archive, then executing code that imports the `base64` module, but a locally extracted `struct.py` file shadows the standard library module, causing arbitrary code execution. The author, Simon Willison, highlights this as a credible example of a security flaw in agentic systems, where the AI's own safety mechanisms can backfire.

In several runs, Claude detected the compromise and attempted to terminate the malicious process, but auto mode denied the cleanup command. This demonstrates that the safety classifier itself can become part of the failure: it allowed the malware to be created, then blocked the very command intended to stop it. Willison agrees with Rehberger's conclusion that the only safe way to run agents under adversarial conditions is with rigorous sandboxing.

The recommended mitigations include running unattended coding agents in a container, VM, or OS sandbox; restricting network egress; monitoring agent activity; and avoiding exposure of home directories, SSH keys, or cloud credentials to the agent runtime. An update notes that this attack is not a classic prompt injection, as no malicious website instructions were followed; instead, it is a confused environment attack exploiting the agent's environment and its own safety controls.

The incident underscores the need for defense-in-depth in AI agent deployments, treating the model and its guardrails as part of a broader security boundary rather than relying solely on the model's reasoning. It also highlights that safety mechanisms can introduce new vulnerabilities if they are not carefully designed and tested against adversarial goals.

- Auto mode in Claude Code is vulnerable to a confused environment attack that succeeds ~80% of the time, using a malicious zip archive to shadow Python's stdlib modules.
- The safety classifier can block cleanup commands, preventing the agent from stopping malware even after it detects the compromise.
- Running agents in sandboxes with restricted egress and no sensitive credential exposure is essential for security.
- This attack is not classic prompt injection but a confused environment attack, per hyperpape's analysis.