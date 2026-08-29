---
domain: android-kotlin
subdomain: server-side-kotlin
concept: isomorphic-html-rendering
title: Compose & kotlinx.html
sources:
  - title: "Compose & kotlinx.html"
    url: "https://jakewharton.com/compose-and-kotlinx-html/"
    author: "Jake Wharton"
---

# Compose & kotlinx.html

Jake Wharton discusses rendering dynamic HTML fragments on the server using kotlinx.html with Ktor, and tackling the problem of stale content without adopting a full client-side framework. He proposes using Cash App's Molecule library to run Compose-style state collection on the JVM, producing HTML strings that can be streamed to the client over a WebSocket. Initial HTML includes a script that receives the updated fragments and patches the DOM using Idiomorph, preserving interactive element state.

The article explores practical tradeoffs for scaling this approach. For real-world usage, a single long-lived connection is preferable, with event framing to target specific DOM elements. Server-sent events (SSE) over HTTP/2 are suggested as a better fit than WebSockets due to multiplexing and built-in framing. The decision of whether the composition runs per-connection or is shared depends on the data's relationship to the user, and a helper can encapsulate static and dynamic routes.

- kotlinx.html can be combined with Ktor to render server-side HTML fragments.
- Molecule enables Compose-style state collection on the JVM to produce dynamic HTML strings.
- Streaming HTML fragments over WebSocket, then patching the DOM with Idiomorph, avoids full page reloads while keeping static HTML delivery.
- For production, consider SSE over WebSockets and framing payloads with target element IDs.
- The approach is ideal for low-traffic admin pages; for larger scale, evaluate connection sharing and multiplexing.