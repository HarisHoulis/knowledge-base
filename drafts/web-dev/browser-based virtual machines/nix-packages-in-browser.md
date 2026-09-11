---
domain: web-dev
subdomain: browser-based virtual machines
concept: nix-packages-in-browser
title: Any Nix Package, Live in Your Browser via qemu-wasm
sources:
  - title: "Any Nix package, live in your browser"
    url: "https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser"
    author: "Farid Zakaria"
    date: "2026-09-04"
  - title: "Review a pull request by booting it"
    url: "https://fzakaria.com/2026/09/09/review-a-pull-request-by-booting-it"
    author: "Farid Zakaria"
    date: "2026-09-09"
  - title: "Any Nix package, live in your browser"
    url: "https://simonwillison.net/2026/Sep/10/trynix/"
    author: "Simon Willison"
    date: "2026-09-10"
---

# Any Nix Package, Live in Your Browser via qemu-wasm

trynix.dev runs an x86_64 Linux virtual machine entirely inside the browser using qemu-wasm, a WebAssembly build of QEMU. That VM can be booted with any Nix package from the past 13 years, and the packages are URL addressable — for example, navigating to trynix.dev/?pkg=python3%403.6.2 and clicking "Load" yields an interactive shell against a VM running Python 3.6.2 from 2017 (fzakaria.com, via simonwillison.net).

The approach is being extended into developer workflows. Farid Zakaria's trynix-preview is a GitHub Action that comments a link on a pull request, letting reviewers boot the PR's build in the browser through trynix.dev. The pitch is "No servers, just browsers" — no server-side infrastructure is needed for a reviewer to interact with a real, booted environment (fzakaria.com, simonwillison.net).

Simon Willison's link post frames this as one of several neat things being built on top of the qemu-wasm foundation, and ties it to code review, Linux, WebAssembly, and GitHub Actions as the relevant topics (simonwillison.net).

- trynix.dev uses qemu-wasm to run an x86_64 Linux VM entirely in the browser via WebAssembly.
- The VM can boot any Nix package from the past 13 years, addressed by URL (e.g. ?pkg=python3%403.6.2).
- Clicking "Load" with that URL gives an interactive shell against Python 3.6.2 from 2017.
- trynix-preview is a GitHub Action that comments a link on a pull request so reviewers can boot the PR's build in the browser.
- The design requires no servers — "No servers, just browsers."