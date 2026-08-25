---
domain: android-kotlin
subdomain: http4k
concept: http4k-basic-server
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24"
---

# Kotlin and http4k - List Stock in a Browser

Duncan, the chief programmer at Gilded Rose Inc, continues building a stock management application. After previous stories successfully implemented printing stock and loading from a file, the customer now wants to view the stock list in a browser, as the command line is difficult to print. This episode focuses on the 'view stock listing in browser' story, using the http4k library to create a simple HTTP server.

The approach is test-driven: Duncan starts by writing a test that expects a server to return a blank HTML document for the root path. He adds http4k dependencies to build.gradle to pull in the necessary HTTP capabilities. The test involves creating a server on the stock list and a client that makes a request, then asserts the response body. This rough sketch guides the implementation and will later be expanded.

The customer also wants automatic updates in the future, but for now the focus is purely on viewing stock in a browser. This work marks a transition from command-line interactions to a web-based interface, building confidence with the customer through incremental delivery.

- Customer requested browser-based stock viewing; command-line printing is difficult.
- Use http4k library to build an HTTP server in Kotlin.
- Start with TDD: write a test expecting a blank HTML response from the server root.
- Add http4k dependencies to build.gradle before implementation.
- Future story includes automatic stock updates via the browser interface.