---
domain: android-kotlin
subdomain: http4k-web
concept: http4k-list-stock-browser
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this video, Duncan continues work on the Gilded Rose Inc. project, addressing a new customer story: viewing the stock list in a browser instead of the command line. The goal is to build an HTTP server using the http4k library, adding dependencies to build.gradle and creating a test that verifies the root endpoint returns HTML. The approach is test-driven: starting with a test that defines a server and client, making a request to the root, and asserting the response body contains expected HTML (Pairing with Duncan, 2021).

- The customer story shifts from command-line printing to browser-based viewing.
- http4k is introduced as the HTTP library for Kotlin.
- A test-first approach drives creation of a server and client.
- The root endpoint ('/') is intended to list stock as HTML.
- The implementation will wrap http4k with custom abstractions for the stock list.