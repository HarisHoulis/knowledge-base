---
domain: android-kotlin
subdomain: kotlin-web
concept: http4k-list-stock
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this episode, Duncan, the chief programmer at Gilded Rose Inc, continues developing a stock management system. The customer is happy with the ability to load stock from a file and print it, but now wants to view the stock list in a browser instead of the command line. To achieve this, the team decides to use the http4k library to build a web server.

Following test-driven development, they start by writing a test that specifies the desired behavior: a client should be able to request the root path from the server and receive an HTML body. This test introduces abstractions for the server and the client, which will wrap http4k. Initially, they plan to return a blank HTML document, with later expansion to display the actual stock items.

The team acknowledges some duplication with existing printing tests but decides to accept it for now to maintain momentum. They anticipate future stories, such as automatically updating stock qualities, but for this session they focus on the browser view. The rapid delivery reinforces the customer's confidence in the team's ability to understand the problem and make changes quickly.

- Use http4k to expose the stock list in a browser via HTTP.
- Start with a failing test that defines the expected response for the root endpoint.
- Introduce server and client abstractions to test the web layer cleanly.
- Accept temporary duplication to keep development moving.
- Deliver incrementally to build customer confidence.