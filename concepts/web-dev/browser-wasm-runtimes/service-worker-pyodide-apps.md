---
domain: web-dev
subdomain: browser-wasm-runtimes
concept: service-worker-pyodide-apps
title: Running the full server-side Datasette Python app in the browser with service workers and Pyodide
sources:
  - title: "Running the full server-side Datasette Python app in the browser with service workers and Pyodide"
    url: "https://simonwillison.net/2026/Nov/17/datasette-lite/"
    author: "Simon Willison"
    date: "2026-11-17"
---

# Running the full server-side Datasette Python app in the browser with service workers and Pyodide

Datasette Lite is a port of the Datasette Python application that runs entirely in the browser using WebAssembly and Pyodide. A complete rewrite replaces the original 2022 hack—which simulated requests in a web worker and injected HTML via innerHTML, breaking any JavaScript-dependent features—with a Service Worker-based architecture that intercepts HTTP requests and serves them from client-side code, making it almost indistinguishable from the real server-side app (source).

The service worker is registered for the whole lite.datasette.io domain, and a parent page creates an iframe requesting Datasette URLs prefixed with a random per-tab session ID like /app/aa94e6851595/. That prefix lets the service worker route each tab's requests back to a dedicated Datasette instance running in a web worker, since Pyodide in a service worker cannot maintain state beyond roughly 30 seconds (source).

URL parameters make instances fully addressable: ?install= loads plugins from PyPI, &url= loads a CORS-enabled SQLite database, &metadata= loads a metadata.yml, &ref= pins a Datasette version, and &sqlite= installs a specific SQLite version from WebAssembly wheels in the datasette/pysqlite3-wasm-wheels repo (163 versions). The author uses these links to demonstrate bugs and fixes in Datasette issues, and argues the pattern generalizes to almost any Python app as a cheap preview environment, now that C/Rust extensions can be compiled to Pyodide-compatible WebAssembly and published to PyPI via PEP 783 (source).

- Service workers intercept requests and serve them from a web worker running Pyodide, replacing the old innerHTML-injection hack so JavaScript and CSS assets work.
- A per-tab /app/<session>/ URL prefix lets one shared service worker route to separate Datasette instances per tab.
- URL parameters (?install, &url, &metadata, &ref, &sqlite) make fully configured instances linkable for demos and bug reproductions.
- WebAssembly wheels for 163 SQLite versions enable testing Datasette against any SQLite release in the browser.
- The approach generalizes to almost any Python app as a cheap preview environment, though non-SQLite databases remain harder.