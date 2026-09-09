---
domain: web-dev
subdomain: server-side-redirects
concept: server-side-redirects
title: Stop using client-side route redirects
sources:
  - title: "Stop using client-side route redirects"
    url: "https://kentcdodds.com/blog/stop-using-client-side-route-redirects"
    author: "Kent C. Dodds"
    date: "2020-04-13"
---

# Stop using client-side route redirects

The article distinguishes between client-side redirects that map a known old URL to a new one (e.g., React Router's `<Redirect from="/old" to="/new">`) and conditional redirects based on state, such as authentication. While the latter may be acceptable, the former should be avoided because it forces the user to download the application bundle before the redirect can occur, wasting bandwidth and time (Dodds, 2020).

Client-side redirects also cannot return proper HTTP status codes like 301 or 302, which prevents search engines and browsers from correctly handling URL changes and caching. This has negative implications for SEO and browser cache behavior (Dodds, 2020).

Instead, the article recommends using server-side redirects. It provides concrete examples for Netlify via `_redirects` or `netlify.toml`, for local static serving via `serve.json`, and for development environments via `setupProxy.js` in Create React App. These approaches are simpler, semantically correct, and align with web standards (Dodds, 2020).

- Avoid client-side route redirects that map known old routes to new routes; they require downloading the app before redirection.
- Client-side redirects don't return HTTP status codes, harming SEO and browser caching.
- Use server-side redirects configured on your hosting platform (Netlify, serve, CRA dev proxy) for better semantics and performance.
- When web standards satisfy the use case, use the web standard.