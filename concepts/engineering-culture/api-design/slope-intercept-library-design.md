---
domain: engineering-culture
subdomain: api-design
concept: slope-intercept-library-design
title: Slope-intercept library design
sources:
  - title: "Slope-intercept library design"
    url: "https://jakewharton.com/slope-intercept-library-design/"
    author: "Jake Wharton"
---

# Slope-intercept library design

In this article, Jake Wharton introduces a mental model for evaluating and designing software libraries based on the slope-intercept equation y=mx+b. The intercept (b) represents the initial cost of learning and setup required to adopt a library, while the slope (m) represents how the library's complexity increases as the user's needs grow over time. He applies this model to three Android libraries: Picasso, Retrofit, and Dagger, showing that Picasso has a low intercept but steep slope, Dagger has a high intercept but shallow slope, and Retrofit sits somewhere in between. Wharton argues that designers should consciously decide where to place complexity—either front-loaded or spread out—and can use multiple API layers (simple to low-level) to serve a broader range of users without forcing a single steep complexity curve.

- A library's 'intercept' is the upfront cost of setup and learning; its 'slope' is how complexity increases with continued use.
- Picasso optimized for a low intercept but later suffers from a steep slope; Dagger has a very high intercept but a very shallow slope; Retrofit balances both.
- Designers should ask questions about where parameters are specified (global vs local), whether they can be grouped, and how defaults work to shape the slope and intercept.
- Layering multiple APIs—declarative, imperative, and low-level—allows a library to approximate a low intercept and low slope across different use cases.