---
domain: ai-workflows
subdomain: agent-security
concept: agent-proxy-firewall
title: Security Firewall for Agents — Ryan Dahl, Deno
sources:
  - title: "Security Firewall for Agents — Ryan Dahl, Deno"
    url: "https://www.youtube.com/watch?v=MkRYPFIMCSA"
    author: "AI Engineer"
    date: "2026-08-17T18:30:06+00:00"
---

# Security Firewall for Agents — Ryan Dahl, Deno

In this talk, Ryan Dahl addresses the security challenges of giving AI agents privileged access to production systems. He explains that Deno's incident response agents have read and write access to production Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack, and they now close incidents that previously required human intervention. However, the critical problem is prompt injection through connected support systems. Dahl rejects the idea that security can rely on a model's refusal behavior—even if models like Opus typically refuse destructive actions, they are untrusted software, and the guard cannot live inside the agent itself (Dahl, 2026).

To solve this, Deno built Claw Patrol, an MIT-licensed proxy that sits in front of the agent and parses every byte leaving it below the HTTP layer. This is necessary because the dangerous path often isn't HTTP—an agent can spawn psql as a subprocess and tunnel to a production database through an EKS endpoint, bypassing any MCP tool definitions or HTTP-level rules. Rules are written in HCL, checked into git, and unit tested against fixture requests. The proxy holds credentials (cookies, OAuth, AWS SigV4) so the agent never sees them, and it can route an action to an LLM judge, a human in Slack, or both before approval. The demo shows Codex in yolo mode being blocked from dropping the users table at the Postgres wire protocol level.

The core message is that agents cannot police themselves. Security requires an external enforcement point that understands the protocol and can enforce policy independent of the model's behavior. Dahl also discusses operational details like running the proxy over Tailscale/WireGuard and the importance of testing rules. While models will improve, the architecture of a separate guard layer remains essential for safe agent deployment.

- Agents are untrusted software; security cannot rely on the model's obedience or refusals.
- A proxy that parses traffic below HTTP is needed to catch subprocess-based attacks like psql over EKS.
- Rules in HCL are version-controlled and unit tested, providing declarative policy enforcement.
- Credentials are held by the proxy, not the agent, to prevent leakage and misuse.
- Actions can be gated by an LLM judge or human approval before execution.