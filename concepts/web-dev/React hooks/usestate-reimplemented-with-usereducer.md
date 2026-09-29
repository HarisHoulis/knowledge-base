---
domain: web-dev
subdomain: React hooks
concept: usestate-reimplemented-with-usereducer
title: How to Implement useState with useReducer
sources:
  - title: "How to implement useState with useReducer"
    url: "https://kentcdodds.com/blog/how-to-implement-usestate-with-usereducer"
    author: "Kent C. Dodds"
    date: "2019-08-30"
---

# How to Implement useState with useReducer

Kent C. Dodds demonstrates re-implementing React's `useState` hook on top of `useReducer` as a learning exercise. He notes that React itself builds `useState` from the same code as `useReducer`, exposing the simpler API because managing a single state value is very common, while `useReducer` would require more boilerplate for that case.

The article first enumerates the `useState` API that must be supported: calling it with no arguments, a literal initial value, or a lazy initializer function; and the updater accepting either a new state value or a function of the previous state. He then reviews the `useReducer` API, whose lazy-initialization form takes a reducer, an `initialArg`, and an initialization function.

The implementation proceeds incrementally. The reducer first just returns the dispatch argument as the new state, then adds a `typeof` check so function updaters receive the previous state. Initialization is handled by passing the initial value as `initialArg` to an initializer that returns it, and finally the initializer adds its own `typeof` check to support lazy initialization by calling the value if it is a function.

The final `useState` is a thin wrapper returning `React.useReducer(useStateReducer, initialValue, useStateInitializer)`. Dodds concludes that readers should keep using the built-in `useState`, but the exercise shows how flexible `useReducer` is.

- React implements `useState` using the same underlying code as `useReducer`; `useState` is the simpler API for the common single-value case.
- The re-implementation must support three call forms: no initial value, a literal initial value, and a lazy initializer function (`useState(() => initialValue)`).
- The updater must support both `setState(newState)` and `setState(prev => newState)`, achieved in the reducer with `typeof newState === 'function' ? newState(prevState) : newState`.
- `useReducer`'s third argument enables lazy initialization: the initial value is passed as `initialArg` to an initializer that calls it if it is a function.
- Dodds recommends continuing to use the built-in `useState` in practice, while noting how flexible `useReducer` is.