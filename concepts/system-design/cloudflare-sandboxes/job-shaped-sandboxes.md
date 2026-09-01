---
domain: system-design
subdomain: cloudflare-sandboxes
concept: job-shaped-sandboxes
title: Simplifying Containers with Cloudflare Sandboxes
sources:
  - title: "Simplifying Containers with Cloudflare Sandboxes"
    url: "https://kentcdodds.com/blog/simplifying-containers-with-cloudflare-sandboxes"
    date: "2026-03-11"
---

# Simplifying Containers with Cloudflare Sandboxes

The article describes migrating an FFmpeg audio pipeline from Cloudflare Containers to Cloudflare Sandboxes. The previous container implementation required a complex lifecycle control plane: heartbeat pings from inside the container, an idle-check endpoint, and shutdown signals. Sandboxes simplify this by providing a one-shot `exec()` model—start a sandbox, run a command, wait for it to finish, and destroy it. This eliminated the entire coordination layer.

The final implementation has the queue worker act as orchestrator: it sends callbacks, creates short-lived presigned R2 URLs for inputs and outputs, runs a single `exec()` call in a fresh sandbox, and destroys the sandbox in a `finally` block. The sandbox image is minimal, based on `cloudflare/sandbox` with only FFmpeg, assets, and a single shell script added. It holds no credentials and knows nothing of the broader system. The article also notes that AI agents accelerated the iteration, enabling an abandoned first attempt and a safe production debugging session that identified two issues: sandbox ID length limits and missing sandbox runtime in the image base.

- Sandboxes with one-shot exec() remove the need for heartbeat and shutdown coordination.
- The worker owns callbacks and R2 credentials; the sandbox only receives signed URLs.
- Dockerfile stays tiny: base `cloudflare/sandbox` image plus ffmpeg and a script.
- AI agents allowed rapid experimentation and safe production debugging, isolating a base-image issue.
- Watch for Sandbox ID length limits and the requirement to use the official base image.