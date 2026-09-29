---
domain: web-dev
subdomain: javascript-language-features
concept: default-parameters
title: JavaScript Default Parameters
sources:
  - title: "JavaScript default parameters"
    url: "https://kentcdodds.com/blog/javascript-default-parameters"
    author: "Kent C. Dodds"
    date: "2018-06-25"
---

# JavaScript Default Parameters

In “JavaScript default parameters,” Kent C. Dodds shows how ES6 default parameters simplify function argument handling. The original example manually checks for required parameters, assigns fallbacks with `upperKind = upperKind || kind.toUpperCase()` and `callback = callback || function noop() {}`, then builds a result object. Dodds notes that this approach has annoying boilerplate and potential bugs related to falsy values.

The ES6 version moves each fallback expression to the right side of the parameter’s equals sign. Default expressions are evaluated only when the parameter is `undefined`, so `requiredParam('kind')` and `requiredParam('size')` run only if those arguments are missing. Defaults can also reference other parameters, as in `upperKind = kind.toUpperCase()`, a feature Dodds says he uses often in options configuration for tools.

The same semantics apply to object destructuring, whether destructuring inside the function body or directly in the parameter list. Examples include `function getCandy(options = {})` followed by destructured defaults, and destructuring the options object directly in the parameter list with a default `{}`. Dodds concludes by linking to a recorded ES6 workshop section for further viewing.

- ES6 default parameters can replace manual `undefined` checks and `||` fallback assignments, reducing boilerplate and falsy-value bugs.
- A default expression is evaluated only when its parameter is `undefined`.
- Default values can reference other parameters, e.g. `upperKind = kind.toUpperCase()`.
- The same default-parameter semantics work with object destructuring, including destructuring directly in the parameter list.