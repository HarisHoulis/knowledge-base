---
domain: web-dev
subdomain: react-typescript
concept: typed-react-components
title: How to write a React Component in TypeScript
sources:
  - title: "How to write a React Component in TypeScript"
    url: "https://kentcdodds.com/blog/how-to-write-a-react-component-in-typescript"
    date: "2021-03-04"
---

# How to write a React Component in TypeScript

The article discusses how to properly type React components in TypeScript. It critiques the common use of React.FC (or React.FunctionComponent) for typing function components, pointing out that it adds an unnecessary children prop, does not support generics, and forces function expressions. Instead, the recommended approach is to treat a React component as a regular function and type its props directly, using function declarations with a props type annotation.

As a practical example, the author builds a Calculator component and refines its props type. He notes that the operator prop should not be a generic string but a union of allowed operations. To avoid duplicating the operation keys, he derives the type using `keyof typeof operations`, which ensures the prop stays in sync with the operations object. This leads to better type safety and maintainability.

- Avoid using React.FC or React.FunctionComponent for typing React components because it automatically allows children, does not support generics, and requires function expressions.
- Type props directly on the function parameters of a function declaration, e.g., `function Calculator({ left, operator, right }: CalculatorProps)`.
- Use `keyof typeof` to derive union types from an object, preventing duplication and keeping the prop type in sync with the implementation.
- Rely on TypeScript's inference for return types of components instead of specifying them explicitly unless necessary.