---
domain: android-kotlin
subdomain: picasso-image-loading
concept: request-replaying
title: Hello Picasso 2.3
sources:
  - title: "Hello Picasso 2.3"
    url: "https://developer.squareup.com/blog/hello-picasso-2-3"
    author: "D. Koutsogiorgas and Jake Wharton"
---

# Hello Picasso 2.3

Picasso 2.3 introduces request replaying, a feature that allows the Dispatcher to track failed image requests and automatically retry them when the network becomes available again. This is especially useful for apps that rely on images such as static maps, improving the user experience without requiring manual reloads. The feature works out of the box and also applies to widgets and notifications via RemoteViews.

- Request replaying automatically retries failed image requests when network connectivity is restored, with no extra code required.
- Picasso's Dispatcher, introduced in 2.0, offloads coordination from the main thread and batches completed requests to the main thread.
- New `into(remoteViews, viewId, ...)` overloads support loading images into widgets and notifications.
- Logging can be enabled with `setLoggingEnabled(true)` and provides per-request IDs and timing metrics, but is discouraged even in development builds due to performance overhead.