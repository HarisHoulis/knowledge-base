---
domain: python-backend
subdomain: datasette-plugins
concept: datasette-ports
title: datasette-ports 0.4
sources:
  - title: "datasette-ports 0.4"
    url: "https://simonwillison.net/2026/Oct/12/datasette-ports/"
    date: "2026-10-12"
---

# datasette-ports 0.4

datasette-ports 0.4 is a release of a plugin that detects and lists all Datasette instances running on the current machine. The update makes the plugin compatible with the latest version of Datasette and adds display of the detected PID for each instance.

Exposing the PID is intended to make it easier to attach the new Python 3.15 profiler to a running Datasette process.

- datasette-ports detects and lists all Datasette instances on the current machine.
- Version 0.4 works with the latest Datasette version.
- It now displays the detected PID, easing attachment of the Python 3.15 profiler.