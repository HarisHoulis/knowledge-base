---
domain: android-kotlin
subdomain: http4k
concept: http4k-stock-list-browser
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this episode, the team continues working on the Gilded Rose inventory system, shifting from a command-line interface to a web browser view. The customer wants to view the stock list in a browser to make printing easier, which requires introducing an HTTP server. The presenter chooses the http4k library for Kotlin, adding dependencies to build.gradle to get started. The approach is strictly test-driven: they write a failing test that defines the desired behavior—requesting the root URL via a client should return a response with a body. This test drives the creation of both a server and a client wrapper around http4k. The transcript captures the initial steps of this design, showing how the test shapes the API before implementation details are filled in (source: Kotlin and http4k - List Stock in a Browser).

- Customer stories drive incremental development: from file loading to command-line printing to browser viewing.
- http4k is a Kotlin library used to build HTTP servers and clients in a functional style.
- Test-driven development guides creation of the API: the test defines a client making a request to the root and expecting a response body.
- The team abstracts http4k behind custom types (server, client) rather than coupling tests to the library directly.
- The next anticipated feature is automatic updating of stock qualities, indicating the project's iterative nature.