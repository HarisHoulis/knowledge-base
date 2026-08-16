---
domain: ai-workflows
subdomain: llm-chat-testing
concept: cors-chat
title: CORS Chat
sources:
  - title: "CORS Chat"
    url: "https://simonwillison.net/2026/Aug/15/cors-chat/"
    date: "2026-08-15"
---

# CORS Chat

CORS Chat is a browser-based tool built by Simon Willison to test OpenAI-Responses-compatible chat endpoints. It provides a web UI for exercising chat APIs that support CORS, with a focus on local LM Studio instances and hosted services like OpenRouter. The tool was created to facilitate testing Qwen 3.8 27B models running on an M5 MacBook Pro and an NVIDIA DGX Spark.

- Provides a web UI for testing OpenAI-Responses-compatible chat endpoints with CORS support.
- Works with LM Studio (using the --cors option) and OpenRouter.
- Conversations are persisted in the browser and can be exported as JSON.
- Progressively renders SVG images generated during streaming token responses.
- Built with the assistance of GPT-5.6-Sol xhigh, as noted in the linked gist.