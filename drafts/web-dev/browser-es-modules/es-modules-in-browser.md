---
domain: web-dev
subdomain: browser-es-modules
concept: es-modules-in-browser
title: Super Simple Start to ESModules in the Browser
sources:
  - title: "Super Simple Start to ESModules in the Browser"
    url: "https://kentcdodds.com/blog/super-simple-start-to-es-modules-in-the-browser"
    author: "Kent C. Dodds"
    date: "2020-01-22"
---

# Super Simple Start to ESModules in the Browser

The post demonstrates using ES Modules directly in browsers now that all major browsers support them. A module is loaded by adding `type="module"` to a `<script>` tag; an inline script can then `import { appendDiv } from './append-div.js'` and call the exported function [source](https://kentcdodds.com/blog/super-simple-start-to-es-modules-in-the-browser).

Modules cannot be loaded by opening the HTML file directly from disk; a local server is required, such as running `npx serve` in the project directory. External modules are loaded with `<script type="module" src="./script-src.js"></script>`. Import specifiers must include the `.js` extension because the modules spec requires pointing directly to a JavaScript resource, though any URL that returns JavaScript works—e.g. `import * as d3 from 'https://unpkg.com/d3?module'` [source](https://kentcdodds.com/blog/super-simple-start-to-es-modules-in-the-browser).

Dynamic `import()` also works and returns a promise, enabling asynchronous loading and error handling. The post provides a gist with the code and references a companion post on ES Modules in Node.js [source](https://kentcdodds.com/blog/super-simple-start-to-es-modules-in-the-browser).

- Use `<script type="module">` to load an inline module, or add `src` to load an external module file.
- Modules must be served over a local HTTP server (e.g., `npx serve`), not opened directly as a `file://` URL.
- Browser ES module imports require explicit file extensions or a URL that returns JavaScript; any such URL can be imported, including CDN URLs like unpkg.
- Dynamic `import()` returns a promise and supports success and error callbacks.