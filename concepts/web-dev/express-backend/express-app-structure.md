---
domain: web-dev
subdomain: express-backend
concept: express-app-structure
title: How I structure Express apps
sources:
  - title: "How I structure Express apps"
    url: "https://kentcdodds.com/blog/how-i-structure-express-apps"
    date: "2020-07-13"
---

# How I structure Express apps

In the article 'How I structure Express apps', the author describes a typical structure for medium-sized Node.js backends built with Express. The setup begins in package.json, specifying Node engines, dependencies such as express, express-async-errors, and loglevel, and dev dependencies for Babel and nodemon. The build script compiles source files from src to dist using Babel, while the start script simply runs node . (source: package.json section).

- Use Babel to compile ESModules from src to dist, with index.js switching between production and dev (nodemon + @babel/register).
- Export a startServer function that returns a Promise, making the server easier to test with integration tests.
- Use express-async-errors so async middleware errors propagate to a custom error middleware.
- Organize routes as Express routers via getRoutes() factory functions, mounting them under /api.
- Implement graceful shutdown handling and a generic error middleware that hides stack traces in production.