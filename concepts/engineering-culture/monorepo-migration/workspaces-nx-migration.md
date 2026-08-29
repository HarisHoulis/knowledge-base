---
domain: engineering-culture
subdomain: monorepo-migration
concept: workspaces-nx-migration
title: Migrating to Workspaces and Nx
sources:
  - title: "Migrating to Workspaces and Nx"
    url: "https://kentcdodds.com/blog/migrating-to-workspaces-and-nx"
    date: "2026-03-10"
---

# Migrating to Workspaces and Nx

The article describes migrating kentcdodds.com from a pseudo-monorepo with separate package.json files and lockfiles to a proper npm workspaces setup with Nx. The main structural change was enforcing that all runnable services live under `services/*`, with the root package.json acting only as a thin orchestration layer for workspace management and convenience scripts. Nx was introduced minimally, relying on inferred package scripts and caching defaults rather than hand-authored project.json files, providing speed benefits mainly through caching (source: kentcdodds.com/blog/migrating-to-workspaces-and-nx).

The move exposed several latent assumptions. Import aliases like `#other/*` broke because Node enforces package boundaries once the site became `services/site`. A hardcoded content path in the GitHub API integration caused production downtime because the content directory moved to `services/site/content`. Docker build stages also needed explicit additions of the Prisma schema and config files. These issues illustrate how enforcing service boundaries surfaces hidden coupling and path assumptions (source: kentcdodds.com/blog/migrating-to-workspaces-and-nx).

CI was restructured to match the actual workload: site-only dependency installs for site changes, and separate worker installs. A missing Playwright browser install in the gate job surfaced as a CI failure, leading to cached browser installation. The author emphasizes that the real win was the structural clarity from `services/*`, not the Nx tooling itself, and warns against trusting an agent's confidence without verification (source: kentcdodds.com/blog/migrating-to-workspaces-and-nx).

- Enforce a clear monorepo structure like `services/*`; the root package.json should only orchestrate workspaces and convenience scripts.
- Use Nx minimally for caching and task orchestration; inferring scripts from package.json avoids project.json overhead.
- Moving services into subdirectories breaks import aliases and hardcoded paths; replace aliases with relative paths and centralize path logic.
- Update Dockerfile stages to include all files needed by each stage (e.g., Prisma schema) and test Docker builds locally or in CI.
- Restructure CI to install only the workspace being changed, and ensure prerequisites like Playwright browsers are explicitly installed and cached.