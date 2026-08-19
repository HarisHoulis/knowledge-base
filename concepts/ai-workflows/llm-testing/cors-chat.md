---
domain: ai-workflows
subdomain: llm-testing
concept: cors-chat
title: CORS Chat
sources:
  - title: "CORS Chat"
    url: "https://simonwillison.net/2026/Aug/15/cors-chat/"
    date: "2026-08-15T14:49:54+00:00"
---

# CORS Chat

CORS Chat is a browser-based tool built to test OpenAI-Responses-compatible chat endpoints, specifically for evaluating Qwen 3.8 27B running in LM Studio on an M5 MacBook Pro and an NVIDIA DGX Spark. The tool provides a simple web UI that works with LM Studio's `--cors` option and with OpenRouter, enabling cross-origin requests from the browser. Conversations are persisted locally in the browser and can be exported as JSON, making it easy to share or debug interactions. A notable feature is the progressive rendering of SVG images generated during streaming, allowing users to watch outputs appear token by token. This utility reflects a practical approach to LLM tooling, focusing on interoperability and developer convenience.

- CORS Chat is a lightweight web UI for testing OpenAI-Responses-compatible chat endpoints directly from the browser.
- It supports both local LM Studio (with `--cors`) and OpenRouter, enabling flexible testing of models like Qwen 3.8 27B.
- Conversations persist in the browser and can be exported as JSON for sharing or further analysis.
- The tool progressively renders SVG images as tokens stream in, offering real-time visualization of generated content.