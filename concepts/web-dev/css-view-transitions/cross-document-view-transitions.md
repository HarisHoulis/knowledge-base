---
domain: web-dev
subdomain: css-view-transitions
concept: cross-document-view-transitions
title: Datasette 1.0a43: Streaming Renderers and Cross-Document View Transitions
sources:
  - title: "datasette 1.0a43"
    url: "https://simonwillison.net/2026/Nov/15/datasette/"
    author: "Simon Willison"
    date: "2026-11-15"
---

# Datasette 1.0a43: Streaming Renderers and Cross-Document View Transitions

Datasette 1.0a43 advances the 1.0 milestone (now 53% complete), with the author leaning heavily on Claude Fable 5.2 to close out remaining items. The largest 1.0 feature is streaming support for output renderers: built-in TSV and CSV exports now stream, and plugins can register streaming capability via the new Response.stream() method to emit every row of a table in one go.

Security fixes include one warranting a GitHub advisory: private stored queries could leak their title and SQL (though not be executed). Dozens of smaller improvements land too—a redesigned row-page JSON representation suitable for 1.0, a new <datasette-copy-button> Web Component, pretty-printed JSON in row columns, a DatasetteModal.confirm() JS utility, and bug fixes from several contributors.

The highlight is a small addition: CSS multi-page view transitions, enabled via @view-transition { navigation: auto } under prefers-reduced-motion: no-preference, with named transitions for .facet-results and the rows table. This makes Datasette—still a multi-page application—feel more like an SPA. It works in Safari and Chrome, with Firefox support expected in Firefox 162 on December 8th 2026.

- Streaming output renderers are the biggest 1.0 item; CSV/TSV exports now stream and plugins can use Response.stream()
- A security advisory covers private stored queries leaking title and SQL (not execution)
- Cross-document CSS view transitions make the multi-page app feel SPA-like, using @view-transition and named view-transition-name rules
- Firefox support for the feature is expected in Firefox 162 on December 8th 2026