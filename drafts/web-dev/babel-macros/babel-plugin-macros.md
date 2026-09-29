---
domain: web-dev
subdomain: babel-macros
concept: babel-plugin-macros
title: Write your own code transform for fun and profit
sources:
  - title: "Write your own code transform for fun and profit"
    url: "https://kentcdodds.com/blog/write-your-own-code-transform"
    author: "Kent C. Dodds"
    date: "2018-06-04"
---

# Write your own code transform for fun and profit

The article introduces `babel-plugin-macros`, describing it as enabling zero-config, importable Babel plugins (source). It notes two developments: it can be used with create-react-app v2 beta because it is included by default in `babel-preset-react-app`, and it was added as an optional transform to astexplorer.net (source).

It then walks through a contrived `gemmafy` macro that splits a string and replaces every space with 🐶. The macro is written as `module.exports = createMacro(gemmafyMacro)`, where `gemmafyMacro` receives `{ references, state, babel }` and replaces the function call with a string literal; `babel-plugin-macros` removes the import automatically (source). The example can be run in astexplorer.net with JavaScript, babylon7, and the babel-macros transform, producing `console.log('hello 🐶 world')` (source).

The article extends this with a more general macro that handles default and named imports, tagged template literals, JSX, and references used as callee or argument. It logs the relevant AST paths for exploration (source).

The conclusion states that precompiling operations can improve runtime performance and bundle size, and that macros allow build-time work with file system access; the possibilities are described as endless (source).

- `babel-plugin-macros` enables zero-config, importable Babel plugins.
- It is included by default in `babel-preset-react-app` used by create-react-app v2 beta and is available as an optional transform on astexplorer.net.
- A macro exports `createMacro` with a function receiving `{ references, state, babel }`, and it manipulates AST paths.
- The `gemmafy` example replaces spaces in a string literal with 🐶; the import is removed automatically.
- Macros can support default imports, named imports, tagged templates, JSX, and arbitrary call patterns, enabling precompilation for runtime performance/bundle size and build-time file system access.