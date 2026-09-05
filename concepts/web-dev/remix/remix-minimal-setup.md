---
domain: web-dev
subdomain: remix
concept: remix-minimal-setup
title: Super Simple Start to Remix
sources:
  - title: "Super Simple Start to Remix"
    url: "https://kentcdodds.com/blog/super-simple-start-to-remix"
    date: "2021-05-03"
---

# Super Simple Start to Remix

This article walks through building a Remix application from scratch, without using the scaffolding CLI, to understand the pieces required. The setup requires installing react, react-dom, and @remix-run/dev, creating an empty remix.config.js, and adding a build script. After the initial build, Remix asks for app/entry.client, app/entry.server, and app/root files; the build fails until @remix-run/react is also installed. The author implements these files manually, showing how the root component renders the full HTML document, entry.client hydrates the document with RemixBrowser, and entry.server uses ReactDOMServer.renderToString plus returns a Response.

- Remix requires little boilerplate: remix.config.js plus app/entry.client.jsx, app/entry.server.jsx, and app/root.jsx.
- The developer controls the entire document from <html> down, including where and whether to include JavaScript.
- Hydration is explicit: entry.client calls hydrateRoot(document, <RemixBrowser />), and server rendering uses RemixServer.
- Remix uses web-standard Request/Response objects, with adapters such as @remix-run/serve, vercel, netlify, or cloudflare-workers bridging platform differences.
- The article notes remix dev provides live reload but not yet HMR, and recommends full-page refreshes while server code is heavily involved.