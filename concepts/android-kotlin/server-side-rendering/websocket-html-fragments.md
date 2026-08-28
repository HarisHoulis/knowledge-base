---
domain: android-kotlin
subdomain: server-side-rendering
concept: websocket-html-fragments
title: Compose & kotlinx.html
sources:
  - title: "Compose & kotlinx.html"
    url: "https://jakewharton.com/compose-and-kotlinx-html/"
---

# Compose & kotlinx.html

Jake Wharton presents a pattern for keeping server-rendered HTML fresh without abandoning static HTML delivery. The starting point is a Ktor route using kotlinx.html's `respondHtml` with reusable layout and component functions, backed by a `StateFlow<List<User>>`. This works until the page goes stale after a minute or two (https://jakewharton.com/compose-and-kotlinx-html/).

- Use Molecule to run composition on the JVM and render HTML fragments as a `StateFlow<String>` over a WebSocket.
- Patch the DOM client-side with Idiomorph to preserve form fields and interactive elements.
- For production, prefer a single multiplexed connection with framed payloads, and consider SSE over WebSocket for unidirectional updates.
- Decide whether the composition is per-connection or shared based on whether the data is user-specific.