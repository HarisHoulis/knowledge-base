---
domain: web-dev
subdomain: browser-polyfills
concept: polyfill-service
title: Polyfill as needed with polyfill-service
sources:
  - title: "Polyfill as needed with polyfill-service"
    url: "https://kentcdodds.com/blog/polyfill-as-needed-with-polyfill-service"
    author: "Kent C. Dodds"
    date: "2018-08-06"
---

# Polyfill as needed with polyfill-service

In a prior post, Kent C. Dodds described an IE10 white screen caused by missing polyfills and introduced the idea of serving polyfills only to browsers that need them. This post explains how he built a `/polyfill.js` endpoint using the open-source `polyfill-service` module that powers polyfill.io. The endpoint returns aggressively cached JavaScript containing only the polyfills required by the requesting browser. For IE10 the response is 60.2kb, while Chrome 67 returns basically empty. He argues that bundling polyfills into `bundle.js` makes modern-browser users pay a tax for the roughly 5% of users on older browsers, and that a separate cached file avoids unnecessary downloads and parse/compile/run costs.

He describes implementation on a NodeJS/Express server using KrakenJS for paypal.me. The route handler calls `polyfill.getPolyfillString`, sets content type and optionally immutable cache headers. User agent is taken from `req.headers['user-agent']`, with `ua` query string override and fallback to IE9; unknown UAs are configured to receive all polyfills via `unknown: 'polyfill'`. Features config uses `es2015`, `es2016`, `es2017`, `es2018`, and `default-3.6` rather than polyfilling everything, which would include large `Intl` language packs.

Caching is handled by server-rendering the polyfill URL with `v` version and encoded `ua` query strings, allowing the file to be cached forever and safely invalidated. He notes a fun issue with polyfill-service not playing nicely with Babel's class compilation. He hopes to build a more official PayPal polyfill service so teams can use modern JavaScript without taxing modern-browser users. A reader, Kevin Deisz, created an open source AWS Lambda service inspired by the post.

- Use the open-source `polyfill-service` module to serve only the polyfills a browser needs, instead of shipping all polyfills in `bundle.js`.
- A separate `/polyfill.js` file can be cached immutably; use versioned and UA-specific URLs so cache stays correct when browsers change.
- Configure user agent detection with a fallback and `unknown: 'polyfill'`; select specific feature sets like `es2015` through `es2018` and `default-3.6` rather than everything.
- Run the module in-house to avoid reliance on polyfill.io's lack of SLA, as done on a Node/Express (KrakenJS) server.