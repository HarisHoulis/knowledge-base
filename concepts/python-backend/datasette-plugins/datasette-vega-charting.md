---
domain: python-backend
subdomain: datasette-plugins
concept: datasette-vega-charting
title: datasette-vega 0.7: Reviving Datasette's Oldest Plugin
sources:
  - title: "datasette-vega 0.7"
    url: "https://simonwillison.net/2026/Nov/14/datasette-vega/"
    author: "Simon Willison"
    date: "2026-11-14"
---

# datasette-vega 0.7: Reviving Datasette's Oldest Plugin

datasette-vega 0.7 is a new release of Datasette's longest untouched plugin, which renders charts using Vega-Lite against data in a table or custom query. The previous release dated back to July 2018.

The release was bumped for compatibility with the latest Datasette alphas and includes cosmetic tweaks to work better with Datasette Lite. Datasette Lite recently gained the ability to run JavaScript plugins like this one.

Because the plugin now works with Datasette Lite, the README's live demo links to a Datasette Lite example charting airline safety data from FiveThirtyEight.

- datasette-vega renders Vega-Lite charts from table data or custom queries
- First release since July 2018, updated for latest Datasette alphas
- Cosmetic tweaks improve compatibility with Datasette Lite
- Datasette Lite now supports running JavaScript plugins
- README demo now links to a live Datasette Lite example