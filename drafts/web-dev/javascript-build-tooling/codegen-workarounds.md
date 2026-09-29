---
domain: web-dev
subdomain: javascript-build-tooling
concept: codegen-workarounds
title: Make maintainable workarounds with codegen
sources:
  - title: "Make maintainable workarounds with codegen 💥"
    url: "https://kentcdodds.com/blog/make-maintainable-workarounds-with-codegen"
    author: "Kent C. Dodds"
    date: "2017-10-09"
---

# Make maintainable workarounds with codegen

Andrew Blick filed an issue on `glamorous` showing that its UMD build did not work with React 16. The cause was that `glamorous` lazy-requires `prop-types`, and Rollup could not handle the CommonJS `require` in the UMD bundle, so `PropTypes = require('prop-types')` remained untranspiled and was not passed in from the global object [source].

Instead of blaming tools, Kent filed an issue with a reproduction to verify the problem was Rollup, then explored a workaround. He used `babel-plugin-codegen` and its companion `codegen.macro` to replace the simple `PropTypes = require('prop-types')` with build-time conditional code based on `process.env.BUILD_FORMAT` [source].

`codegen` runs the provided code string like a regular module at build time, then replaces itself with the exported code string. For UMD builds, the workaround pulls `PropTypes` from `window` or `global`; for all other builds, it continues to use `require('prop-types')`, leaving existing builds unchanged [source].

Kent notes that putting too much code inside a string loses syntax highlighting and lintability, so larger workarounds can be pulled into another file and required inside `codegen`. He values that using a Babel macro keeps the workaround localized and optimized, and says it took less than 10 minutes [source].

- `glamorous`'s UMD build broke with React 16 because Rollup could not handle its CommonJS `require('prop-types')` lazy-require.
- Andrew Blick filed the issue with a reproduction; Kent used it to verify the problem was Rollup and then built a workaround.
- `codegen.macro` executes code at build time and replaces itself with the exported code string, enabling conditional build-specific output.
- The workaround kept `require('prop-types')` for normal builds but pulled `PropTypes` from the global object for UMD builds.
- Using a Babel macro makes the workaround localized and optimized; avoid large inline code strings because you lose syntax highlighting and linting.