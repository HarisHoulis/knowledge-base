---
domain: ai-workflows
subdomain: claude-code
concept: ai-generated-web-tool
title: Video compressor using WebAssembly FFMPEG
sources:
  - title: "Video compressor"
    url: "https://simonwillison.net/2026/Sep/7/video-compressor/"
    date: "2026-09-07T18:29:07+00:00"
---

# Video compressor using WebAssembly FFMPEG

Simon Willison recorded a short demo video on his phone for his Equal Earth animation and wanted to publish an optimized version on his blog using FFMPEG. To do this, he used Claude Fable 5.1 in Claude Code for web to build a browser-based video compression tool. The tool leverages the WebAssembly build of FFMPEG, allowing video processing entirely in the browser without server-side encoding.

- The tool uses FFMPEG compiled to WebAssembly to run in the browser.
- It was built with Claude Fable 5.1 in Claude Code for web.
- The purpose was to optimize a phone-recorded video for blog publication.
- The tool demonstrates a practical use case for AI-assisted development of web utilities.