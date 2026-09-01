---
domain: engineering-culture
subdomain: monorepo-migration
concept: workspaces-nx-migration
title: Migrating to Workspaces and Nx
sources:
  - title: "Migrating to Workspaces and Nx"
    url: "https://kentcdodds.com/blog/migrating-to-workspaces-and-nx"
    author: "Kent C. Dodds"
    date: "2026-03-10"
---

# Migrating to Workspaces and Nx

Kent C. Dodds migrated kentcdodds.com from a loose monorepo with multiple independent package.json files to a proper npm workspaces setup with Nx. The key structural change was enforcing that all runnable services live under `services/*`, making the root package.json a thin orchestration layer and giving each service its own package boundary. This exposed hidden assumptions in the codebase, such as package import aliases that no longer resolved and hardcoded content paths that broke production.

- Enforce a `services/*` directory structure so every deployable has its own package boundary and the root package.json only orchestrates.
- Use Nx minimally for caching and package-script inference rather than hand-authoring project.json files.
- Moving code can break runtime assumptions like import aliases and hardcoded content paths; verify with local runs, not just agent confidence.
- Restructure CI around actual workspace usage: install only the workspace being tested and cache Playwright browsers appropriately.