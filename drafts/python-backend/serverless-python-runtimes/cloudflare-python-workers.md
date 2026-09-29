---
domain: python-backend
subdomain: serverless-python-runtimes
concept: cloudflare-python-workers
title: Cloudflare Python Workers reach general availability
sources:
  - title: "Cloudflare Python Workers are now generally available"
    url: "https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/"
    author: "Simon Willison"
    date: "2026-09-21"
---

# Cloudflare Python Workers reach general availability

Cloudflare's Python Workers are now generally available. The implementation compiles Python to WebAssembly via Pyodide and runs it inside Cloudflare's V8-based `workerd` runtime (Simon Willison, 2026).

The WebAssembly VM imposes limits, most notably that both `multiprocessing` and `threading` are non-functional, as documented in Cloudflare's stdlib reference (Simon Willison, 2026).

Local development is handled by the `pywrangler` CLI tool, packaged on PyPI as `workers-py`. It runs a full local simulation of the stack, executing code with Pyodide in WebAssembly in V8 inside a 123MB `workerd` binary (which in the author's case landed in `node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd`) (Simon Willison, 2026).

The release is framed as a significant investment by Cloudflare in the wider Python ecosystem: the announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham, with Gyeongjae and Hood both being Pyodide core maintainers (Simon Willison, 2026).

- Python Workers compile Python to WebAssembly via Pyodide and execute it in Cloudflare's V8-based `workerd` runtime.
- `multiprocessing` and `threading` do not work in the WebAssembly VM.
- The `pywrangler` CLI (PyPI package `workers-py`) provides a full local simulation of the stack, including Pyodide-in-Wasm-in-V8 inside a 123MB `workerd` binary.
- The release is credited to Pyodide core maintainers Gyeongjae Choi and Hood Chatham, alongside Dominik Picheta, signalling Cloudflare's investment in the Python ecosystem.