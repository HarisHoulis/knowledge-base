---
domain: ai-workflows
subdomain: llm-testing-tools
concept: cors-chat
title: CORS Chat
sources:
  - title: "CORS Chat"
    url: "https://simonwillison.net/2026/Aug/15/cors-chat/"
    author: "Simon Willison"
    date: "2026-08-15"
---

# CORS Chat

CORS Chat is a web-based tool created by Simon Willison to facilitate testing OpenAI-Responses-compatible chat endpoints, particularly for local models like Qwen 3.8 27B running in LM Studio on an M5 MacBook Pro or NVIDIA DGX Spark (Source: Simon Willison, 2026). The tool provides a simple UI that works with LM Studio when launched with the --cors option, as well as with OpenRouter, making it flexible for various local and remote LLM setups (Source: Simon Willison, 2026).

A key feature of CORS Chat is its ability to persist conversations in the browser and export them as JSON, allowing users to save and share chat sessions. Additionally, it detects SVG images generated during streaming and progressively renders them in real time, enhancing the chat experience for multimodal outputs (Source: Simon Willison, 2026). The tool was built with the assistance of GPT-5.6-Sol xhigh, demonstrating an AI-assisted development workflow (Source: Simon Willison, 2026).

- CORS Chat is a web UI for testing OpenAI-Responses-compatible chat endpoints, supporting LM Studio with --cors and OpenRouter (Source: Simon Willison, 2026).
- Conversations are stored in the browser and can be exported as JSON for portability (Source: Simon Willison, 2026).
- It progressively renders SVG images while tokens stream, useful for multimodal chat (Source: Simon Willison, 2026).
- The tool was built using GPT-5.6-Sol xhigh, an example of AI-assisted coding (Source: Simon Willison, 2026).