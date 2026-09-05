---
domain: web-dev
subdomain: typescript
concept: constrained-identity-function
title: How to write a Constrained Identity Function (CIF) in TypeScript
sources:
  - title: "How to write a Constrained Identity Function (CIF) in TypeScript"
    url: "https://kentcdodds.com/blog/how-to-write-a-constrained-identity-function-in-typescript"
    author: "Kent C. Dodds"
    date: "2021-03-09"
---

# How to write a Constrained Identity Function (CIF) in TypeScript

The article addresses a TypeScript typing challenge: enforcing that all values in an object literal share a common type while preserving the specific key union for `keyof typeof`. A direct type annotation like `Record<string, OperationFn>` widens the keys to `string`, losing autocomplete and type safety for the operator prop. The solution is a constrained identity function (CIF): a generic function that accepts an object and immediately returns it, but constrains the values to a given type via `extends`. This lets TypeScript infer both the narrow keys and the desired value types from the object literal. The author demonstrates this pattern on a calculator operations object, allowing functions to be written without individual annotations while maintaining a finite union of operators. The post also explores a generic CIF factory and notes that TypeScript 4.9's `satisfies` operator offers a cleaner alternative for this use case.

- A plain type annotation like `Record<string, OperationFn>` widens `keyof typeof` to `string`, losing specific key information.
- A constrained identity function (CIF) is a generic function that returns its input while constraining the value type, preserving narrow keys inferred from object literals.
- The CIF pattern lets you enforce all operation functions have the same signature without typing each function individually.
- TypeScript 4.9 introduced `satisfies`, which solves the same problem more ergonomically.
- Generic CIFs are possible but require awkward currying; in practice writing a dedicated CIF is simple enough.