---
domain: ai-workflows
subdomain: ai-agent-security
concept: lethal-triad
title: Your AI Isn't the Problem, Your Infrastructure Is
sources:
  - title: "Your AI Isn't the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder"
    url: "https://www.youtube.com/watch?v=Wb2v9Phhnns"
    author: "AI Engineer"
    date: "2026-10-14"
---

# Your AI Isn't the Problem, Your Infrastructure Is

Shao-Chun Jiang, Lead Product Manager at Coder, argues that failures in AI agent deployments stem from infrastructure rather than model quality. Drawing on real incidents at regulated companies, she contends that paying more for a smarter model cannot fix the underlying problem, because large language models are inherently non-deterministic and lack any structural distinction between instructions and context — all information reaches the model through the same door, so contradictory context can override explicit instructions. The solution is infrastructural control: locking the door rather than telling someone not to leave the room.

Jiang frames the risk using the "lethal triad," a concept coined by AI researcher Simon Willison describing the vulnerability that arises when an agent simultaneously has access to confidential private data, unreliable content it did not create, and the ability to communicate externally. Any one of these is often necessary for an agent to be useful, but combined they enable serious incidents. She stresses that agents causing damage are typically not compromised by external attackers — they are simply following the permissions they were given.

The talk's core message is that prevention is achievable now, not in some future where models become trustworthy. Organizations already possess many of the tools needed; they simply have not yet customized them for the AI world. Rather than vague advice like stopping AI use altogether, Jiang promises concrete steps companies can take this week to constrain what their agents are authorized to do.

- AI agent failures are an infrastructure problem, not a model problem — smarter models cannot eliminate the risk
- LLMs are non-deterministic and cannot structurally distinguish instructions from context, making them impossible to fully trust
- The "lethal triad" (private data access + untrusted content + external communication) creates critical agent vulnerability
- Damaging agents usually act within granted permissions rather than being hijacked by external attackers
- Prevention comes from infrastructural controls you can implement now, not from waiting for better models