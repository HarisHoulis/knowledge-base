---
domain: system-design
subdomain: scaling-large-systems
concept: scaling-performance-lessons
title: Scaling Slack and GitHub: Performance, Load Testing, and Database Sharding Lessons
sources:
  - title: "Scaling Slack and GitHub with Maude Lemaire"
    url: "https://newsletter.pragmaticengineer.com/p/scaling-slack-and-github-with-maude"
    author: "Gergely Orosz"
    date: "2026-11-05"
---

# Scaling Slack and GitHub: Performance, Load Testing, and Database Sharding Lessons

Maude Lemaire, a principal engineer and author of 'Refactoring at Scale,' shares lessons from scaling backend infrastructure at Slack, GitHub, and Cursor. She argues performance should matter even without external competition: at Rent the Runway she sped up a 10-second homepage load on her own initiative because 'the best competition is competition with yourself' (Orosz, 2026).

At Slack, fan-out costs drove concrete design constraints. Custom emojis are capped at 23 because each emoji fans out to every member of a channel, so a 100,000-member channel posting 100 emojis means 10 million fan-outs. Related 'event floods' overwhelm power users' WebSockets when many busy channels fire at once. To load test 500,000 WebSocket connections, spinning up headless Chrome sessions would have cost roughly $150,000 per run, so Lemaire built Koi Pond, slimmed-down Go-based Slack clients ('Koi') that establish the connections cheaply (Orosz, 2026).

At GitHub, the Rails monolith's Active Record abstraction hid database cost: the homepage triggered about 100 SQL queries across three clusters, and many were scatter queries lacking a sharding key, which capped GitHub at 16 shards because more shards slow such queries. On AI, Lemaire personally verifies all LLM output for foundational platform work, and she recommends rotating platform and product engineers so platform engineers stay connected to real product experience (Orosz, 2026).

- Performance work is worthwhile even without competitors; pursue it proactively when it improves user experience.
- Fan-out costs shape product limits: Slack caps custom emojis at 23 to avoid thundering-herd network load.
- Load testing at scale needs cheap simulated clients: Koi Pond's Go-based 'Koi' avoided a ~$150,000-per-run headless Chrome approach for 500,000 WebSocket connections.
- Developer-friendly abstractions like Active Record can hide database load; scatter queries without sharding keys limited GitHub to 16 shards.
- Verify LLM output carefully for foundational platform work, and rotate platform and product engineers to keep platform work grounded in product reality.