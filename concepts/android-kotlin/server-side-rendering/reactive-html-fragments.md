---
domain: android-kotlin
subdomain: server-side-rendering
concept: reactive-html-fragments
title: Compose & kotlinx.html
sources:
  - title: "Compose & kotlinx.html"
    url: "https://jakewharton.com/compose-and-kotlinx-html/"
    author: "Jake Wharton"
---

# Compose & kotlinx.html

Jake Wharton discusses using kotlinx.html with Ktor for server-rendered HTML pages, but notes that content becomes stale after a minute or two. Rather than adopting client-side Compose for HTML, he uses Molecule to run Compose-style composition on the server, emitting HTML fragments as a StateFlow<String> over WebSocket. The client then patches the existing DOM using Idiomorph, which preserves interactive elements like form fields. He cautions that this approach is suitable for low-traffic admin pages and suggests improvements for production: using SSE instead of WebSocket for unidirectional updates, framing payloads to target specific DOM IDs, and deciding whether composition runs per-connection or is shared.

- Server-rendered HTML with kotlinx.html becomes stale; Molecule enables streaming HTML fragments from the server.
- Molecule runs composition on the JVM and emits HTML strings, which can be sent over WebSocket to the client.
- Idiomorph patches the DOM by morphing existing content, preserving interactive elements.
- For production, prefer SSE over WebSocket and use an envelope to multiplex updates to different elements.
- Consider whether the composition is tied to a connection or shared across connections based on data types.