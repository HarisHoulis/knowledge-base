---
domain: android-kotlin
subdomain: http4k
concept: http4k-browser-stock
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

The team continues building a stock management system for Gilded Rose Inc. The customer is happy with the ability to load and print stock from a file, but now wants to view the stock list in a browser because the command line is difficult to print. The goal is to implement the 'view stock listing in a browser' story using the http4k library to handle HTTP.

- Add http4k dependencies to build.gradle to enable HTTP server capabilities.
- Use test-driven development: start with a functional test for viewing stock in a browser.
- The test creates a server on the stock list, builds a client, and requests the root endpoint, expecting an HTML response body.
- Accept temporary duplication with existing tests to keep focus on the new HTTP functionality.