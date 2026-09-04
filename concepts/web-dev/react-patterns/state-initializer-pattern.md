---
domain: web-dev
subdomain: react-patterns
concept: state-initializer-pattern
title: The State Initializer Pattern
sources:
  - title: "The State Initializer Pattern"
    url: "https://kentcdodds.com/blog/the-state-initializer-pattern"
    date: "2021-11-05"
---

# The State Initializer Pattern

The state initializer pattern allows React component consumers to set the initial state via a prop, such as `initialCount`, and to reset the component to that initial state at any time without unmounting/remounting. It resembles the `defaultValue` prop in HTML inputs, but the author prefers the `initial` prefix for clarity. The core implementation is simply to accept an initial value prop, pass it to `useState`, and use it in the reset handler.

- The pattern exposes an optional 'initial*' prop to initialize and reset component state.
- To avoid reacting to prop changes after mount, capture the initial value once using `useRef`, `useState`, or `useReducer`.
- The built-in `key` prop can also reset state by forcing a remount, but that may skip animations and trigger cleanup callbacks.
- The state initializer pattern is preferable when preserving component state animations or avoiding remount side effects is desired.