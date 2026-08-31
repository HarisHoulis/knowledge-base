---
domain: android-kotlin
subdomain: server-side-rendering
concept: molecule-html-streaming
title: Compose & kotlinx.html
sources:
  - title: "Compose & kotlinx.html"
    url: "https://jakewharton.com/compose-and-kotlinx-html/"
    author: "Jake Wharton"
---

# Compose & kotlinx.html

The article describes an approach to server-side rendering dynamic HTML fragments using Kotlin, kotlinx.html, and Molecule. The author uses Ktor to serve static HTML with a reusable layout and user list, but notes that the content becomes stale after a short time. Instead of adopting a full client-side framework like Compose for HTML, they use Molecule on the JVM to manage state and render HTML fragments as strings, then stream these strings over a WebSocket connection [1]. The client receives the fragments and uses Idiomorph.morph to patch the DOM, preserving interactive elements. The author emphasizes this is suitable for low-traffic admin pages and discusses potential improvements for real-world usage: multiplexing multiple updates over a single connection, switching to SSE for unidirectional framing, and deciding whether composition should be per-connection or shared. The simplicity of the implementation is highlighted, with a helper to encapsulate static and dynamic routes as optional [1].

- kotlinx.html can render server-side HTML fragments, but static pages become stale; Molecule can stream reactive HTML updates over WebSocket.
- Idiomorph.morph patches the DOM, preserving form fields and interactive elements when updating content.
- For production scale, consider SSE instead of WebSocket for unidirectional payloads, and multiplex updates with an envelope targeting HTML IDs.
- Composition can run per-connection or be shared, depending on whether the data is connection-specific.
- The total additional code is minimal, making it an attractive alternative to client-side frameworks for simple admin pages.