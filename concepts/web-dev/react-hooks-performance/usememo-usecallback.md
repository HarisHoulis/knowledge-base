---
domain: web-dev
subdomain: react-hooks-performance
concept: usememo-usecallback
title: When to useMemo and useCallback
sources:
  - title: "When to useMemo and useCallback"
    url: "https://kentcdodds.com/blog/usememo-and-usecallback"
    author: "Kent C. Dodds"
    date: "2019-06-04"
---

# When to useMemo and useCallback

The article uses a candy dispenser example to argue that wrapping `dispense` in `React.useCallback` is actually worse for performance because it does more work per render: defining the function, defining the dependency array, and calling the hook (source). It also notes that the original function can be garbage collected on subsequent renders, while the `useCallback` version may retain previous function references, making memory use worse. `useMemo` is similar but can memoize any value; memoizing simple values like `initialCandies` is not worth the added complexity or cost (source).

The article identifies two legitimate reasons for these hooks: referential equality and computationally expensive calculations (source). Referential equality matters because objects, arrays, and functions created inside a component are new every render, so using them in dependency arrays causes effects to re-run every render. `useCallback` and `useMemo` can stabilize references, especially when passing non-primitive props to components wrapped in `React.memo`, which otherwise re-render unnecessarily (source). However, the article warns that most unnecessary re-renders should not be optimized, and `React.memo`-style optimizations should not be used without measuring because they come with costs and can be tricky to get right (source).

`useMemo` is also useful for expensive synchronous calculations: React calls the memoized function only when dependencies change and returns cached previous values for the same inputs (source). The overall message is that performance optimizations are not free—they always have a cost but do not always provide a benefit—so developers should optimize responsibly and apply the AHA Programming principle, waiting until the abstraction/optimization is clearly needed (source).

- `useCallback` and `useMemo` add overhead and are not automatically performance wins; in simple cases they can be worse than plain function definitions (source).
- Use them for referential equality: stabilizing objects, arrays, or functions used in dependency arrays or passed as props to `React.memo` components (source).
- Use `useMemo` for computationally expensive calculations so the value is recomputed only when dependencies change (source).
- Avoid optimizing unnecessary re-renders and avoid `React.memo`/`PureComponent`/`shouldComponentUpdate` without measuring, because these optimizations have costs and may not help (source).
- Performance optimizations are not free; optimize responsibly and wait until the optimization is clearly needed (source).