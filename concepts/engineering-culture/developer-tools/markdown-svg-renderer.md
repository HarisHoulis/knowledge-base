---
domain: engineering-culture
subdomain: developer-tools
concept: markdown-svg-renderer
title: Markdown SVG upgrades
sources:
  - title: "Markdown SVG upgrades"
    url: "https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/"
    author: "Simon Willison"
    date: "2026-08-16"
---

# Markdown SVG upgrades

Simon Willison's markdown-svg-renderer is a browser-based tool that renders Markdown containing SVG documents. It accepts pasted Markdown or a URL to a CORS-friendly document or GitHub Gist, producing a bookmarkable page with rendered SVG, including animated SVGs. The tool adds tabs for exporting the SVG as PNG, JPEG, or MP4, addressing the need to share SVG content on platforms that don't support it directly. The MP4 export is a new feature that detects SVG animations, estimates loop duration, renders frames, and uses ffmpeg.wasm (30+MB) to compile them into video entirely in the browser.

- Markdown with embedded SVG is rendered live in the browser, with optional URL input via Gist or CORS-friendly URLs for bookmarkable pages.
- Tabs allow downloading rendered SVG as PNG or JPEG, useful for platforms without SVG support.
- A new MP4 tab analyzes SVG animations, guesses loop length, renders frames, and uses ffmpeg.wasm to create a video in-browser.
- The tool is tailored to sharing animated SVGs, solving the author's need to share pelican-riding-bicycle drawings.