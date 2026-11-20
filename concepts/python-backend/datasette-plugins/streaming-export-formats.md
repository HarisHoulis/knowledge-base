---
domain: python-backend
subdomain: datasette-plugins
concept: streaming-export-formats
title: datasette-arrows 0.1a0: Streaming Apache Arrow Exports for Datasette
sources:
  - title: "datasette-arrows 0.1a0"
    url: "https://simonwillison.net/2026/Nov/18/datasette-arrows/"
    author: "Simon Willison"
    date: "2026-11-18"
---

# datasette-arrows 0.1a0: Streaming Apache Arrow Exports for Datasette

Datasette 1.0a43 introduced the ability for plugins to implement streaming export formats, extending the existing streaming CSV and TSV support in core. Streaming lets users export millions of rows without loading the entire table into memory, since those formats can emit data in chunks. The register_output_renderer() plugin hook now enables the same pattern for other formats.

To validate the new hook, Simon Willison built datasette-arrows, a plugin that adds Apache Arrow streaming export. He notes a principle of never releasing a new plugin feature without an accompanying plugin that exercises it. Claude Fable 5.2 suggested the Apache Arrow streaming format as a good candidate and built the plugin in almost a single shot.

Installing the plugin (datasette install datasette-arrows) adds an Arrow option to the export dialog. The screenshot shown comes from Datasette's main branch; the most recent release does not yet group streaming formats like Arrow with TSV and CSV under the "All rows in this table" section, but that grouping is planned for the next alpha release.

- Datasette 1.0a43 added a plugin hook for streaming export formats, generalizing core's streaming CSV/TSV support.
- Streaming exports avoid loading full tables into memory, enabling export of millions of rows.
- datasette-arrows implements Apache Arrow streaming via register_output_renderer() and was built almost in a single shot by Claude Fable 5.2.
- New plugin features should ship with a reference plugin that uses them.
- Grouping of streaming formats in the export dialog is planned for the next alpha.