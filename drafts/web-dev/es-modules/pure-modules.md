---
domain: web-dev
subdomain: es-modules
concept: pure-modules
title: Pure Modules
sources:
  - title: "Pure Modules"
    url: "https://kentcdodds.com/blog/pure-modules"
    author: "Kent C. Dodds"
    date: "2018-04-30"
---

# Pure Modules

Kent C. Dodds argues that JavaScript modules should be pure in the sense that importing them has no side effects, although the functions they expose may be impure (Kent C. Dodds, 2018). He shows an impure example where `a.js` imports `b.js`, which imports `c.js`; `c.js` reads `serverData` from the DOM at module evaluation time. Because ES module imports execute before the importing module's body regardless of where the import statement appears, merely importing `a.js` can trigger side effects, cryptic errors, and code execution the importer may not need.

These impure modules have several downsides: unknown consequences for importers, unnecessary operations that cannot be tree-shaken away, inability to choose the order of operations without creating another setup module, and difficulty testing modules that depend on pre-existing DOM or global state (Kent C. Dodds, 2018). The proposed alternative is to export explicit `init` functions. For example, `c.js` exports `serverData` and an `init` function that reads and assigns the DOM data; `b.js` imports and calls `initC` inside its own `init`; `a.js` imports and calls `b`'s `init` before logging ready. This makes import side-effect-free while preserving explicit setup.

The article acknowledges that the entry module (often `index.js`) may still be impure, since something must kick off the application. Keeping other modules pure limits root-level work, avoids the listed issues, and brings more clarity to the codebase (Kent C. Dodds, 2018).

- ES module imports run before any module code, even if import statements appear later in the file.
- Impure modules cause unknown consequences for importers, including cryptic runtime errors.
- Root-level side effects prevent tree-shaking and may perform unnecessary work.
- Explicit `init` functions let developers control order of operations and simplify testing.
- The entry module can remain impure to start the app, but other modules should avoid root-level side effects.