---
domain: web-dev
subdomain: React
concept: react-hooks-vs-render-props
title: React Hooks: What's going to happen to render props?
sources:
  - title: "React Hooks: What's going to happen to render props?"
    url: "https://kentcdodds.com/blog/react-hooks-whats-going-to-happen-to-render-props"
    author: "Kent C. Dodds"
    date: "2018-12-10"
---

# React Hooks: What's going to happen to render props?

React Hooks and render props share the same primary use case: sharing React component logic. In the article, Kent C. Dodds argues that hooks are simpler than class components plus render props by comparing react-toggled's render-prop Toggle with a useToggle hook implementation. The hook version reduces usage to `const { on, toggle } = useToggle()`, and additional helpers like `getTogglerProps` can be split into separate hooks for tree-shaking (source).

Existing render-prop APIs do not need to be abandoned immediately. Dodds shows a migration path: a render-prop component can be implemented in one line as `const Toggle = ({ children, ...props }) => children(useToggle(props))`, allowing teams to keep their current API and migrate over time. He also notes this approach is useful for testing custom hooks, though closures introduce testing nuances (source).

Render props will remain useful for inversion of control. The example of react-virtualized's `rowRenderer` prop shows a render prop delegating row rendering to the user; rewriting it to use hooks may not offer a clear benefit over the current API. Thus render props and this style of inversion of control are here to stay for such cases (source).

At the time, hooks were in alpha and subject to change, but they were opt-in and would not require breaking changes to React's API. Dodds advises against rewriting apps, recommending refactoring once hooks are stable (source).

- Hooks simplify logic reuse compared with class components and render props, as shown by `useToggle` vs the `Toggle` render-prop component.
- Render-prop components can be preserved by wrapping a hook: `const Toggle = ({ children, ...props }) => children(useToggle(props))`.
- Splitting hook utilities can enable tree-shaking of unused helpers like `getTogglerProps`.
- Render props remain valuable for inversion-of-control cases such as react-virtualized's `rowRenderer`.
- At publication, React Hooks were alpha, opt-in, and not requiring breaking API changes; refactor after stable rather than rewrite.