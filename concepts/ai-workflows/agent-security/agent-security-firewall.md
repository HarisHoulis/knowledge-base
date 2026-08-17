---
domain: ai-workflows
subdomain: agent-security
concept: agent-security-firewall
title: Security Firewall for Agents — Ryan Dahl, Deno
sources:
  - title: "Security Firewall for Agents — Ryan Dahl, Deno"
    url: "https://www.youtube.com/watch?v=MkRYPFIMCSA"
    author: "AI Engineer"
    date: "2026-08-17T18:30:06+00:00"
---

# Security Firewall for Agents — Ryan Dahl, Deno

In this talk, Ryan Dahl describes how Deno Deploy uses AI agents, such as OpenClaw, to automatically service on-call incidents. These agents are given broad read/write access to production systems including Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack, allowing them to gather full context and resolve issues that previously required human intervention. Dahl emphasizes that this is powerful but dangerous, because agents connected to external support systems are susceptible to prompt injection and could take destructive actions like dropping a user table.

- Treat agents as untrusted software; never rely on model alignment for security.
- Isolate agents at the VM level and focus security on outbound network traffic.
- Dangerous actions often use non-HTTP protocols (e.g., psql) invoked via subprocesses, so firewalls must understand protocol semantics, not just ports.
- Fine-grained credentials and ACLs are helpful but insufficient due to composite access paths across systems like EKS.
- A security firewall should allow human-like workflows while preventing destructive actions like dropping tables.