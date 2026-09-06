---
domain: web-dev
subdomain: typescript
concept: function-overload-types
title: Define function overload types with TypeScript
sources:
  - title: "Define function overload types with TypeScript"
    url: "https://kentcdodds.com/blog/define-function-overload-types-with-type-script"
    author: "Kent C. Dodds"
    date: "2021-01-12"
---

# Define function overload types with TypeScript

The article explains how to define function overload types in TypeScript, beginning with a common pattern: a function that either accepts a callback or returns a Promise when no callback is provided. The author shows how to declare multiple overload signatures for `asyncAdd` before the implementation, ensuring TypeScript catches incorrect usage such as calling `.then` on a `void` result. The key is to list all valid signatures first, then write a single implementation that is compatible with all of them, often using optional parameters and a union of possible return types.

He then applies the same principle to a more complex real-world case: typing a `codegen.macro` utility. For `codegen`, overloads are needed to support a tagged template literal form, a function-call form, and a `codegen.require` namespace method. The author demonstrates declaring these overloads and then casting the underlying macro implementation to the typed interface using `export default macro as typeof codegen`. This gives consumers type safety while keeping the implementation details hidden. The post notes that the JSX form was not yet typed due to overload limitations (source: Define function overload types with TypeScript, Kent C. Dodds, 2021).

- Define function overloads by declaring each allowed signature before the implementation, then implement once with optional parameters and compatible return types.
- Function overloads catch invalid calls at compile time, e.g., using `.then` on a void-returning callback overload.
- The same technique works for complex APIs like tagged template literals, function calls, and namespaced functions using `declare namespace`.
- For libraries that wrap macros or other non-standard implementations, cast the actual function to the typed overloads to expose a clean public API.
- Some forms (like JSX in the example) may not be typeable due to current TypeScript limitations.