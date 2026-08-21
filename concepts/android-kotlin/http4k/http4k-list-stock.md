---
domain: android-kotlin
subdomain: http4k
concept: http4k-list-stock
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this episode, Duncan continues building the Gilded Rose inventory system by adding a new feature: viewing the stock list in a browser instead of the command line. The approach is test-driven, starting with a test that expects a server to return an HTML response when a client requests the root endpoint. The team plans to use the http4k library to handle HTTP communication, adding necessary dependencies to build.gradle.

The session emphasizes incremental development and keeping the customer confident by delivering small, visible improvements. The immediate goal is to display stock in a browser, while future stories will involve automatic updates to stock qualities. The transcript shows the early stages of designing the server and client abstractions, with the test guiding the creation of these components.

- The new story is to view the stock list in a browser, moving away from command-line output.
- http4k is selected as the HTTP library, and dependencies will be added to build.gradle.
- Development is test-driven: a test is written first to describe the desired server and client behavior.
- The test expects a response body containing HTML when requesting the root URL.
- The work continues the Gilded Rose project, with emphasis on quick, customer-visible progress.