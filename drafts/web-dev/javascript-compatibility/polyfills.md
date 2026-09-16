---
domain: web-dev
subdomain: javascript-compatibility
concept: polyfills
title: What is a polyfill
sources:
  - title: "What is a polyfill"
    url: "https://kentcdodds.com/blog/what-is-a-polyfill"
    date: "2018-07-30"
---

# What is a polyfill

The article explains that a bug causing a blank page in IE10 was due to a missing `Array.prototype.includes`, which Babel transpilation does not handle because Babel transforms syntax, not built-in APIs (source). Babel's env preset only applies syntax transforms, so APIs like `includes` remain missing in older environments (source).

A polyfill is code that makes the currently running JavaScript environment support features it lacks (source). A gated polyfill for `Array.prototype.includes` checks if the method is missing, then monkey-patches the prototype so existing native implementations are not overridden (source). Monkey-patching adds support to all arrays; gating can cause compatibility issues, such as `String.prototype.contains` being renamed to `includes` because some MooTools versions implemented `contains` differently (source).

Recommended tools include `babel-preset-env` for syntax transforms, and `core-js`, `babel-polyfill`, or Airbnb `js-shims` for polyfills (source). Polyfills are sometimes called shims (source). To avoid shipping unnecessary polyfills, services like polyfill.io can serve only polyfills relevant to the requesting browser (source). Ponyfills are similar but do not monkey-patch; the author generally favors them, though polyfills remain necessary because dependencies may rely on unsupported built-ins (source).

- Babel transpiles syntax but does not polyfill new built-in APIs like `Array.prototype.includes`.
- Polyfills add missing APIs to the runtime; gated polyfills avoid overriding existing implementations.
- Monkey-patching prototypes has risks, illustrated by the `String.prototype.contains`/`includes` naming conflict.
- Use `core-js`, `babel-polyfill`, or `js-shims` for polyfills; polyfill.io can serve browser-specific polyfills.
- Ponyfills avoid monkey-patching but polyfills are still needed for dependencies that rely on unsupported built-ins.