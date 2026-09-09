---
domain: web-dev
subdomain: react
concept: interaction-tracing
title: Tracing user interactions with React
sources:
  - title: "Tracing user interactions with React"
    url: "https://kentcdodds.com/blog/tracing-user-interactions-with-react"
    author: "Kent C. Dodds"
    date: "2020-05-08"
---

# Tracing user interactions with React

This post explains React's experimental interaction tracing API, which adds user-interaction context to performance data collected via the `Profiler` component. By using `unstable_trace` from `scheduler/tracing`, developers can wrap state updates so that the resulting render commits are associated with a named interaction (e.g., 'form submitted'). This helps answer questions like whether a dropdown update is fast on a click but slow on a type. The `Profiler`'s `onRender` callback receives an `interactions` property containing this information, and the React DevTools Profiler can visualize these interactions.

- Use `unstable_trace(id, performance.now(), callback)` to associate a state update with a named user interaction.
- For asynchronous workflows, wrap the success callback (or continuation) with `unstable_wrap` so both the initial and subsequent state updates remain tied to the same interaction.
- Interaction tracing is experimental and provides context for Profiler measurements, making it easier to see which user actions caused slow renders.
- The API was removed in React 17, so this article is archived and the technique no longer applies to current React versions.