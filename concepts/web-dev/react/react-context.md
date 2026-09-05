---
domain: web-dev
subdomain: react
concept: react-context
title: How to use React Context effectively
sources:
  - title: "How to use React Context effectively"
    url: "https://kentcdodds.com/blog/how-to-use-react-context-effectively"
    date: "2021-06-05"
---

# How to use React Context effectively

Kent C. Dodds explains how to create and consume React Context effectively, building on his earlier advice that context should not be used for every state-sharing problem. He advocates creating a custom provider component and a custom consumer hook (e.g., `useCount`) rather than exposing the raw Context object. This improves developer experience and maintainability by failing fast with a helpful error message when a hook is used outside its provider, and by enabling TypeScript to avoid undefined checks.

He demonstrates a pattern where `CountProvider` uses `useReducer` to manage state and provides a value of `{ state, dispatch }`. A custom hook `useCount` calls `React.useContext` and throws an error if the context is undefined. He also covers how to support class components with a custom consumer component if hooks are unavailable, and discusses handling async actions via helper functions that accept `dispatch` rather than using action creators. The final code intentionally does not export the raw context object, ensuring only the intended provider and consumer APIs are used.

- Don't reach for Context to solve every state-sharing problem; it can be scoped to parts of the tree and multiple separate contexts are recommended.
- Create a custom provider component and a custom hook (e.g., `useCount`) instead of directly exporting the raw context object.
- Throw an error inside the custom hook when context is undefined to fail fast and prevent silent runtime issues.
- With TypeScript, define the context type as `{ state, dispatch } | undefined` so the custom hook provides type-safe access without extra checks.
- For async actions, create helper functions that accept `dispatch` and orchestrate the sequence of dispatches.