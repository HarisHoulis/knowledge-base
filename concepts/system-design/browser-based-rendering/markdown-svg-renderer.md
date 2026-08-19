---
domain: system-design
subdomain: browser-based-rendering
concept: markdown-svg-renderer
title: Markdown SVG upgrades
sources:
  - title: "Markdown SVG upgrades"
    url: "https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/"
    author: "Simon Willison"
    date: "2026-08-16"
---

# Markdown SVG upgrades

The article describes the evolution of a browser-based Markdown-to-SVG rendering tool. The tool accepts Markdown input via paste or URL (including GitHub Gists) and renders embedded SVG documents into a live, interactive page. A key addition is a tabbed interface that allows users to export the rendered SVG to PNG or JPEG directly in the browser, making it easier to share on platforms that do not support SVG natively (Willison, 2026).

The newest feature is an MP4 export tab, which detects whether the SVG contains animations, estimates the loop duration, renders numerous frames, and uses ffmpeg.wasm (a WebAssembly build of FFMPEG) to compile those frames into an MP4 video entirely client-side. This enables sharing animated SVG content on platforms that lack native SVG animation support. The tool also supports bookmarkable URLs that embed the source document URL, providing a persistent rendered view of any CORS-friendly Markdown file (Willison, 2026).

- The tool renders Markdown with embedded SVGs into live, interactive documents.
- SVG content can be exported to PNG and JPEG via browser-side tabs, avoiding platform SVG limitations.
- A new MP4 tab uses ffmpeg.wasm to convert animated SVGs to MP4 videos by analyzing animation timing and rendering frames in the browser.
- Supports loading Markdown from URLs or Gists, with bookmarkable hash-based URLs for sharing rendered views.