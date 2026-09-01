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

The video demonstrates continuing development of a stock-list application for Gilded Rose Inc., using Kotlin and the http4k library. The customer previously could load stock from a file and print it, but now wants to view the stock list in a browser because printing from the command line is difficult. The session focuses on adding an HTTP server to serve the stock list as HTML, following a test-driven development approach (Pairing with Duncan, 2021, https://www.youtube.com/watch?v=1XtSVSmu3BI).

The developer starts by adding http4k dependencies to build.gradle, then writes a functional test that creates some stock, builds a server wrapping the stock list, and uses a client to make a request to the root URL. The test expects the response body to be a blank HTML document initially, which will be expanded later. This test drives the creation of server and client abstractions on top of http4k (Pairing with Duncan, 2021, https://www.youtube.com/watch?v=1XtSVSmu3BI).

The episode also highlights the team's incremental delivery and customer confidence. They note that the customer now understands they can edit the stock list in a text editor, but the next stories will involve updating quantities automatically. The development style is test-first, with duplication from previous printing tests accepted temporarily because the tests are unlikely to live long (Pairing with Duncan, 2021, https://www.youtube.com/watch?v=1XtSVSmu3BI).

- Add http4k dependencies to build.gradle before implementing the HTTP server.
- Start with a test that creates stock, spins up a server, and makes a client request to the root.
- Expect a blank HTML response body initially, then expand to render the stock list.
- Use test-driven development and reuse similar test structures from printing tests, accepting duplication as temporary.
- The customer story is to view stock in a browser, with future stories for automatic quantity updates.