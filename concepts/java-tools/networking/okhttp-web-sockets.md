---
domain: java-tools
subdomain: networking
concept: okhttp-web-sockets
title: Web Sockets now shipping in OkHttp 3.5!
sources:
  - title: "Web Sockets now shipping in OkHttp 3.5!"
    url: "https://developer.squareup.com/blog/web-sockets-now-shipping-in-okhttp-3-5"
---

# Web Sockets now shipping in OkHttp 3.5!

OkHttp 3.5 introduces native, stable support for Web Sockets, enabling fully bi-directional streaming of messages between client and server. Unlike HTTP's request/response model, Web Sockets allow either peer to send messages at any time. The API is straightforward: pass a Request and a WebSocketListener to `newWebSocket()`, then send messages with `send(String)` or `send(ByteString)`. OkHttp manages its own sending thread, so `send` can be called from any thread, including Android's main thread. Received messages are delivered to the listener's `onMessage` callback, with additional callbacks for lifecycle events (source: https://developer.squareup.com/blog/web-sockets-now-shipping-in-okhttp-3-5).

- OkHttp 3.5 adds a stable WebSocket API, replacing the earlier experimental `okhttp-ws` artifact.
- WebSockets provide fully bi-directional streaming between client and server.
- The API supports text and binary messages via `send(String)` and `send(ByteString)`.
- Send operations are thread-safe and may be called from Android's main thread.
- The library's WebSocket implementation had origins in an internal PonyDebugger-style tool, and matured over three years.