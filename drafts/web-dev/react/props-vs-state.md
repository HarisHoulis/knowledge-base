---
domain: web-dev
subdomain: react
concept: props-vs-state
title: React Fundamentals: Props vs State
sources:
  - title: "React Fundamentals: Props vs State"
    url: "https://kentcdodds.com/blog/props-vs-state"
    author: "Kent C. Dodds"
    date: "2019-07-08"
---

# React Fundamentals: Props vs State

React components are functions that return renderable output, and props are an object of arbitrary inputs passed as the first argument, analogous to function arguments. JSX attributes supply props, which can be numbers, strings, arrays, objects, functions, etc. Props are read-only: attempting to mutate them raises a TypeError, so defaults should be handled with local variables or destructuring defaults (source).

State is data that changes over the lifetime of a specific component instance. When a value must change dynamically and trigger a re-render, such as an input-controlled number, state is appropriate. React state is updated via useState; React does not know about direct prop mutation, and props cannot be changed anyway (source).

State can be initialized from props, but if a prop value is only used as the initial state, the article recommends naming it with an initial prefix, e.g. initialN2, to signal that later prop changes will not affect state. To respond to prop changes, lift state up (source).

Conclusion: props are arguments or inputs passed to a component; state is managed within the component and can change over time. The article presents this as a foundational React distinction (source).

- Props are analogous to function arguments and are passed to React components as a single object via JSX attributes.
- Props are immutable; React will throw if you try to assign to a prop, so use local values or destructuring defaults for defaults.
- State is data that changes over the component instance's lifetime and is used for values that need to trigger re-renders.
- State can be initialized from props; name such props with an initial prefix to indicate they will not update state after initialization.
- To reflect prop changes in state, lift state up.