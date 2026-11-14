---
domain: web-dev
subdomain: datasette-plugins
concept: referrer-policy-tile-requests
title: datasette-leaflet 0.3: Fixing OpenStreetMap Referrer Policy
sources:
  - title: "datasette-leaflet 0.3"
    url: "https://simonwillison.net/2026/Nov/13/datasette-leaflet/"
    author: "Simon Willison"
    date: "2026-11-13"
---

# datasette-leaflet 0.3: Fixing OpenStreetMap Referrer Policy

datasette-leaflet 0.3 addresses a conflict between Datasette's default HTTP headers and OpenStreetMap's tile usage policy. OpenStreetMap requires that requests to its hosted tile server send a referrer header, but Datasette table pages used the `Referrer-Policy: no-referrer` header, causing plugins loading OpenStreetMap tiles to violate that policy.

The plugin, which bundles Leaflet so other Datasette plugins can depend on it, now sets the referrer policy on the tile requests themselves to `strict-origin-when-cross-origin`. This passes the host but not the full page path, satisfying OpenStreetMap's policy while limiting information disclosure.

- OpenStreetMap's policy requires a referrer header on tile server requests.
- Datasette's `Referrer-Policy: no-referrer` header caused tile-loading plugins to violate that policy.
- datasette-leaflet 0.3 sets `strict-origin-when-cross-origin` on tile requests, sending the host but not the full path.