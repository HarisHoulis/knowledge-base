---
domain: web-dev
subdomain: react-state-management
concept: state-colocation
title: State Colocation will make your React app faster
sources:
  - title: "State Colocation will make your React app faster"
    url: "https://kentcdodds.com/blog/state-colocation-will-make-your-react-app-faster"
    author: "Kent C. Dodds"
    date: "2019-09-23"
---

# State Colocation will make your React app faster

State colocation means placing state as close to where it is relevant as possible [1]. The article argues that one of the leading causes of slow React apps is global state, especially rapidly changing global state: when state is managed high in the component tree, every update invalidates the entire React tree, so React must check all components for DOM updates [1]. Moving state down—such as moving the dog name state into `DogName`—lets React skip unrelated slow components entirely because they cannot reference the changed state [1].

Real-world cases include putting too much state in Redux or global context, such as input state or tooltip visibility [1]. Debouncing user input can help but hurts UX, and applying `React.memo`/`useMemo`/`useCallback` everywhere adds complexity and still requires a top-down render pass [1]. Instead, put state at the closest common parent when multiple components need it, and keep context providers as close to relevant components as possible [1]. Redux can still be used, but should be limited to actual global state [1].

The article provides a decision tree: start with `useState`; if only one component uses it, leave it; if one child uses it, colocate; if a sibling/parent uses it, lift; if prop drilling becomes a problem, move state to a context provider or use component composition; revisit as requirements change [1].

- Rapidly changing global state causes broad re-renders and performance issues because React must check the entire tree on each update.
- Colocate state as close as possible to where it is used; when multiple components need it, place it at the closest common parent.
- Colocation reduces React's work and improves maintainability compared with lifting all state.
- Avoid putting all state in Redux or global context; reserve global stores for actual global state.
- Memoization approaches like `React.memo`/`useMemo`/`useCallback` can add complexity and are less effective than colocating state.