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

The article describes migrating kentcdodds.com from a repo with multiple independent deployables and separate package managers to a proper npm workspaces monorepo with Nx. The key structural change was enforcing that all runnable applications live under `services/*`, each with its own package.json, while the root package.json became a thin orchestration layer with workspace declarations and forwarding scripts. Three old lockfiles were replaced by a single root lockfile, and Nx was added with minimal configuration, relying on caching defaults and package-script inference rather than hand-authored project files.

The migration surfaced several real-world issues. Package import aliases broke because Node enforces package boundaries once a subpackage is defined. Production went down because content paths hardcoded to `content/` had moved to `services/site/content/`. Docker build stages needed additional paths like the Prisma schema. The article emphasizes that restructuring around real service boundaries exposed hidden assumptions and that CI was then optimized around the actual workload, including site-only installs and Playwright browser caching.

The main lesson is to validate large refactors locally rather than trusting an agent's confidence, especially when the agent cannot build Docker images. Nx was useful mainly for caching; the real win came from having a clean, consistent monorepo structure.

- Move all runnable deployables under `services/*`, each with its own package.json, and make the root package.json a thin orchestration layer.
- Nx can be added minimally with caching defaults and package-script inference; no need for hand-authored project.json files.
- Enforcing package boundaries breaks import aliases that cross package roots; replace them with relative paths.
- Hardcoded content paths break when files move directories; centralize path logic and create graceful fallbacks.
- Restructure CI around actual usage patterns: install only the workspace needed and cache Playwright browsers to avoid surprise failures.