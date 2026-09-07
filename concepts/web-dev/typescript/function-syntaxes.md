---
domain: web-dev
subdomain: typescript
concept: function-syntaxes
title: TypeScript Function Syntaxes
sources:
  - title: "TypeScript Function Syntaxes"
    url: "https://kentcdodds.com/blog/typescript-function-syntaxes"
    date: "2021-02-25"
---

# TypeScript Function Syntaxes

The article catalogs the many ways functions can be written in TypeScript, ranging from function declarations and expressions to arrow functions, classes, generator functions, and async functions. A key clarification is that the `=>` syntax is only used when defining a function type itself (e.g., `type Fn = (arg: ArgType) => ReturnType`), while in all other contexts (interfaces, object types, implementations) the return type is annotated with a colon (e.g., `const fn = (arg: ArgType): ReturnType => ...`). The post provides concrete examples throughout, including how to type object properties, class methods, rest parameters, and default parameters.

- Use `=>` only when defining a standalone function type; use `:` everywhere else.
- Default parameters are treated as optional by TypeScript, allowing calls like `sum(1)` even if the second param has a default.
- Typed function properties on objects cannot be annotated inline; you must extract the function type and then assign it.
- Generic arrow functions in TSX need `<Type extends unknown>` to avoid confusion with JSX.
- A custom type guard function (e.g., `typedBoolean`) enables type narrowing in array `.filter()` calls.