---
domain: python-backend
subdomain: python-testing-and-observability
concept: wrapture
title: Introducing wrapture
sources:
  - title: "Introducing wrapture"
    url: "https://simonwillison.net/2026/Aug/31/introducing-wrapture/"
    author: "Simon Willison"
    date: "2026-08-31"
---

# Introducing wrapture

Wrapture is a Python library by Graham Dumpleton that makes it easy to wrap functions or methods so all access can be traced or overridden to return different values. It serves as both an alternative to unittest.mock and a tool for attaching observation to code you do not control, recording what flows through it without disturbing the program being watched. The library includes OpenTelemetry support and a configuration-based mechanism for adding tracing to existing Python projects, as shown in the article's example of observing a Calculator domain and sinking traces to a JSON lines file.

- Wrapture provides tracing and override capabilities for functions and methods, acting as a practical alternative to unittest.mock.
- It includes OpenTelemetry support and a configuration-driven approach to observability.
- The project supports test patterns like stubbing and transforming return values, demonstrated with wrapture.binding examples.
- Wrapture was developed entirely by an AI assistant under careful human direction, explicitly not vibe coding.