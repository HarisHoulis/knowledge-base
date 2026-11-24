---
domain: ai-workflows
subdomain: coding-agents
concept: agent-built-datasette-plugin
title: datasette-charts 0.1a0: An AI-Assisted Charting Plugin for Datasette
sources:
  - title: "datasette-charts 0.1a0"
    url: "https://simonwillison.net/2026/Nov/23/datasette-charts/"
    author: "Simon Willison"
    date: "2026-11-23"
---

# datasette-charts 0.1a0: An AI-Assisted Charting Plugin for Datasette

Simon Willison released datasette-charts 0.1a0, a Datasette plugin that generates charts for any table or arbitrary SQL query. After thinking about the problem for over a year, he built an initial prototype with Claude Fable 5.2 on a Sunday, and the prototype went well enough that it became a full plugin. It is available to try in Datasette Lite.

The plugin defines several chart types using vendored D3, Observable Plot, and topojson-client, each with heuristics for identifying when a chart type might suit a given set of rows. Suggestion thumbnails at the top are actual data-driven visualizations; selecting one opens the full chart with editing tools, and users can also build charts manually. Chart state is persisted in a URL #fragment so charts can be bookmarked and shared.

The key feature is that charts account for all rows, not just the current page of up to 100 results as with datasette-vega. Each chart compiles to a SQL query that aggregates across the entire result set using GROUP BY, time bucketing, and window functions, with results capped at 5,000 rows for display. Sampling helps suggest charts for larger tables without evaluating the full result set. Willison describes it as an alpha but the closest he has come to Datasette visualizing data with minimal user direction.

- Prototype built with Claude Fable 5.2 in a single session, then expanded into a full plugin
- Charts compile to SQL aggregations (GROUP BY, time bucketing, window functions) over the entire result set, capped at 5,000 rows
- Chart types use vendored D3, Observable Plot, and topojson-client with heuristics for suggesting matches
- Chart state persists in the URL #fragment for bookmarking and sharing
- Sampling enables chart suggestions on large tables without full evaluation