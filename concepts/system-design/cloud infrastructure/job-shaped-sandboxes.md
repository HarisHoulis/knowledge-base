---
domain: system-design
subdomain: cloud infrastructure
concept: job-shaped-sandboxes
title: Simplifying Containers with Cloudflare Sandboxes
sources:
  - title: "Simplifying Containers with Cloudflare Sandboxes"
    url: "https://kentcdodds.com/blog/simplifying-containers-with-cloudflare-sandboxes"
    date: "2026-03-11"
---

# Simplifying Containers with Cloudflare Sandboxes

The article describes migrating an audio-processing pipeline from Cloudflare Containers to Cloudflare Sandboxes, eliminating a complex lifecycle coordination layer. The initial container solution required heartbeats, idle checks, and shutdown signals because containers didn't automatically stop when the job finished. Sandboxes, by contrast, support a single `exec()` call that runs a command to completion and then the sandbox is destroyed, matching the one-shot nature of the job.

A first sandbox attempt (PR #726) recreated the container architecture as a long-lived service, but the merged approach (PR #729) made the sandbox an implementation detail of the existing queue worker. The worker creates presigned R2 URLs for inputs/outputs, calls `sandbox.exec()` with a shell script, and sends callbacks itself. The sandbox image contains only the Cloudflare sandbox base, FFmpeg, assets, and a CLI script, with no credentials.

Two production issues surfaced after deployment: the sandbox ID exceeded the 63-character limit, and the Dockerfile used a plain Debian image instead of the required Cloudflare sandbox base, causing 501 errors during exec. The ID was shortened to 35 characters, and the base image fix was identified and implemented by an AI agent using the Cloudflare MCP server. The entire iteration—from first container implementation to final sandbox design—took about an hour of developer time, demonstrating the value of agent-assisted exploration and debugging.

- Cloudflare Sandboxes let one-shot jobs run without heartbeat/shutdown coordination, unlike containers.
- The merged design embeds sandbox execution in the existing queue worker, using presigned R2 URLs and keeping credentials out of the sandbox.
- Two production failures required fixes: sandbox ID length (max 63 chars) and the need for the official Cloudflare sandbox base image.
- An AI agent debugged the production failure safely and wrote the fix, leveraging the Cloudflare MCP server.
- The container migration solved the immediate CPU problem, while the sandbox migration fixed the architectural complexity.