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

In this episode, the team continues building a Gilded Rose inventory system. The customer requested the ability to view the stock list in a browser instead of the command line, so they decide to add an HTTP interface using the http4k library in Kotlin (source: https://www.youtube.com/watch?v=1XtSVSmu3BI). The work is test-driven: they begin by writing a test that creates a server from the stock list, then a client that requests the root URL and expects an HTML response body. This test drives the design of server and client abstractions that will integrate with http4k (source: https://www.youtube.com/watch?v=1XtSVSmu3BI). The team acknowledges that the immediate goal is only viewing the list, but they anticipate future requirements like automatically updating item quantities. The current milestone is a stepping stone toward a more interactive system (source: https://www.youtube.com/watch?v=1XtSVSmu3BI).

- Use http4k to expose the stock list as an HTTP endpoint at the root URL.
- Start with a test that expects an HTML body from a client request.
- Build the server around the existing stock list data structure.
- Browser viewing is a prerequisite for future automatic quantity updates.
- Test-driven development drives the design of server and client abstractions.