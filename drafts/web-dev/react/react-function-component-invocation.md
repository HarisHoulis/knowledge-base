---
domain: web-dev
subdomain: react
concept: react-function-component-invocation
title: Don't call a React function component
sources:
  - title: "Don't call a React function component"
    url: "https://kentcdodds.com/blog/dont-call-a-react-function-component"
    author: "Kent C. Dodds"
    date: "2019-12-08"
---

# Don't call a React function component

The article explains why calling a React function component directly—such as `items.map(Counter)`—can trigger the error `React Error: Rendered fewer hooks than expected` (Kent C. Dodds, 2019). React does not treat a directly invoked function as its own component instance, so hooks inside it are registered against the parent component. When the list changes, the number and order of hooks seen by that parent can change, violating the Rules of Hooks.

Refactoring the call into an inline function that uses `useState` reveals the same issue: hooks are always called for the parent `App` component, not for a separate `Counter` component (Kent C. Dodds, 2019). Conditional hook calls, like placing `useEffect` inside an `if`, produce the same class of error because hooks must be called the same number of times for a given component.

To fix it, render components with JSX or `React.createElement` instead of calling them, e.g. `items.map(i => <Counter key={i.id} />)` (Kent C. Dodds, 2019). This gives React a component instance to associate hooks with. The article notes that direct invocation may sometimes appear to work, but the hooks are still attached to the parent instance and can behave unexpectedly.

- Calling a function component directly, like `items.map(Counter)`, runs its hooks against the parent component instance rather than a separate `Counter` instance.
- This can cause `React Error: Rendered fewer hooks than expected` because hook order/count for the parent may change between renders.
- Conditionally calling hooks, such as `useEffect` inside an `if`, violates the Rules of Hooks for the same underlying reason.
- Render components with JSX or `React.createElement` instead of invoking them directly, e.g. `items.map(i => <Counter key={i.id} />)`.
- Direct invocation may sometimes appear to work, but hooks attach to the parent component and can lead to unexpected behavior.