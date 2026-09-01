---
domain: system-design
subdomain: cloudflare-sandboxes
concept: job-shaped-sandboxes
title: Simplifying Containers with Cloudflare Sandboxes
sources:
  - title: "Simplifying Containers with Cloudflare Sandboxes"
    url: "https://kentcdodds.com/blog/simplifying-containers-with-cloudflare-sandboxes"
    author: "Kent C. Dodds"
    date: "2026-03-11"
---

# Simplifying Containers with Cloudflare Sandboxes

In this article, Kent C. Dodds describes migrating an FFmpeg audio-processing pipeline from Cloudflare Containers to Cloudflare Sandboxes. The container implementation required a complex lifecycle-control plane, including heartbeat pings, idle checks, and shutdown signals, to manage the container's state. Sandboxes offer a simpler model: you run a single `exec()` command, wait for it to finish, and the sandbox is automatically done. This eliminates the coordination layer entirely, as the queue worker becomes the orchestrator that creates presigned R2 URLs, invokes a one-shot sandbox process, and handles callbacks itself.

- Sandboxes provide a one-shot execution model that removes the need for heartbeat/shutdown coordination required by containers.
- The final design keeps R2 credentials in the worker and gives the sandbox only short-lived presigned URLs, reducing security exposure.
- The sandbox image is minimal: the official `cloudflare/sandbox` base image plus FFmpeg and a single shell script.
- AI agents accelerated architectural iteration; an abandoned PR informed the final design, and an agent debugged a production issue by probing the live environment.
- Two production issues surfaced after merge: sandbox ID length (must be 1-63 chars) and the need to use the official base image rather than plain Debian.