---
domain: android-kotlin
subdomain: server-side-rendering
concept: compose-kotlinx-html
title: Compose & kotlinx.html
sources:
  - title: "Compose & kotlinx.html"
    url: "https://jakewharton.com/compose-and-kotlinx-html/"
    author: "Jake Wharton"
---

# Compose & kotlinx.html

Jake Wharton describes a server-side rendering approach for low-traffic admin pages using Kotlin, Kotlinx.html, and Molecule. Instead of adopting a client-side framework like Compose for HTML, he reuses existing kotlinx.html rendering functions on the server to produce HTML fragments as strings. Molecule manages a single piece of state over time, converting a StateFlow of data into a StateFlow of HTML strings that can be streamed to the client (Wharton, "Compose & kotlinx.html", https://jakewharton.com/compose-and-kotlinx-html/).

On the client, a WebSocket receives these HTML fragments and updates the DOM using Idiomorph, which patches only the changed parts, preserving form fields and interactive elements. While this works for his use case, Wharton notes scalability considerations: multiplexing updates on a single connection, using SSE instead of WebSockets for unidirectional payloads, and deciding whether to run composition per-connection or shared (Wharton, "Compose & kotlinx.html", https://jakewharton.com/compose-and-kotlinx-html/).

- Molecule enables Compose-like state management on the JVM to render kotlinx.html fragments as strings.
- HTML fragments can be streamed to the client over WebSocket and applied via Idiomorph for DOM patching.
- This approach avoids abandoning static HTML for server-rendered pages.
- For production-scale use, consider SSE with multiplexed updates and careful connection handling.