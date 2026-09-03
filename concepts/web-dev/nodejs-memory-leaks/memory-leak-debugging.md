---
domain: web-dev
subdomain: nodejs-memory-leaks
concept: memory-leak-debugging
title: Fixing a Memory Leak in a Production Node.js App
sources:
  - title: "Fixing a Memory Leak in a Production Node.js App"
    url: "https://kentcdodds.com/blog/fixing-a-memory-leak-in-a-production-node-js-app"
    author: "Kent C. Dodds"
    date: "2023-01-12"
---

# Fixing a Memory Leak in a Production Node.js App

Kent C. Dodds recounts debugging memory and CPU spikes in his production Node.js blog, which compiles ~200 MDX posts at runtime using mdx-bundler and shiki for syntax highlighting. Despite scaling down and removing LiteFS, the problem persisted, pointing to other changes in the migration process. Initial diagnosis using heap snapshots revealed a problematic ArrayBuffer from vscode-oniguruma, a dependency of shiki, allocating over 125MB (Dodds, 2023).

- Heap snapshots taken via a custom admin route helped identify vscode-oniguruma/shiki as a major memory consumer.
- Fixes included running shiki in a worker thread via tinypool with idleTimeout to allow memory reclamation.
- Caching evaluated MDX components with an LRU cache avoided repeated `new Function` compilation.
- Removing a leaking express-http-proxy for Cloudinary eliminated TLSSocket/request object retention.
- After fixes, memory stabilized at ~500MB, allowing scaling down from 2GB to 512MB.