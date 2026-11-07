---
domain: system-design
subdomain: hybrid-ui-architecture
concept: server-driven-ui
title: Yelp Combines Native and Server-Driven UI for Its AI Assistant
sources:
  - title: "Yelp Combines Native and Server-Driven UI for Its AI Assistant"
    url: "https://www.infoq.com/news/2026/11/yelp-assistant-hybrid-ui/"
    author: "Leela Kumili"
    date: "2026-11-06"
---

# Yelp Combines Native and Server-Driven UI for Its AI Assistant

Yelp's AI Assistant uses a hybrid architecture that blends native mobile controls with server-driven conversation rendering, built on an internal framework called CHAOS. The design separates view configuration from conversation data, letting the backend drive chat interactions and enabling UI updates without shipping new app releases (Kumili, InfoQ).

The approach addresses cross-platform challenges by reusing the same server-driven rendering model across platforms, and Yelp reports it also supports reuse for its Biz Ask Anything pilot. The core tradeoff is flexibility: server-driven UI lets Yelp iterate on conversational experiences faster, while native controls preserve platform-appropriate behavior where needed.

- Hybrid UI mixes native mobile controls with server-driven conversation rendering via the CHAOS framework
- View configuration is decoupled from conversation data, enabling backend-driven chat interactions
- UI updates can ship without new app releases
- The model helps address cross-platform challenges and is reused for the Biz Ask Anything pilot