---
domain: ai-workflows
subdomain: model-context-protocol
concept: mcp-apps
title: MCP Apps: Extending the Frontier
sources:
  - title: "MCP Apps: Extending the Frontier — Ido Salomon & Liad Yosef"
    url: "https://www.youtube.com/watch?v=-jY2T2PiJBE"
    author: "AI Engineer"
    date: "2026-08-02T23:30:06+00:00"
---

# MCP Apps: Extending the Frontier

The talk introduces MCP Apps, an extension to the Model Context Protocol (MCP) that enables services to send their own interactive UI directly into chat clients, avoiding the limitation of text-only responses. The speakers, Ido Salomon and Liad Yosef, explain that this approach preserves brand identity and UX, which is a key concern for companies building MCP servers. MCP Apps originated from MCPUI, an open protocol created by Salomon in May of the previous year, and later became an official MCP extension through a partnership with Anthropic and OpenAI. The protocol is now supported by major clients such as Claude, VS Code, ChatGPT, Cursor, and others, with early adopters including Eleven Labs, Shopify, Postman, and Block. The talk also covers the core concept of transmitting UI over MCP, using existing primitives like resources to return HTML, and enabling interactivity for actions like favoriting a song. The speakers highlight the growing community and open working group that continues to evolve the spec.

- MCP Apps allow services to send their own UI to chat clients, preserving brand identity and UX instead of reducing them to text databases.
- MCPUI was the original open protocol created by Ido Salomon, later partnered with Anthropic and OpenAI to become the official MCP Apps extension.
- Adoption includes clients like Claude, VS Code, ChatGPT, Cursor, and companies like Shopify, Postman, Eleven Labs, and Block.
- The protocol supports interactivity, not just visualization, allowing users to interact directly with the embedded UI.
- An open working group convenes every three weeks to refine the spec and support the community.