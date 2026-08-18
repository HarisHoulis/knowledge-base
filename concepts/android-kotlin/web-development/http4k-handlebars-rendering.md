---
domain: android-kotlin
subdomain: web-development
concept: http4k-handlebars-rendering
title: Kotlin and http4k - List Stock in a Browser
sources:
  - title: "Kotlin and http4k - List Stock in a Browser"
    url: "https://www.youtube.com/watch?v=1XtSVSmu3BI"
    author: "Pairing with Duncan"
    date: "2021-11-24T15:54:21+00:00"
---

# Kotlin and http4k - List Stock in a Browser

This video is the third part of an Extreme Programming (XP) series where the Gilded Rose stock control system is incrementally implemented in Kotlin. The customer requests the ability to view the stock list in a browser to facilitate printing, leading to a focused coding session that integrates web capabilities into the existing application [1]. The session demonstrates a practical, step-by-step approach to adding an HTTP server and templating without overcomplicating the architecture.

The core technical addition is the use of http4k, a lightweight HTTP toolkit for Kotlin, combined with Handlebars for server-side HTML templating. The developers load stock data from the filesystem and render it into an HTML page using a Handlebars template, effectively exposing the data through a browser interface. This approach highlights how http4k's functional design and Handlebars' simplicity can be combined to create a small but functional web view within an existing codebase [1].

The session also emphasizes dense, deliberate coding practices and incremental feature development, typical of XP methodologies. The presenters mention that viewers who enjoy this content would likely benefit from the book "Java to Kotlin, A Refactoring Guidebook," which provides further guidance on refactoring Java applications to Kotlin [1]. Overall, the video serves as a hands-on example of adding web rendering to a Kotlin project while maintaining a clean, testable structure.

- http4k provides a lightweight and functional way to add HTTP endpoints to a Kotlin application.
- Handlebars templates allow clean separation of HTML rendering from business logic.
- The session demonstrates an incremental, XP-style approach to feature development.
- Rendering filesystem-loaded data into a browser view is a common need for internal tools and printable lists.
- The book 'Java to Kotlin' is recommended for further refactoring insights.