---
domain: ai-workflows
subdomain: managed-agents
concept: cloud-sandboxed-agents
title: Build Your Own Team of Managed Agents
sources:
  - title: "Build Your Own Team of Managed Agents - Jack Wotherspoon, Google DeepMind"
    url: "https://www.youtube.com/watch?v=Y_p3y6zP5QE"
    author: "AI Engineer"
    date: "2026-10-26"
---

# Build Your Own Team of Managed Agents

Jack Wotherspoon (Google DeepMind) explains managed or cloud-based agents: instead of running an agent on your own laptop, you run it in a cloud sandbox. Sandboxes are powerful because they don't hijack your local machine (browser pop-ups, spawned processes) and because your laptop isn't scalable—you can't easily share a personal agent setup with colleagues or embed it in a customer-facing app without routing users through your personal subscription. Managed agents solve this by letting you scale properly.

Building this yourself is tedious: creating a container or VM, downloading dependencies, building a testing system, and handling network settings, firewall rules, and security. Gemini managed agents reduce this to a single API call that provisions a sandbox with a ready-made "antigravity" toolkit built in; scaling means making more API calls.

The offering lives in the new Interactions API, a reworked SDK focused on agents rather than the old model input/output pattern, since interactions better represent what agents do (creating and accessing files, calling MCP tools). You call an agent and set the environment parameter to "remote" to request a cloud-managed agent. Internally, the call goes to the Gemini API with built-in server tools (web search via Google, file system tools) plus custom or MCP tools, and launches a sandbox on Google Cloud infrastructure. You can upload files at launch, including agent skills, an agents.md file, or a GitHub repository.

The core building blocks are the antigravity framework (the same framework powering Google's antigravity products, handling tool calls and built-in tools), the environment (a separate entity enabling multi-agent workflows where different agents share a sandbox and hand off files), and skills uploaded into the sandbox.

- Managed agents run in cloud sandboxes, avoiding local machine hijacking and enabling sharing and scaling beyond a personal laptop.
- Gemini managed agents provision a sandbox with a built-in antigravity toolkit via a single API call, eliminating container, networking, and security setup.
- The new Interactions API models agent behavior (file creation, MCP tool calls) better than the old model input/output SDK.
- Setting the environment parameter to "remote" requests a cloud-managed agent backed by Google Cloud infrastructure.
- The environment is a separate entity, enabling multi-agent workflows where agents share a sandbox and pass files between them.