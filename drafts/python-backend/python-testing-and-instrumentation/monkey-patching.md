---
domain: python-backend
subdomain: python-testing-and-instrumentation
concept: monkey-patching
title: Don't Sleep on Wrapture: A Monkey Patching Toolkit for Python
sources:
  - title: "Don't sleep on wrapture"
    url: "https://simonwillison.net/2026/Sep/11/wrapture/"
    author: "Simon Willison"
    date: "2026-09-11"
  - title: "wrapture documentation"
    url: "https://wrapture.readthedocs.io/"
    author: "Graham Dumpleton"
  - title: "wrapture-workshops"
    url: "https://github.com/GrahamDumpleton/wrapture-workshops"
    author: "Graham Dumpleton"
---

# Don't Sleep on Wrapture: A Monkey Patching Toolkit for Python

Simon Willison highlights wrapture, Graham Dumpleton's new monkey patching package for Python, as a tool that is "shaping up to be an indispensable tool for Python developers" — and notes his surprise at the lack of buzz around it (simonwillison.net). Wrapture targets monkey patching, the practice of replacing or wrapping attributes at runtime, which is commonly used for testing, instrumentation and observability.

Since the initial release on August 31st, Dumpleton has been publishing new tutorials for the package "almost daily" (simonwillison.net). The covered surface is broad, spanning standard library modules such as `unittest.mock`, `http.client`, `sqlite3`, `urllib.request`, `xmlrpc.client` and `xmlrpc.server`, plus popular third-party frameworks and libraries including `aiohttp`, `django`, `fastapi`, `flask`, `grpc`, `httpx`, `jinja2`, `requests`, `sqlalchemy`, `starlette`, `urllib3`, `uvicorn`, `werkzeug.serving` and `wsgiref.simple_server` (simonwillison.net).

Dumpleton has also published a set of interactive workshops for wrapture, implemented as JupyterLab notebooks (simonwillison.net). Willison notes wrapture is still alpha software but already very usable, particularly because it can be configured and tried out through a TOML file without modifying any Python code at all (simonwillison.net).

His overall assessment is that wrapture feels like a Swiss Army Knife package that, once mastered, will provide value against a wide range of problems for years (simonwillison.net).

- wrapture is Graham Dumpleton's new Python monkey patching package, described by Simon Willison as potentially indispensable and under-discussed.
- Tutorials have appeared almost daily since the August 31st initial release, covering stdlib modules and frameworks like django, fastapi, flask, httpx, requests, sqlalchemy, starlette and grpc.
- Interactive JupyterLab-notebook workshops accompany the package.
- It remains alpha software but is already usable, and can be configured via a TOML file without modifying any Python code.