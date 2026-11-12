---
domain: ai-workflows
subdomain: agentic-engineering
concept: agent-written-codebases
title: AWS Emulator: A Rust Project Built by a Swarm of Agents
sources:
  - title: "aws-emulator"
    url: "https://simonwillison.net/2026/Nov/11/aws-emulator/"
    author: "Simon Willison"
    date: "2026-11-11"
---

# AWS Emulator: A Rust Project Built by a Swarm of Agents

Simon Willison notes that AWS's new emulator is written in Rust and was produced by a large swarm of agents, generating 29,684 commits in the project's first three weeks. He points to a guest post by Swaminathan (Swami) Sivasubramanian on Werner Vogels' blog describing how the project came to be and what it means for the engineer's job when agents write the code.

Willison highlights a practical limitation: the emulator currently requires Docker to run on macOS or Windows. He hopes this changes so a single downloadable binary could be used as part of standard test suites in other languages and on other platforms.

- The AWS emulator is written in Rust and was built by a swarm of agents, with 29,684 commits in its first three weeks.
- Sivasubramanian's guest post on Vogels' blog covers the project's origin and the engineer's role when agents write code.
- The emulator currently requires Docker on macOS and Windows, which limits easy use in cross-platform test suites.
- Willison wants a single-binary distribution usable in standard test suites across languages and platforms.