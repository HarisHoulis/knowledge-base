---
domain: ai-workflows
subdomain: browser-automation
concept: bun-webview-json-api
title: A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView
sources:
  - title: "A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView"
    url: "https://simonwillison.net/2026/Aug/20/bun-webview-json-api/"
    author: "Simon Willison"
    date: "2026-08-20"
  - title: "Bun v1.4"
    url: "https://bun.com/blog/bun-v1.4"
    author: "Bun"
    date: "2026-08-20"
---

# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

Bun 1.4, the first stable version after its Rust rewrite, introduced a wide range of new features, including Bun.WebView, which provides first-class browser automation support via macOS WebKit or CDP-controlled Chromium. The release notes emphasize increases in Node.js test suite compatibility, bug fixes, performance improvements, and new APIs such as Bun.Image, Bun.markdown, Bun.cron, and Bun.Terminal. The Rust rewrite itself was downplayed in the announcement (source: https://simonwillison.net/2026/Aug/20/bun-webview-json-api/).

Simon Willison used Claude Code to prototype a JSON API inspired by his shot-scraper javascript tool, allowing users to load web pages and execute JavaScript against them. The TypeScript server implementation runs a full Chrome instance and requires roughly 192MB-256MB of RAM in a container, as tested using cgroups. This demonstrates the feasibility of building lightweight browser-automation services on top of Bun.WebView.

- Bun 1.4 adds Bun.WebView for browser automation, supporting macOS WebKit and Chromium via CDP.
- The release includes 2,900+ bug fixes, 1,517 new Node.js test suite tests, and performance improvements.
- A prototype JSON API was built with Claude Code, enabling JavaScript execution on loaded web pages.
- The service requires 192MB-256MB RAM for complex pages, making it suitable for containerized deployment.