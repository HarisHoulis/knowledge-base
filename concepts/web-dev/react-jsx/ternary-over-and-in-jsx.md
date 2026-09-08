---
domain: web-dev
subdomain: react-jsx
concept: ternary-over-and-in-jsx
title: Use ternaries rather than && in JSX
sources:
  - title: "Use ternaries rather than && in JSX"
    url: "https://kentcdodds.com/blog/use-ternaries-rather-than-and-and-in-jsx"
    date: "2020-07-27"
---

# Use ternaries rather than && in JSX

The article warns against using the logical AND (`&&`) operator for conditional rendering in JSX, because of JavaScript's behavior of returning the falsy operand itself. For example, `0 && anything` evaluates to `0`, so rendering an empty contacts array with `contacts.length && contacts.map(...)` would display a stray `0` in the UI. Similarly, `undefined && component` evaluates to `undefined`, which React treats as a missing return value and throws an error. The author shares a real incident at PayPal where this bug shipped.

- Avoid using `&&` for conditional JSX because it can leak falsy values like `0` or `undefined` into the render output.
- Use ternaries (`condition ? <Component/> : null`) to explicitly control what renders in the falsy branch.
- For multiple elements, you can also use an `if` statement with a variable to make the branching clearer.
- TypeScript and the `jsx-no-leaked-render` ESLint rule can help catch accidental leaks of falsy values.
- Rendering `0` is valid in React, which makes it easy to unknowingly display unintended characters when `&&` is used with `.length` or other numeric values.