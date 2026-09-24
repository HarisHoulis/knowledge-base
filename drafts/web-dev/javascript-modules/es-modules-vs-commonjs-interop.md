---
domain: web-dev
subdomain: javascript-modules
concept: es-modules-vs-commonjs-interop
title: Misunderstanding ES6 Modules: Babel 6 Migration Lessons
sources:
  - title: "Misunderstanding ES6 Modules, Upgrading Babel, Tears, and a Solution"
    url: "https://kentcdodds.com/blog/misunderstanding-es6-modules-upgrading-babel-tears-and-a-solution"
    author: "Kent C. Dodds"
    date: "2015-12-23"
---

# Misunderstanding ES6 Modules: Babel 6 Migration Lessons

Kent C. Dodds recounts how upgrading from Babel 5 to Babel 6 broke over 200 modules in his application because he had misunderstood the ES6 modules spec. Babel 5 allowed misuse of `export`/`import` statements—notably exporting an object as default and then destructuring pieces from it at import time—but Babel 6 correctly removed this capability per the spec. Logan Smyth clarified on Stack Overflow that the author "fundamentally misunderstood ES6 modules and that Babel 5 had facilitated that misunderstanding" (Babel 5 to Babel 6 upgrade post).

The root issue is that ES6 modules must be statically analyzable—imports and exports cannot change at runtime. The author's habit of exporting a mutable object as default and importing dynamic properties from it only works in CommonJS, where `require` executes at runtime. Because imports/exports in ES6 cannot be dynamic, this pattern is invalid, and Babel 6 stopped transpiling it as if it were valid.

The practical conflict arose from mixing ES6 `export` with CommonJS `require`. After the change, `require('./add')` returns an object containing all named exports plus the default export under the `default` key, rather than the default export directly. Dodd offers three fixes: use `require('./add').default`, commit fully to ES6 modules (`import add from './add'`), or commit fully to CommonJS (`module.exports`). He solved it by either switching exports to `module.exports` or using a regex find-and-replace to change `require('./thing')` to `require('./thing').default`.

His recommendation is to avoid mixing ES6 modules and CommonJS, favoring ES6 throughout. For utility modules, named exports pair well with tree shaking; for single components/services, default exports are more appropriate. The core lesson: learn how things are supposed to work before relying on transpiler behavior.

- ES6 modules must be statically analyzable, so imports/exports cannot be dynamic at runtime—unlike CommonJS `require`.
- Babel 5 permitted destructuring imports from a default-exported object; Babel 6 removed this as a spec correction, breaking code that relied on it.
- After the change, `require('./thing')` returns an object where the default export lives under the `.default` key, not the export itself.
- Avoid mixing ES6 modules and CommonJS; if forced, consider plugins like babel-plugin-add-module-exports.
- Use named exports for utility modules (enables tree shaking) and default exports for single components/services.