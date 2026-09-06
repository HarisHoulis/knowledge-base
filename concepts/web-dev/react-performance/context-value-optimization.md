---
domain: web-dev
subdomain: react-performance
concept: context-value-optimization
title: How to optimize your context value
sources:
  - title: "How to optimize your context value"
    url: "https://kentcdodds.com/blog/how-to-optimize-your-context-value"
    author: "Kent C. Dodds"
    date: "2021-03-08"
---

# How to optimize your context value

Kent C. Dodds explains when optimizing React context values is actually necessary: when the context value changes frequently, there are many consumers, React.memo is being used because things are slow, and performance has been measured. Otherwise, React is fast enough and adding complexity is wasteful. The recommended solution is to split state and dispatch into separate context providers, using useReducer or useState, so components that only need the updater function don't re-render when state changes. This avoids the need for useMemo entirely and is simpler than more complex memoization patterns. The author notes this API can be annoying and offers a convenience hook, but warns that using it loses the performance benefit for components that only need one part.

- Only optimize context values when you have measured performance problems: frequent value changes, many consumers, and React.memo in use.
- Put state in one context provider and dispatch in another to avoid re-rendering components that only use the updater.
- This approach avoids needing useMemo and is simpler than the original recommendation.
- A combined useCount() hook is possible but loses the performance benefits if components only need one piece.
- Avoid premature optimization; React is fast and complexity should be spent wisely.