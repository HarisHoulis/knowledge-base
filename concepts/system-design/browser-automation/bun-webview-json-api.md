---
domain: system-design
subdomain: browser-automation
concept: bun-webview-json-api
title: A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView
sources:
  - title: "A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView"
    url: "https://simonwillison.net/2026/Aug/20/bun-webview-json-api/"
    author: "Simon Willison"
    date: "2026-08-20"
---

# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

The article covers the release of Bun 1.4, the first stable version after a Rust rewrite. The release notes downplayed the rewrite and instead emphasized new features, such as Bun.WebView, and claimed over 2,900 bug fixes and a significant jump in Node.js compatibility (source).

Bun.WebView is highlighted as the most interesting addition, providing first-class browser automation through macOS WebKit or a Chromium process via the Chrome DevTools Protocol (CDP). This enables the creation of tools like the prototype JSON API described in the article.

The prototype, built with Claude Code for web, offers a web API that loads a page and executes JavaScript against it, similar to the shot-scraper javascript CLI tool. Testing showed that running a full Chrome instance against complex web pages requires a container with 192MB-256MB of RAM (source).

- Bun 1.4 is the first stable version since the Rust rewrite, adding many features and fixing 2,900+ issues.
- Bun.WebView enables browser automation via WebKit or Chromium CDP.
- A shot-scraper-style JSON API was prototyped to load web pages and execute JavaScript.
- The prototype requires 192-256MB RAM to run full Chrome on complex pages.