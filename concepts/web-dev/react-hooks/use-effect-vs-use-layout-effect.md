---
domain: web-dev
subdomain: react-hooks
concept: use-effect-vs-use-layout-effect
title: useEffect vs useLayoutEffect
sources:
  - title: "useEffect vs useLayoutEffect"
    url: "https://kentcdodds.com/blog/useeffect-vs-uselayouteffect"
    date: "2020-12-01"
---

# useEffect vs useLayoutEffect

Kent C. Dodds explains the difference between useEffect and useLayoutEffect in React. useEffect is the default hook for side effects; it runs after the browser paints, meaning it does not block visual updates. Code that previously lived in componentDidMount, componentDidUpdate, and componentWillUnmount should typically go into useEffect for performance reasons (url: https://kentcdodds.com/blog/useeffect-vs-uselayouteffect).

useLayoutEffect, on the other hand, runs synchronously immediately after React performs DOM mutations but before the browser paints. This is the correct choice when an effect mutates the DOM and that mutation would cause a visible flicker if done after paint. It is also needed for tasks like measuring the DOM or triggering a synchronous re-render, and it behaves like componentDidMount/componentDidUpdate in scheduling (url: https://kentcdodds.com/blog/useeffect-vs-uselayouteffect).

The article also highlights a special ordering case where updating a ref in useEffect may be stale for code in another useEffect because hooks run in order; useLayoutEffect can be used to guarantee the ref is set before other synchronous code runs (url: https://kentcdodds.com/blog/useeffect-vs-uselayouteffect).

- Use useEffect as the default for most effects; it runs after render and does not block the browser from painting.
- Use useLayoutEffect when an effect mutates the DOM and the mutation could visibly change appearance before the browser paints.
- useLayoutEffect runs synchronously after DOM mutations and before paint, making it suitable for measurements and synchronous re-renders.
- For ref updates that must be visible to other code running earlier, use useLayoutEffect to avoid stale values.