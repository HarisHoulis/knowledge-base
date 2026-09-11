---
domain: ai-workflows
subdomain: spatial-agent-interfaces
concept: agents-on-the-canvas
title: The Spatial Harness: Bringing Agents to the Canvas
sources:
  - title: "The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw"
    url: "https://www.youtube.com/watch?v=XWcXwnysmpY"
    author: "Max Drake"
    date: "2026-09-10"
---

# The Spatial Harness: Bringing Agents to the Canvas

Max Drake, a product engineer at tldraw, argues that the infinite canvas is a strong medium for collaborating with LLM agents, not just with people. tldraw is described as a free infinite-canvas whiteboarding app, a London-based company, and — most importantly for this talk — the SDK that powers many infinite-canvas experiences, including Replit's agent canvas work (Drake, "The Spatial Harness").

The SDK exists because would-be canvas-app builders kept getting stuck on the canvas primitives themselves — resizing, selection, matrix math — instead of building their actual product. Drake says the same pattern repeated after LLMs arrived: people had ideas for apps with LLMs manipulating things in space, but "there were no best practices" and they got stuck. tldraw's response was to make it easy to build with agents and LLMs on the canvas (Drake, "The Spatial Harness").

Drake points to tldraw's built-in multiplayer — live sync, collaborator cursors, selections, and viewports — and claims that the properties making a canvas good for human collaboration also make it a good place to interact and collaborate with agents (Drake, "The Spatial Harness").

As a contrast, he notes that agents working off-canvas, such as Claude Code, work well partly because their medium (writing code) is essentially text-in, text-out — the format they were trained on (Drake, "The Spatial Harness"). He closes the opening with a live demo: asking his agent to find a Notion document a colleague emailed and build that demo in the tldraw desktop app (Drake, "The Spatial Harness").

- tldraw is an infinite-canvas whiteboard app and, more importantly here, an SDK powering many canvas experiences, including Replit's agent canvas.
- The SDK was built because teams kept getting stuck on canvas primitives (resizing, selection, matrix math) rather than on their actual app.
- The same failure pattern recurred with LLM-on-canvas apps, where no best practices existed yet.
- tldraw ships multiplayer (live sync, cursors, selections, viewports), and Drake argues these same qualities make the canvas good for collaborating with agents.
- Off-canvas coding agents like Claude Code work well partly because code is text-in, text-out — the medium they were trained on.