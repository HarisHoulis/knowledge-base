---
domain: ai-workflows
subdomain: ai-assisted-geospatial
concept: geojson-map-viewer
title: GeoJSON Map Viewer
sources:
  - title: "GeoJSON Map Viewer"
    url: "https://simonwillison.net/2026/Sep/1/geojson/"
    author: "Simon Willison"
    date: "2026-09-01"
---

# GeoJSON Map Viewer

Simon Willison describes needing to display GeoJSON files on a map and export them as PNGs, and how AI chatbots helped build a tool for this. He asked GPT-5.6-Sol for suggestions, and it proactively built the GeoJSON Map Viewer; subsequent iterations using Claude Code and Fable 5.1 refined it (Simon Willison, 2026). The tool allows overlaying multiple GeoJSON layers with custom colors and opacity, and can be shared via URL parameters that set the map location and zoom. Willison also used ChatGPT Work to generate GeoJSON polygons from natural language requests, such as the exact boundary of the El Granada Community Services District or the Midcoast Community Council. These generated files were loaded into the new viewer to combine and visualize both boundaries on one map.

- AI chatbots can generate complete tools from natural language requests, as demonstrated by the GeoJSON Map Viewer being initially built by GPT-5.6-Sol.
- Iterative refinement with multiple AI tools (Claude Code, Fable 5.1) improved the quality and functionality of the generated tool.
- ChatGPT Work can produce accurate GeoJSON boundary files from simple location descriptions, e.g., 'the exact boundary of the El Granada GCSD'.
- The GeoJSON Map Viewer supports displaying multiple GeoJSON layers simultaneously, with options like color, opacity, and map presets for sharing via URLs.