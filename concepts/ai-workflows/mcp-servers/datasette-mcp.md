---
domain: ai-workflows
subdomain: mcp-servers
concept: datasette-mcp
title: datasette-mcp 0.2
sources:
  - title: "datasette-mcp 0.2"
    url: "https://simonwillison.net/2026/Sep/1/datasette-mcp/"
    date: "2026-09-01T15:30:12+00:00"
---

# datasette-mcp 0.2

datasette-mcp 0.2 is the first non-alpha release of the MCP plugin for Datasette. The main change is that the `rows` field returned by the `execute_sql` tool is now an array of objects instead of an array of arrays, which should help weaker language models avoid losing track of which positional array element maps to which column. The plugin also now depends on `mcp>=2.1.1`. The author states they have been using it quite a bit and are confident it is ready.

- `execute_sql` now returns `rows` as an array of objects, improving clarity for models.
- Plugin now requires `mcp>=2.1.1`.
- This is the first non-alpha release of datasette-mcp.
- The author has been using the plugin themselves and considers it ready.