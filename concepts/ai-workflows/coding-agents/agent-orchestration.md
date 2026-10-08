---
domain: ai-workflows
subdomain: coding-agents
concept: agent-orchestration
title: Steal My App: Self-Hosting Cody with AI Agents
sources:
  - title: "Steal My App (I'll Show You How)"
    url: "https://www.youtube.com/watch?v=zuR3JEQmSLk"
    author: "Kent C. Dodds"
    date: "2026-10-06"
---

# Steal My App: Self-Hosting Cody with AI Agents

Kent C. Dodds demonstrates orchestrating multiple AI agents to self-host the Cody application outside of Cloudflare. He begins by consulting a Grok bot named Cody, which serves as a "commander in chief" communicating with other bots via MCP servers to perform tasks. When asked about self-hosting, the bot initially misunderstands and suggests hosting Jev instead, but after clarification, it researches the problem and concludes that running Cody outside Cloudflare would require a complete rewrite due to deep Cloudflare dependencies. Dodds notes that while Cody is open source and can run on a personal Cloudflare account, running it in a Docker container outside Cloudflare is "fusion level of complexity."

The breakthrough comes from staying informed about external developments: Deno recently released its own implementation of Durable Objects, a daemon that runs Cloudflare Workers and Durable Objects on your own hardware with state in S3-compatible storage, using the same Wrangler packages. This revises the difficulty from "thermonuclear" to merely difficult, though some Cloudflare-specific services like Vectorize, Workers AI, AI Gateway, and email processing would still need adapters. Dodds emphasizes the importance of keeping an eye on what's happening outside your usual work and sharing findings with your agent for investigation.

With the path clarified, Dodds delegates the actual implementation to a cloud agent named Devon, instructing it to use the Cody MCP server to create a new repository called KodiBot. He tells Devon to use the best model available in Devon Cloud, decide for itself how to build it, and complete the task fully without half-measures. Dodds explicitly states he doesn't want to be involved in the details and won't look at the result until it's completely done, framing this as an experiment in agent autonomy. The approach leverages adapters so that one project could later support both Cloudflare and self-hosted environments.

- A Grok bot named Cody acts as a "commander in chief" that communicates with other bots via MCP servers to research and perform tasks.
- Self-hosting Cody outside Cloudflare was initially deemed "fusion level of complexity" due to deep Cloudflare dependencies, but Deno's new Durable Objects implementation made it feasible.
- Staying informed about external developments (like Deno's release) can unlock solutions that agents can then investigate and apply.
- Dodds delegates the full implementation to a cloud agent named Devon, instructing it to use the best model, decide its own approach, and complete the task without half-measures.
- The goal is to use adapters so the same project can later support both Cloudflare and self-hosted environments.