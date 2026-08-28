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

The article recounts migrating kentcdodds.com to a proper monorepo structure using npm workspaces and Nx. Previously, the repo contained multiple deployable services (the main site, an OAuth worker, and two audio-related components) each with its own package.json and lockfile, making the folder layout a monorepo only in name. The change consolidated all runnable services under `services/*`, turned the root package.json into a thin orchestration layer, and replaced three lockfiles with a single root lockfile (source: Migrating to Workspaces and Nx, 2026).

The migration exposed three categories of breakage. First, package import aliases like `#other/*` failed because Node's package boundary rules rejected imports outside the package root, requiring replacement with explicit relative paths. Second, production went down because the GitHub content path hardcoded as `content/` was now `services/site/content/`, causing 404s; a centralized path utility and graceful fallbacks fixed the issue. Third, Docker build stages needed additional files (Prisma schema and config) that were previously omitted from the production-deps stage (source: Migrating to Workspaces and Nx, 2026).

CI was restructured around actual usage: the site installs only its own dependencies, and Playwright browsers are cached and installed in the gate job. The author emphasizes that Nx's caching was useful, but the real win was the structural clarity of `services/*`, and warns against trusting an agent's confidence—it should be made to prove changes work, especially for infrastructure (source: Migrating to Workspaces and Nx, 2026).

- Enforce a strict `services/*` layout for every runnable service, with a thin root package.json that delegates to workspaces.
- Node package alias boundaries cause failures when code moves into a subpackage; replace aliases with relative imports.
- Hardcoded paths relative to the repo root will break in a monorepo—centralize content paths to survive moves.
- Docker stages need the full set of files (e.g., Prisma schema) even when not directly used in install steps.
- Use Nx for caching but treat the structural monorepo change as the primary improvement.