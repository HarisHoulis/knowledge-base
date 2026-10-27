---
domain: web-dev
subdomain: browser-automation
concept: headless-webview-scripting
title: webframe: Evaluated as a Scraper and a Sandbox
sources:
  - title: "webframe: evaluated as a scraper and a sandbox"
    url: "https://simonwillison.net/2026/Oct/26/webframe-evaluation/"
    author: "Simon Willison"
    date: "2026-10-26"
---

# webframe: Evaluated as a Scraper and a Sandbox

webframe is a small Go project by Jeff Lindsay that lets you "run a web page like a program": you point it at a URL or file, it executes it in a hidden headless web view, and it outputs console.log() to standard output and exceptions to standard error. It is built on the glaze library, which exposes the system browser (WKWebView on macOS, WebKitGTK on Linux, WebView2 on Windows), so it does not bundle its own browser engine.

Simon Willison notes that it resembles his own shot-scraper javascript tool, but in a much smaller package that avoids a Playwright dependency. To assess it, he had Claude Opus 5.5 explore the repository, run it, build exploratory prototypes, and evaluate it both as a sandboxing tool and as a web-scraping tool using the patterns encouraged by shot-scraper's JavaScript command.

The evaluation is published as a research report in the simonw/research repository.

- webframe runs a web page like a program, piping console.log() to stdout and exceptions to stderr
- It uses the system browser via the glaze library rather than bundling a browser engine
- It is comparable to shot-scraper javascript but far smaller and without a Playwright dependency
- The evaluation covered both sandboxing and scraping use cases, with prototypes built by an AI agent