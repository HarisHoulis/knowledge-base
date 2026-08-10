---
domain: system-design
subdomain: http4k
concept: http4k-browser-listing
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

In this episode, Duncan continues developing the Gilded Rose stock system. After delivering the ability to load and print stock, the customer requests viewing the stock list in a browser. Duncan plans to use the http4k library to add an HTTP interface. Following test-driven development, he starts by sketching a test: create some stock, instantiate a server around the stock list, build a client to connect to the server, and make a request to the root. The expected result is an HTML response body. This rough test is meant to explore the types needed, deferring HTTP specifics. Duncan notes that the design is not final and may change. He also mentions that the customer wants the next feature to automatically update item qualities over time, indicating that the simple file-based workflow will get more complex.

- Use http4k to create an HTTP server for the stock list.
- Start with a failing test that defines the desired client-server interaction.
- The test expects the server to return an HTML body at the root path.
- The design is intentionally rough and will be refined as implementation progresses.
- Future work includes automatic updates of stock qualities.