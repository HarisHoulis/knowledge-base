---
domain: python-backend
subdomain: observability
concept: opentelemetry-trace-ingestion
title: Using Parseable with Datasette for OpenTelemetry traces
sources:
  - title: "Using Parseable with Datasette for OpenTelemetry traces"
    url: "https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry/"
    author: "Simon Willison"
    date: "2026-10-06"
  - title: "TIL: Using Parseable with Datasette for OpenTelemetry traces"
    url: "https://til.simonwillison.net/datasette/datasette-parseable-opentelemetry"
    author: "Simon Willison"
    date: "2026-10-06"
---

# Using Parseable with Datasette for OpenTelemetry traces

Parseable is a new observability platform spotted on Show HN: an open source (AGPL) Rust implementation that ships as a single ~180MB binary, alongside an "Enterprise" edition with extra features and a cloud-hosted option [source].

Datasette 1.0a41 added OpenTelemetry support, contributed by Alex Garcia, which makes it possible to emit traces from Datasette itself [source]. The author used Codex to work out how to run Parseable and feed it traces from Datasette, and published a human-written TIL documenting the patterns that worked, plus a screenshot of a Datasette trace rendered inside the Parseable localhost web application [source].

The post is a short pointer to that TIL rather than a full walkthrough; the practical artifact is the combination of Datasette's new OTEL instrumentation with a local, single-binary Parseable instance as the trace backend [source].

- Parseable is an observability platform with an open source AGPL Rust implementation distributed as a single ~180MB binary, plus Enterprise and cloud-hosted variants [source].
- Datasette 1.0a41 introduced OpenTelemetry support (credited to Alex Garcia), enabling Datasette to emit traces [source].
- Parseable can act as the local trace backend for Datasette's OpenTelemetry output, viewable in its localhost web UI [source].
- The how-to details live in a companion TIL, generated experimentally with Codex but written up by hand [source].