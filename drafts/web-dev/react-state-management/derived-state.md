---
domain: web-dev
subdomain: react-state-management
concept: derived-state
title: Don't Sync State. Derive It!
sources:
  - title: "Don't Sync State. Derive It!"
    url: "https://kentcdodds.com/blog/dont-sync-state-derive-it"
    author: "Kent C. Dodds"
    date: "2019-09-30"
---

# Don't Sync State. Derive It!

React state often includes values that can be calculated from other state. In a tic-tac-toe example, `squares` is source state, while `nextValue`, `winner`, and `status` are derived: they can be computed with `calculateNextValue`, `calculateWinner`, and `calculateStatus` rather than stored in separate `useState` calls. Managing them as state requires updating every derived value whenever `squares` changes, which risks values falling out of sync, especially when adding features like selecting two squares at once [1].

Reducing duplication with a single `setNewState` helper improves things, but the better solution is to derive values during render: `const nextValue = calculateNextValue(squares)`, etc. Then no synchronization is needed, and new behaviors only update `squares`. `useReducer` centralizes updates in a reducer so derived state is less likely to fall out of sync, but the author finds it more complex than direct derivation for this case [1].

The same principle applies when source state comes from props: instead of `useEffect` or render-time state setters, calculate derived values on the fly. Performance is usually not a concern; the author benchmarks `calculateWinner` at millions of operations per second and recommends `useMemo` only for computationally expensive functions after measuring. For broader needs, Reselect provides memoization, and MobX computed values offer lazily evaluated derived state [1].

- Derive computed values from source state during render instead of syncing separate state variables.
- State synchronization risks out-of-sync state, especially as features multiply.
- useReducer centralizes updates, but direct derivation is simpler for cases like tic-tac-toe.
- Derived state via props should be calculated on the fly, not synchronized with effects or render-time setters.
- JavaScript is fast; use useMemo only after measuring, and consider Reselect or MobX for memoized/lazy derived state.