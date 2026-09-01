---
domain: ai-workflows
subdomain: ai-tooling
concept: codex-bundles-libreoffice
title: Codex bundles LibreOffice
sources:
  - title: "Codex bundles LibreOffice"
    url: "https://simonwillison.net/2026/Sep/1/codex-libreoffice/"
    author: "Simon Willison"
    date: "2026-09-01"
---

# Codex bundles LibreOffice

Simon Willison discovered that the OpenAI Codex desktop app (now rebranded as ChatGPT) stores a large runtime bundle in the user's cache folder. Specifically, the `codex-primary-runtime` directory under `~/.cache/codex-runtimes/` contains approximately 1.7GB of dependencies, including a full Python installation, a full Node.js installation, and native binaries for Poppler, git, and the LibreOffice open source office suite (Willison, 2026).

- The Codex desktop app caches a 1.7GB runtime bundle in ~/.cache/codex-runtimes/codex-primary-runtime.
- The bundle includes full Python and Node.js installations, plus native binaries for Poppler, git, and LibreOffice.
- A plugins/documents folder contains skills that tell Codex how to locate and use these bundled binaries.
- This illustrates the heavy dependency footprint embedded in modern AI coding assistants.