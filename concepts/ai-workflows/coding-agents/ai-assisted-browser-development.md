---
domain: ai-workflows
subdomain: coding-agents
concept: ai-assisted-browser-development
title: Ladybird's First Alpha Release and Its Heavy Use of Coding Agents
sources:
  - title: "Ladybird's first alpha release"
    url: "https://simonwillison.net/2026/Nov/23/ladybird/"
    author: "Simon Willison"
    date: "2026-11-23"
---

# Ladybird's First Alpha Release and Its Heavy Use of Coding Agents

Ladybird, an independent browser project with its own HTML parser, CSS engine, layout, JavaScript, and WebAssembly implementations, released its first alpha for macOS and Linux in November 2026, letting users install it without compiling. Simon Willison found it fast and lightweight, with most sites working; it runs tabs in separate processes and handled WebAssembly-heavy tools like an ffmpeg-based video compressor and a Pyodide REPL, though Datasette Lite failed due to an unimplemented service worker API (navigator.serviceWorker.startMessages), for which he filed an issue.

The project has leaned heavily on coding agents. In February 2026 Andreas Kling described porting parts of LibJS from C++ to 25,000 lines of Rust in two weeks using Claude Code and Codex. The October 2026 newsletter credits agents with a large jump in web-platform-tests passes—about 2.12 million to 2.18 million in five days—by pointing agents at WPT to fill in missing functionality, alongside a new JavaScript JIT and a Cranelift WebAssembly engine with a 7x JetStream 3 boost.

Kling frames the alpha as incomplete and insecure: some sites won't work, crashes happen, and the team explicitly invites security researchers to hack it. Willison says he won't use it for sensitive accounts like GitHub or Gmail but keeps it for anonymous browsing and testing, valuing a new entrant in the stagnant browser engine market.

- Ladybird's first alpha (macOS/Linux) ships its own HTML, CSS, layout, JS, and WebAssembly engines, using external HarfBuzz, Skia, ffmpeg, and SQLite.
- Coding agents drove major progress: a C++-to-Rust LibJS port and roughly 60,000 new web-platform-tests passes in October 2026.
- Tabs run in separate processes; most WebAssembly tools worked, but service worker support is incomplete (Datasette Lite failed).
- The team makes no security promises and invites researchers to hack it; Willison avoids using it for sensitive accounts.