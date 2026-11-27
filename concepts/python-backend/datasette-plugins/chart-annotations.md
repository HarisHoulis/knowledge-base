---
domain: python-backend
subdomain: datasette-plugins
concept: chart-annotations
title: datasette-charts 0.3a0 Adds Chart Annotations
sources:
  - title: "datasette-charts 0.3a0"
    url: "https://simonwillison.net/2026/Nov/25/datasette-charts/"
    author: "Simon Willison"
    date: "2026-11-25"
---

# datasette-charts 0.3a0 Adds Chart Annotations

datasette-charts 0.3a0 introduces chart annotations, letting users render a chart and then overlay lines, shaded areas, labels, or a combination of the three. The release post demonstrates this with a bar chart of global power plant capacity by decade, available to try in Datasette Lite with a chart builder UI for tweaking annotations.

Annotations are encoded in the chart JSON configuration, with types such as point, range, line, and text, each carrying a text label and positioning coordinates. For example, a point annotation marks the 2000s as the largest decade total at 1.157 million MW, a range annotation shades 1950–1990, a line annotation draws a 1,000,000 MW reference, and a text annotation adds a caveat about data coverage.

When Datasette Agent is also installed, the agent can build annotated charts from natural-language prompts, as shown in the agent.datasette.io demo where a prompt asked for an annotated comparison of tagged LLM versus Datasette content.

- datasette-charts 0.3a0 adds annotations: lines, shaded ranges, labels, or combinations
- Annotations are stored in the chart JSON config with types like point, range, line, and text
- The chart builder UI in Datasette Lite allows tweaking annotations interactively
- With Datasette Agent installed, an agent can generate annotated charts from prompts