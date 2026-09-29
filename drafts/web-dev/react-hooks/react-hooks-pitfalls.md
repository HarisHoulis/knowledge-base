---
domain: web-dev
subdomain: react-hooks
concept: react-hooks-pitfalls
title: 5 Tips to Help You Avoid React Hooks Pitfalls
sources:
  - title: "5 Tips to Help You Avoid React Hooks Pitfalls"
    url: "https://kentcdodds.com/blog/react-hooks-pitfalls"
    author: "Kent C. Dodds"
    date: "2019-08-05"
---

# 5 Tips to Help You Avoid React Hooks Pitfalls

The article introduces React Hooks, released in February 2019, as a feature that simplifies state and side-effect management but requires a shift in how developers think about React component lifecycles, state, and side effects (source). It lists five common pitfalls and advises reading the React Hooks documentation and FAQ before starting, and installing and following the `eslint-plugin-react-hooks` rules, especially the exhaustive deps rule, which catches real bugs such as stale effects and stale closures (source).

A key recommendation is to stop thinking in lifecycles and instead think about synchronizing side effects with application state. The article shows a `DogInfo` example where an empty dependency array causes a fetch not to rerun when `dogId` changes; including `dogId` in the dependency array fixes the bug. The takeaway is that dependencies should be included not because an effect runs “on mount,” but because the effect’s logic should never get stale (source).

The article also warns against overthinking performance and testing. Functions redefined on each render are usually cheap to create, and unnecessary re-renders are not necessarily bad because React avoids DOM updates when possible; React is fast by default, so optimize only after measuring. For tests, avoid testing implementation details like component state or instances, and instead interact with what is rendered, so refactoring components from classes to hooks does not break user-facing tests (source).

- Read the React Hooks docs and FAQ first to build a solid conceptual foundation.
- Install and follow `eslint-plugin-react-hooks`, especially the exhaustive deps rule; disabling it should be a rare escape hatch.
- Think in terms of synchronizing side effects to state rather than lifecycle methods, and include dependencies to avoid stale closures and missed updates.
- React is fast by default; investigate slow renders before applying `React.memo`, `useMemo`, or `useCallback` prematurely.
- Avoid testing implementation details; test what the user sees and interacts with so hook refactors do not force unnecessary test rewrites.