---
domain: engineering-culture
subdomain: monorepo-migration
concept: npm-workspaces-nx-migration
title: Migrating to Workspaces and Nx
sources:
  - title: "Migrating to Workspaces and Nx"
    url: "https://kentcdodds.com/blog/migrating-to-workspaces-and-nx"
    author: "Kent C. Dodds"
    date: "2026-03-10"
---

# Migrating to Workspaces and Nx

Kent C. Dodds describes migrating kentcdodds.com from a folder-based monorepo with multiple independent package.json files to a proper npm workspaces monorepo, consolidating all runnable services under services/* and using a single root lockfile. The root package.json became a thin orchestration layer with convenience scripts forwarding to the main site workspace, while Nx was introduced primarily for caching with minimal configuration and no hand-authored project files (source: Kent C. Dodds, 2026).

- Enforce a simple structural rule: every runnable thing lives under services/*, and the root package.json only owns workspace-wide orchestration.
- Moving packages into subdirectories breaks package import aliases and hardcoded path assumptions; fix with explicit relative paths and centralize content path constants.
- Always pull down and locally run structural refactors before deploying; the GitHub content path change caused a production outage.
- Use Nx caching for repeated tasks, but the real win is the enforced service boundary rather than the tool itself.
- Restructure CI to install only the workspace being tested and cache Playwright browsers to avoid missing browser binaries in gate jobs.