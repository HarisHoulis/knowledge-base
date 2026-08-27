---
domain: system-design
subdomain: cloud-infrastructure
concept: sandbox-job-lifecycle
title: Simplifying Containers with Cloudflare Sandboxes
sources:
  - title: "Simplifying Containers with Cloudflare Sandboxes"
    url: "https://kentcdodds.com/blog/simplifying-containers-with-cloudflare-sandboxes"
    author: "Kent C. Dodds"
    date: "2026-03-11"
---

# Simplifying Containers with Cloudflare Sandboxes

The article describes migrating an FFmpeg audio stitching pipeline from Cloudflare Containers to Cloudflare Sandboxes. Previously, the container-based approach required a complex control plane with heartbeat pings, idle checks, and shutdown signals to manage the container lifecycle. The sandbox model eliminates this because each sandbox runs a single `exec()` command to completion and then exits, matching the natural lifecycle of a one-shot job.

- Cloudflare Sandboxes allow a single `sandbox.exec()` call to run a job to completion, removing the need for heartbeat and shutdown coordination.
- The final design embeds the sandbox invocation directly in the queue worker, which creates short-lived presigned R2 URLs, runs a shell script inside the sandbox, and destroys the sandbox in a `finally` block.
- The sandbox image is minimal: it uses the official `cloudflare/sandbox` base image, installs FFmpeg, copies assets and a shell script, and requires no credentials inside the sandbox.
- Two issues surfaced only in production: sandbox IDs must be 1-63 characters, and the image must include the Cloudflare sandbox runtime (not a plain Debian with custom CMD).
- An AI agent was used to investigate the production failure safely, using real env vars and fake draft IDs to isolate the issue, and then fix the Dockerfile.