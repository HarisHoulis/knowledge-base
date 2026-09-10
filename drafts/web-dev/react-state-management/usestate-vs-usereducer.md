---
domain: web-dev
subdomain: react-state-management
concept: usestate-vs-usereducer
title: Should I useState or useReducer?
sources:
  - title: "Should I useState or useReducer?"
    url: "https://kentcdodds.com/blog/should-i-usestate-or-usereducer"
    author: "Kent C. Dodds"
    date: "2020-03-09"
---

# Should I useState or useReducer?

The article frames `useState` and `useReducer` as two tools with different trade-offs, not as old versus new APIs. The choice depends on the situation, and an application may use both (source).

In the `useDarkMode` example, the `useState` implementation is much simpler. A typical Redux-style `useReducer` version is verbose, and simplifying it essentially reimplements `useState`; the article concludes that for an independent piece of state, `useState` is the better solution (source).

In the `useUndo` example, the original `useState` version with separate `past`, `present`, and `future` states and memoized callbacks can create stale closure bugs. Adding `set` to effect dependencies can even cause an infinite loop because `set` changes when `past` or `present` changes. The fix is to store state in a single object and use functional updates, removing those dependencies (source).

The `useReducer` version of `useUndo` centralizes `UNDO`, `REDO`, `SET`, and `RESET` transitions in a reducer. This avoids stale closure issues and keeps complex, interrelated state logic in one place (source).

- `useState` and `useReducer` are both valid; choose based on trade-offs rather than treating one as newer or better.
- For simple, independent state such as dark mode, `useState` is simpler and clearer.
- For complex, interrelated state transitions such as undo/redo, `useReducer` can prevent stale closure bugs and centralize logic.
- Combining state into one object and using functional updates can fix stale closure and dependency issues in `useState`.
- Typical Redux-style reducers can be verbose; simplifying them may just reimplement `useState`.