---
domain: web-dev
subdomain: react-hooks
concept: array-destructuring
title: React Hooks: Array Destructuring Fundamentals
sources:
  - title: "React Hooks: Array Destructuring Fundamentals"
    url: "https://kentcdodds.com/blog/react-hooks-array-destructuring-fundamentals"
    author: "Kent C. Dodds"
    date: "2018-12-31"
---

# React Hooks: Array Destructuring Fundamentals

The `const [count, setCount] = useState(0)` line from React's Hooks docs uses JavaScript array destructuring, an ES6 feature, rather than React-specific syntax (source). The author argues that understanding an abstraction makes you more effective at using it, and suggests inspecting unfamiliar syntax in AST Explorer—where it appears as an `ArrayPattern`—then looking it up on MDN (source).

Array destructuring is syntactic sugar. Babel compiles it by assigning `useState`'s return value to a temporary variable and reading values by index; with Babel's "Loose" env preset, that output simplifies to direct indexed assignments (source). The article shows you can rename destructured values, pull more or fewer elements, skip positions with commas, and provide default values for `undefined` elements (source). Most of these variations are unnecessary with `useState` because it reliably returns an array of two elements (source).

`useState` is implemented in `react-dom` and delegates to the current renderer; its implementation calls `useReducer` with `basicStateReducer`, and `useReducer` returns `[newState, dispatch]` (source). That array return is what enables the ergonomic destructuring into a state value and an updater function (source).

- `const [count, setCount] = useState(0)` uses ES6 array destructuring, not a React-specific language feature.
- Babel desugars array destructuring into a temporary variable plus indexed access; the "Loose" preset simplifies the output further.
- Destructuring supports renaming, omitting elements, skipping with commas, and defaults for `undefined` values.
- `useState` is implemented via `useReducer` and returns an array `[newState, dispatch]`, which is why it can be destructured into state and updater.