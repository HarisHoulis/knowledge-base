---
domain: android-kotlin
subdomain: kotlin-web-development
concept: http4k-basic-server
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this video, Duncan, the chief programmer at Gilded Rose Inc, continues developing a stock management system. The focus is on implementing a new user story to view the stock list in a browser, as the customer finds the command line difficult. The approach is test-driven development using the http4k library for Kotlin. The session begins by adding http4k dependencies to the build.gradle file, then writing a test that simulates a client connecting to a server and requesting the root endpoint, expecting an HTML response body.

- Add http4k dependencies to build.gradle to enable HTTP server functionality.
- Write a test first that creates a server from the stock list and a client to make requests.
- The client's request to the root path should return a response with a body.
- The test is a placeholder to rough out the design, and will be refined as http4k is integrated.