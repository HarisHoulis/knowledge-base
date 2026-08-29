---
domain: system-design
subdomain: web-rendering
concept: streaming-html-fragments
title: Compose & kotlinx.html
sources:
  - title: "Compose & kotlinx.html"
    url: "https://jakewharton.com/compose-and-kotlinx-html/"
    author: "Jake Wharton"
---

# Compose & kotlinx.html

The article presents a server-side rendering approach using Ktor and kotlinx.html to create reusable HTML layouts and page components. The author notes that while this works well initially, content becomes stale if left open for a long time. Rather than adopting a full client-side framework like Compose for HTML, the author proposes a lightweight isomorphic solution using Molecule to manage state and render HTML fragments on the server, which are then streamed to the client via WebSocket (source: https://jakewharton.com/compose-and-kotlinx-html/).

- Static server-rendered HTML with kotlinx.html becomes stale, so dynamic updates are needed.
- Molecule runs the composition on the server, producing a StateFlow<String> of HTML fragments that can be sent over WebSocket.
- The client receives the fragment and uses Idiomorph to morph the DOM, preserving form fields and interactive elements.
- For production, prefer a single connection with multiplexing, consider SSE over WebSocket for unidirectional payloads, and decide whether composition is per-connection or shared.
- The technique is suitable for low-traffic admin pages; evaluate tradeoffs for real user-facing sites.