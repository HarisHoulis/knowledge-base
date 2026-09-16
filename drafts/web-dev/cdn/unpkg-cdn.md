---
domain: web-dev
subdomain: cdn
concept: unpkg-cdn
title: unpkg: An Open Source CDN for npm
sources:
  - title: "unpkg: An open source CDN for npm"
    url: "https://kentcdodds.com/blog/unpkg-an-open-source-cdn-for-npm"
    author: "Kent C. Dodds"
    date: "2018-08-13"
---

# unpkg: An Open Source CDN for npm

unpkg is an open source, global content delivery network for everything on npm, created by Michael Jackson to easily demo React Router by proxying files hosted on npm (source). It serves any package file through a URL like `unpkg.com/:package@:version/:file`, such as `https://unpkg.com/d3@5.5.0/dist/d3.min.js`. Bare package URLs redirect to the file specified by the package's `package.json` `unpkg` field, and version ranges like `d3@^5.5.0` are supported, though pinning a version is recommended to avoid breaking changes from major version bumps (source).

unpkg is fast because npm published packages cannot be changed, so files can be heavily cached (source). It is hosted on Heroku, which handles only about 5% of traffic, while Cloudflare serves 95% of unpkg's traffic from cache (source). It is useful for open source project demos and instructional material, but it is a free, best-effort service without uptime or support guarantees, making it unsuitable for mission-critical applications at scale; Michael Jackson recommends paying for well-supported infrastructure if files are crucial to a business (source).

Kent C. Dodds plans to build a hosted version of unpkg at PayPal because many projects use the same dependencies, such as React, react-dom, rxjs, and lodash, and each project currently serves its own `bundle.js` with duplicated code (source). A hosted unpkg would let teams use whatever versions they want while allowing users to download a common version only once, and it could be integrated into `paypal-scripts` for automatic user experience improvement (source).

- unpkg provides URL-based access to any file in any npm package, e.g. `unpkg.com/d3@5.5.0/dist/d3.min.js`.
- Bare package URLs redirect using the `package.json` `unpkg` field, and version ranges are supported; pinning versions avoids breaking changes.
- Because npm packages are immutable, unpkg can cache aggressively; Cloudflare serves 95% of its traffic from cache.
- unpkg is a free, best-effort service without uptime or support guarantees, so it is not recommended for mission-critical applications at scale.
- A hosted unpkg at PayPal could reduce duplicate downloads across projects by sharing common dependency versions without forcing all teams to use the same versions.