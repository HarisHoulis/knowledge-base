---
domain: web-dev
subdomain: modern-website-architecture
concept: modern-website-stack
title: How I built a modern website in 2021
sources:
  - title: "How I built a modern website in 2021"
    url: "https://kentcdodds.com/blog/how-i-built-a-modern-website-in-2021"
    author: "Kent C. Dodds"
    date: "2021-09-29"
---

# How I built a modern website in 2021

In this article, Kent C. Dodds describes the architecture and technology choices behind the complete rewrite of kentcdodds.com, which he considers a full-stack web application rather than a simple blogfolio. The site runs on Remix and React with TypeScript, uses Prisma for ORM, XState for state management, Tailwind CSS for styling, and is deployed on Fly.io across multiple regions. He emphasizes that the scale – about 27k lines of TypeScript and 280k words of content – justifies the complexity (Kent C. Dodds, 2021).

- The site is a large Remix application (27k lines of TypeScript, 280k words of content) with user accounts, a database, and a cache, making it a modern full-stack app.
- Deployment uses two GitHub Actions: one refreshes content by fetching changed MDX files from GitHub and updating the Redis cache (reducing updates from 10-25 minutes to 8 seconds), and the other runs lint, type checks, tests, and builds before deploying with Fly.io.
- Fly.io enables multi-region deployment with colocated Postgres and Redis clusters; non-primary regions are read-only to maintain consistency, avoiding vendor lock-in via Docker containers.
- The tech stack includes React, Remix, TypeScript, XState, Prisma, Express, Cypress, Jest, Tailwind CSS, MSW, and mdX-bundler, among others.