---
domain: android-kotlin
subdomain: http4k
concept: list-stock-in-browser
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this video, Duncan continues working on the Gilded Rose Inc. project. The customer asks for the ability to view the stock list in a browser instead of the command line. Duncan plans to use the http4k library for HTTP handling and follows a test-driven development approach, starting with a test that requests the root URL and expects an HTML response body (source).

- Use http4k to build an HTTP server and client in Kotlin.
- Write tests first to drive development of the server endpoint.
- Expose the stock list at the root URL of the web server.
- Abstract server and client interactions to make testing easier.