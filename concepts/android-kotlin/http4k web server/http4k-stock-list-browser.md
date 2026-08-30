---
domain: android-kotlin
subdomain: http4k web server
concept: http4k-stock-list-browser
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this episode, Duncan continues building the Gilded Rose inventory system. After successfully printing stock to the command line, the customer requests to view the stock list in a browser to make printing easier. The team adds a new backlog story to implement an HTTP server that serves the stock list as HTML, while anticipating a future story for automatic updates (Pairing with Duncan, 2021).

Following test-driven development, Duncan starts by writing a test for the browser listing. The test creates a server from a stock list, builds a client that knows how to connect to the server, makes a request to the root path, and expects a response body with HTML. The types are not yet known, so the test guides the implementation. They also add http4k dependencies to build.gradle to support the HTTP functionality (Pairing with Duncan, 2021).

The episode emphasizes delivering small increments to build customer confidence. The design wraps http4k, with the server constructed from the stock list and a client to interact with it. Later they plan to expand the HTML and eventually handle updating stock quantities, but the immediate goal is to return a blank HTML document from the server (Pairing with Duncan, 2021).

- The customer wants to view the stock list in a browser, moving from command-line printing to an HTML page.
- Development is test-driven: a test is written first to define expected behavior for the server and client.
- http4k dependencies are added to build.gradle to enable HTTP server and client capabilities.
- The design involves a server built from the stock list, a client that can request the root path, and a response body containing HTML.
- The immediate milestone is a simple HTML response, with future plans for automatic quantity updates.