---
domain: system-design
subdomain: cloudflare-sandboxes
concept: job-shaped-sandbox
title: Simplifying Containers with Cloudflare Sandboxes
sources:
  - title: "Simplifying Containers with Cloudflare Sandboxes"
    url: "https://kentcdodds.com/blog/simplifying-containers-with-cloudflare-sandboxes"
    author: "Kent C. Dodds"
    date: "2026-03-11"
---

# Simplifying Containers with Cloudflare Sandboxes

The article details how Kent C. Dodds migrated an FFmpeg audio processing pipeline from Cloudflare Containers to Cloudflare Sandboxes. The container approach required a 'heartbeat dance': the container couldn't signal completion, so he had to build heartbeat pings, idle checks, and shutdown endpoints purely for lifecycle management. Cloudflare Sandboxes offer a simpler model: calling `sandbox.exec()` runs a command and finishes when it's done, eliminating that coordination layer entirely (Kent C. Dodds, 2026).

The first sandbox attempt (PR #726) still mirrored the container architecture by creating a separate service with its own HTTP endpoint, callback ownership, and R2 credentials. The merged design (PR #729) instead made the sandbox an implementation detail of the existing queue worker. The worker creates presigned R2 URLs, runs a single `exec()` call in a fresh sandbox, and destroys it in a `finally` block. The sandbox image is minimal: it runs one shell script that downloads inputs, runs FFmpeg, uploads outputs, and exits. No credentials or secrets enter the sandbox (Kent C. Dodds, 2026).

The article also highlights two production issues caught after deployment: sandbox IDs exceeded the 63-character limit, and the initial Dockerfile used plain Debian instead of the official `cloudflare/sandbox` base image, causing 501 errors. Both were fixed, with the latter debugged by an AI agent using live production tooling. The author emphasizes that new infrastructure primitives are only helpful if they change the system's shape; the sandbox's one-shot execution model is the natural fit for job-shaped work (Kent C. Dodds, 2026).

- Cloudflare Sandboxes remove the heartbeat/shutdown plumbing required by Containers for one-shot jobs.
- The best design embeds the sandbox directly in the queue worker, not as a separate service.
- Sandboxes use presigned R2 URLs, so no credentials are passed inside.
- Production debugging can be safely delegated to AI agents, but human review is still essential.
- Infrastructure primitives are most valuable when they let you simplify the architecture.