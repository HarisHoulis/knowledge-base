---
domain: web-dev
subdomain: react-hooks
concept: use-state-lazy-initialization-and-function-updates
title: useState lazy initialization and function updates
sources:
  - title: "useState lazy initialization and function updates"
    url: "https://kentcdodds.com/blog/use-state-lazy-initialization-and-function-updates"
    date: "2020-08-03"
---

# useState lazy initialization and function updates

React's useState hook can take a function for lazy initialization, allowing expensive or I/O-based initial state calculations to run only on the initial render. This avoids unnecessary work on every re-render, since the function is only called when React needs the initial state. The author notes this is a performance optimization used sparingly, but it's valuable for scenarios like reading from localStorage or complex computations.

The dispatch function returned by useState also supports passing an updater function that receives the previous state. This is essential when state updates depend on stale values, especially after asynchronous operations. Without function updates, closures can cause multiple rapid updates to use the same stale count, resulting in incorrect state. Using `setCount(prev => prev + 1)` ensures each update is based on the latest state, regardless of render timing. The author emphasizes that any time new state is computed from previous state, a function update should be used, and notes that useReducer inherently avoids this problem.

- Lazy initialization: pass a function to useState to defer expensive initial state computation until the first render.
- Function updates: pass a function to the state setter to reliably compute new state from the previous state.
- Avoid stale closures: asynchronous handlers can close over old state values; function updaters solve this by receiving the current state.
- useReducer automatically provides the latest state to reducers, avoiding stale state issues for most cases.