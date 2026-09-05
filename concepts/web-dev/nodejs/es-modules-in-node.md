---
domain: web-dev
subdomain: nodejs
concept: es-modules-in-node
title: Super Simple Start to ESModules in Node.js
sources:
  - title: "Super Simple Start to ESModules in Node.js"
    url: "https://kentcdodds.com/blog/super-simple-start-to-es-modules-in-node-js"
    date: "2021-04-08"
---

# Super Simple Start to ESModules in Node.js

The article explains how to start using ESModules in Node.js, noting that Node v10 reaches its end of life on April 30, 2021, after which all supported Node versions will support ESModules. It presents a simple example with `import` and `export` statements, including top-level `await`, and shows that running `node .` initially fails because ES modules are an opt-in feature in Node.js.

Node.js offers two ways to enable ES modules: using the `.mjs` file extension for individual files, or adding a `package.json` with `"type": "module"` to opt in an entire directory. The article demonstrates the second approach by adding a minimal `package.json` and rerunning the command successfully. It concludes by pointing readers to the official announcement for further details (Kent C. Dodds, 2021).

- All supported Node.js versions (after v10's end of life) support ESModules.
- ESM in Node.js is opt-in: either use the `.mjs` extension or set `"type": "module"` in `package.json`.
- Adding `{"type": "module"}` to the project's `package.json` enables ESM for all `.js` files in that project.
- ESM in Node.js supports top-level `await`, simplifying asynchronous code.