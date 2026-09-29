---
domain: web-dev
subdomain: react-performance
concept: react-render-optimization
title: Optimize React Re-renders by Passing Elements as Props
sources:
  - title: "One simple trick to optimize React re-renders"
    url: "https://kentcdodds.com/blog/optimize-react-re-renders"
    author: "Kent C. Dodds"
    date: "2019-06-24"
---

# Optimize React Re-renders by Passing Elements as Props

When React re-renders a parent, it creates new React element objects and new props objects for its children. This means a child component like `Logger` will re-render on every parent render even if its props values are unchanged, because the props object itself has changed. The article demonstrates this with a `Counter` and `Logger` example: clicking the button logs `counter rendered` each time because the parent recreates the `Logger` element and its props object (Kent C. Dodds, 2019).

A simple optimization is to create the expensive child element once in a parent that renders less often, then pass that element down as a prop. In the second example, `Counter` receives `logger={<Logger label="counter" />}` from `ReactDOM.render`, so the `Logger` element and its props object stay identical between renders. React can then bail out of re-rendering that subtree, similar to `React.memo` but checking the props object holistically (Kent C. Dodds, 2019).

The practical takeaway: if you have performance issues, “lift” the expensive component to a parent where it will render less often, then pass it down as a prop. This often solves the problem without spreading `React.memo` throughout the codebase. The author notes this does not fix slow initial renders or necessary top-down re-renders; those should be addressed separately. Also, legacy context prevents this optimization, so migrating away from legacy context is recommended for performance (Kent C. Dodds, 2019).

- React creates new element and props objects on every render, causing child components to re-render even when their prop values are unchanged.
- Passing a pre-created element as a prop keeps the element identity and props object stable, allowing React to skip re-rendering that subtree.
- Practical pattern: lift expensive components to a parent that renders less often and pass them down as props instead of wrapping everything in `React.memo`.
- This optimization does not address slow initial renders or re-renders that genuinely need to happen; handle those separately.
- Legacy context disables this optimization, so migrating from legacy context is advisable for performance.