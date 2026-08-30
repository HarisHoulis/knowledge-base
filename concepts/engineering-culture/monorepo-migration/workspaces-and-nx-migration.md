---
domain: engineering-culture
subdomain: monorepo-migration
concept: workspaces-and-nx-migration
title: Migrating to Workspaces and Nx
sources:
  - title: "Migrating to Workspaces and Nx"
    url: "https://kentcdodds.com/blog/migrating-to-workspaces-and-nx"
    author: "Kent C. Dodds"
    date: "2026-03-10"
---

# Migrating to Workspaces and Nx

The article describes migrating kentcdodds.com from a loose set of sibling packages to a proper npm workspaces monorepo with Nx. The new structure places every runnable service under `services/*`, with a thin root `package.json` that owns workspace declarations and Nx. Each service keeps its own package.json and scripts, while the root lockfile replaces three nested lockfiles. The migration was largely structural, with Nx used minimally for caching via target defaults.

- Enforce a `services/*` layout for every runnable deployable to create real package boundaries.
- Use a root package.json only for workspace orchestration and convenience scripts; keep app-specific scripts in each service.
- Package import aliases that cross package boundaries fail with ERR_INVALID_PACKAGE_TARGET; replace with relative paths.
- Moving content paths can break runtime GitHub API fetches—centralize path logic in a utility.
- CI should install per-workspace dependencies and cache Playwright browsers to avoid expensive full installs.
- Don't rely on an agent's confidence; verify structural refactors locally or in a staging environment.