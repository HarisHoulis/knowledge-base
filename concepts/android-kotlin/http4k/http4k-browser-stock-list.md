---
domain: android-kotlin
subdomain: http4k
concept: http4k-browser-stock-list
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this session, Duncan continues work on the Gilded Rose Inc. project, focusing on a new customer requirement: viewing the stock list in a browser instead of the command line. The customer previously saw value in printing stock and loading it from a file, but now wants a more accessible interface, with future plans for automatic updates. The team decides to use the http4k library to build an HTTP server that serves the stock list as HTML.

Following test-driven development, Duncan starts by writing a test that expects a response from the server root. He creates a conceptual server and client, with the client making a request to the root and the response body containing HTML. Initially, the test expects a blank HTML document, which serves as a minimal first step. The approach is exploratory, roughing out the interfaces before integrating with http4k (Duncan, 2021).

- Customer wants to view stock list in browser, moving away from command-line printing.
- The team chooses http4k as the library for building the HTTP server.
- Test-driven development: write a test that expects an HTML response from the server root.
- The initial test targets an empty HTML document to establish the server-client interaction.
- Future stories include automatic updates of stock qualities.