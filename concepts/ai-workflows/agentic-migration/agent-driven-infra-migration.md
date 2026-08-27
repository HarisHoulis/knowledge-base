---
domain: ai-workflows
subdomain: agentic-migration
concept: agent-driven-infra-migration
title: Fable nailed my production YOLO infra migration
sources:
  - title: "Fable nailed my production YOLO infra migration"
    url: "https://www.youtube.com/watch?v=LNd2AT7evE4"
    author: "Kent C. Dodds"
    date: "2026-07-21T14:15:05+00:00"
---

# Fable nailed my production YOLO infra migration

Kent C. Dodds describes using an AI agent to perform a massive production migration of his site kentcods.com. With a single prompt to the agent, he changed 40,000 lines of code, moving from fly.io to Cloudflare as the host, and also switched from Prisma to Remix and from Cloudinary to Cloudflare, all in one giant pull request.

- A single agent prompt can drive a 40,000-line production migration when given clear context and scope.
- The migration involved moving hosting from fly.io to Cloudflare, changing the ORM/framework from Prisma to Remix, and replacing Cloudinary with Cloudflare.
- The site is highly dynamic and user-specific, so it cannot rely on CDN caching; it requires fast full server-side rendering.
- The move was motivated by Fly's LiteFS tooling reaching legacy status, pushing Kent to find a new long-term host.
- The site includes unique features like semantic search, podcast recording, user accounts, and team-based scoring, making the migration complex.