---
domain: android-kotlin
subdomain: http4k
concept: test-driven-http-server
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Duncan"
    date: "2021-11-24"
---

# Kotlin and http4k - List Stock in a Browser

This video demonstrates building a web-based stock list viewer using Kotlin and the http4k library. The team previously implemented command-line printing of stock loaded from a disk file; the customer now wants to view the stock list in a browser, which requires exposing the stock data over HTTP. The implementation is driven by test-driven development: the author first writes a test that creates a server for the stock list, builds a client to connect to it, and expects a response body when requesting the root path. This high-level test intentionally avoids assuming http4k-specific details, naturally guiding the design of minimal server and client abstractions. Dependencies are added to build.gradle to pull in http4k, and the transcript cuts off as coding begins, emphasizing an incremental, test-first workflow that builds customer confidence through working features.

- The customer wants to view the stock list in a browser, requiring an HTTP server.
- http4k is the chosen Kotlin HTTP library, added via build.gradle dependencies.
- Tests are written first to define server and client behavior at a high level.
- The test asserts that a request to the root returns a response body.
- Development follows a test-driven, incremental approach with visible progress.