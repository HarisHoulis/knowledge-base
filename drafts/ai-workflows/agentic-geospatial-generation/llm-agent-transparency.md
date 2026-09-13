---
domain: ai-workflows
subdomain: agentic-geospatial-generation
concept: llm-agent-transparency
title: Generating running routes with GPT-6 Astra and ChatGPT Work
sources:
  - title: "Generating running routes with GPT-6 Astra and ChatGPT Work"
    url: "https://simonwillison.net/2026/Sep/12/astra-running-routes/"
    date: "2026-09-12T23:56:42+00:00"
---

# Generating running routes with GPT-6 Astra and ChatGPT Work

The author asked ChatGPT Work with GPT-6 Astra (Max) to plan 5K and 10K loop running routes from his home address using OpenStreetMap data (source). The system worked for 27 minutes and produced an embedded visualization plus downloadable GPX and GeoJSON files (source).

When asked how it created the route, ChatGPT said it used Nominatim to locate the address and Overpass to download local OSM roads and trails, then calculated the loops locally (source). The map visualization used a "visualize skill" and created an HTML file at /workspace/el-granada-5k-share.html for embedding in the ChatGPT UI, with route geometry stored in a script type application/json and D3 loaded from an allow-listed CDN (source).

The author criticizes the lack of transparency: the actual code and exact details of what the model did were not visible in the ChatGPT UI, which he calls an anti-feature (source). By the time he asked for the Python code, ChatGPT could not provide it, apparently because the thread had been compacted; he argues that any LLM system using compaction should preserve pre-compacted text and make it available via agent tool calls (source).

- ChatGPT Work with GPT-6 Astra (Max) generated 5K and 10K loop running routes from OSM data in 27 minutes, returning an embedded map, GPX, and GeoJSON (source).
- The model reported using Nominatim for address geocoding and Overpass for downloading OSM roads and trails (source).
- The visualization was produced via a "visualize skill" that embedded D3 from an allow-listed CDN inside ChatGPT's UI (source).
- The author calls the invisibility of the executed code and exact steps an anti-feature (source).
- Thread compaction prevented later retrieval of the Python code; the author says pre-compacted text should be preserved and accessible through agent tool calls (source).