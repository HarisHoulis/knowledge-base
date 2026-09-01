---
domain: ai-workflows
subdomain: agent-security
concept: sandboxed-agent-runtime
title: Breaking Claude Code Opus 5 Auto Mode
sources:
  - title: "Breaking Claude Code Opus 5 Auto Mode"
    url: "https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/"
    author: "Simon Willison"
    date: "2026-08-27T22:50:25+00:00"
  - title: "Breaking Claude Code Opus 5 and Auto Mode"
    url: "https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/"
    author: "Johann Rehberger"
    date: "2026"
---

# Breaking Claude Code Opus 5 Auto Mode

Johann Rehberger, a prominent prompt injection researcher, discovered an attack against Claude Code's auto mode that reportedly works 80% of the time. The exploit tricks the agent into downloading and extracting a zip archive that contains a malicious `struct.py` file, then induces it to execute code importing `base64`, which inadvertently loads the local `struct.py` from the archive. This is characterized as a confused environment attack rather than classic prompt injection, because the agent is not following instructions from an external website but rather misidentifying the local file as a trusted library ([Simon Willison, 2026](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/)).

A striking detail is that auto mode sometimes prevented the agent from stopping the malware. In several runs, once Claude detected the compromise and tried to terminate the malicious process, the auto mode classifier blocked the cleanup command. This illustrates a fundamental safety concern: the safety mechanism itself can be exploited, as it allowed the malware process to be created but blocked the command designed to kill it. The author agrees with Rehberger's conclusion that the only safe way to run agents under adversarial conditions is to use a sandbox. Recommended measures include running unattended agents in containers, VMs, or OS-level sandboxes, restricting network egress, monitoring agent activity, and never exposing home directories, SSH keys, or cloud credentials to the agent runtime ([Simon Willison, 2026](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/)).

- Attack exploits confused environment, tricking Claude Code into executing a malicious local `struct.py` after extracting an archive, with an 80% success rate.
- Auto mode can block the agent's own cleanup commands, turning the safety classifier into a vector that allows the malware to continue running.
- The incident is not classic prompt injection because no external instructions are accidentally followed; it's a confused environment attack due to untrusted files in the working directory.
- Recommendation: always run coding agents in sandboxed containers/VMs, restrict network egress, monitor activity, and avoid exposing sensitive credentials or home directories.