---
domain: ai-workflows
subdomain: coding-agents
concept: single-prompt-plugin-generation
title: datasette-maplibre 0.1a0: A Geospatial Plugin Built From One Prompt
sources:
  - title: "datasette-maplibre 0.1a0"
    url: "https://simonwillison.net/2026/Nov/15/datasette-maplibre/"
    author: "Simon Willison"
    date: "2026-11-15"
---

# datasette-maplibre 0.1a0: A Geospatial Plugin Built From One Prompt

Simon Willison released datasette-maplibre 0.1a0, a new Datasette geospatial plugin combining the MapLibre GL library with OpenFreeMap, the free vector map server operated by Zsolt Ero. It is the first new Datasette geospatial plugin in quite a while.

Most of the plugin was built with a single prompt to Claude Fable 5.2, which asked the model to study the datasette-cluster-map and datasette-leaflet-geojson plugins plus a local OpenFreeMap demo file, then build a new plugin combining their features while being "creative" and thinking "outside the box." That instruction produced a few neat ideas, the author's favorite being SVG previews of GeoJSON shapes that only load a WebGL preview when scrolled into view.

Claude also built a comprehensive demo that works in the latest Datasette Lite, letting users load the plugin and a demo database entirely in the browser via Pyodide and WebAssembly. A demo page shows both GeoJSON shapes and lat/lon points on the same map.

- datasette-maplibre 0.1a0 combines MapLibre GL with the free OpenFreeMap vector tile server
- Most of the plugin was generated from a single prompt to Claude Fable 5.2 referencing two existing plugins
- The "be creative" instruction yielded features like lazy-loaded WebGL previews with SVG placeholders
- A full demo runs in Datasette Lite via Pyodide and WebAssembly