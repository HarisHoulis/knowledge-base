---
domain: web-dev
subdomain: data-visualization
concept: datasette-charts-ui-improvements
title: datasette-charts 0.2a1 Release Notes
sources:
  - title: "datasette-charts 0.2a1"
    url: "https://simonwillison.net/2026/Nov/24/datasette-charts-2/"
    author: "Simon Willison"
    date: "2026-11-24"
---

# datasette-charts 0.2a1 Release Notes

datasette-charts 0.2a1 is a minor release focused on UI improvements to the Datasette charting plugin. Collapsing the suggested charts section now leaves the chart itself visible, and following a link to a chart opens it with suggestions collapsed for that visit. On table pages, the chart panel now sits below the filtered row-count line (e.g. "4,235 rows where country = CHN").

The release also replaces the "Data" table under each chart with Copy TSV and Copy CSV buttons, removes the "Chart this data" item from the table, view and query action menus, and adds more spacing between lines in chart tooltips.

- Collapsing suggested charts keeps the chart visible; chart links open with suggestions collapsed
- Chart panel repositioned below the filtered row-count line on table pages
- Data table replaced by Copy TSV and Copy CSV buttons
- "Chart this data" removed from table, view and query action menus