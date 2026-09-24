---
domain: python-backend
subdomain: observability-and-frontend-tooling
concept: opentelemetry-integration
title: Datasette 1.0a41: OpenTelemetry Support and a Modal Web Component
sources:
  - title: "datasette 1.0a41"
    url: "https://simonwillison.net/2026/Sep/24/datasette/"
    date: "2026-09-24"
  - title: "datasette 1.0a41 release"
    url: "https://github.com/simonw/datasette/releases/tag/1.0a41"
  - title: "Datasette internals: telemetry"
    url: "https://docs.datasette.io/en/latest/internals.html#internals-telemetry"
  - title: "Datasette JavaScript plugins: modals"
    url: "https://docs.datasette.io/en/latest/javascript_plugins.html#javascript-plugins-modals"
---

# Datasette 1.0a41: OpenTelemetry Support and a Modal Web Component

Datasette 1.0a41 adds OpenTelemetry support, contributed by Alec Garcia, with documentation placed under Datasette's internals telemetry section [source]. This gives the project built-in telemetry instrumentation.

The release also refactors all of Datasette's modal dialogs into a single Web Component, which is now documented for other plugins to use [source]. This consolidates previously duplicated modal behavior into a reusable component exposed to the plugin ecosystem.

The post is tagged javascript, datasette, web-components, alex-garcia, and opentelemetry, indicating the two focal changes span backend observability and frontend component reuse [source].

- OpenTelemetry support was added to Datasette in 1.0a41, contributed by Alec Garcia [source].
- OpenTelemetry is documented in Datasette's internals documentation [source].
- All modal dialogs were refactored into a single Web Component [source].
- That modal Web Component is documented for other plugins to use [source].