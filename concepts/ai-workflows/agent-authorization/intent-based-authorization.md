---
domain: ai-workflows
subdomain: agent-authorization
concept: intent-based-authorization
title: Intent-Based Authorization for AI Agents: Limits of OAuth and the Case for Runtime Intent
sources:
  - title: "An AI Agent Got Its User Banned From Resy — Keycard, JPMorgan Chase & AAuth"
    url: "https://www.youtube.com/watch?v=IavxrdVnwXM"
    author: "AI Engineer"
    date: "2026-10-17"
---

# Intent-Based Authorization for AI Agents: Limits of OAuth and the Case for Runtime Intent

A panel from Keycard (Ellie, Ian) with JPMorgan Chase's Michael Davis and OAuth co-author Dick Hardt discusses why giving AI agents more autonomy is hard despite stronger models. Runtime authorization—verifying an agent's rights on each tool invocation rather than granting permanent access—is proposed as the direction, but deciding whether an action is safe is complicated because MCP tools and APIs are under-specified, perfect policies are hard to write, and the agent's environment constantly changes. Intents are offered as extra context to make better runtime decisions about what an agent may do [source].

Ian argues regulated firms prioritize security and business continuity over innovation, and that enterprises are a mix of identity 'islands' from different worlds. The core problem is that modern security systems were built for a world where humans made all decisions and software was deterministic, while access scopes are too coarse—citing Salesforce's long-standing single OAuth API scope as an example that is not useful for agents [source].

Dick Hardt explains OAuth was designed for one website interacting with another, with prior registration, browser redirects, and later scopes; it was not built for agents whose required actions aren't known in advance, where different instances of the same agent need different access levels, and where OAuth-style scopes are too crude [source].

Michael Davis says successful companies onboard agents like developers—starting without full change access and progressing gradually. Safety context isn't just what the agent claims; environment signals such as whether it runs in a sandbox can change the allowed autonomy level [source].

- Runtime authorization checks agent rights per tool invocation instead of granting permanent, abusable access.
- OAuth was built for site-to-site flows with prior registration and browser redirects, and its scopes are too coarse for agent tasks.
- Modern security systems assume human decisions and deterministic software, not autonomous agents.
- Intents supply runtime context to decide what an agent is allowed to do when policies and tool descriptions are insufficient.
- Companies onboard agents like developers: start with limited access and grant more as they progress, using environment signals like sandboxing.