---
domain: web-dev
subdomain: react-component-patterns
concept: compound-components
title: React Hooks: Compound Components
sources:
  - title: "React Hooks: Compound Components"
    url: "https://kentcdodds.com/blog/compound-components-with-react-hooks"
    author: "Kent C. Dodds"
    date: "2019-02-18"
---

# React Hooks: Compound Components

The article explains compound components as two or more components that work together, typically parent and child, to provide an expressive and flexible API. It compares the pattern to HTML's `<select>` and `<option>`, where one component without the other would not work or make sense, and notes that compound APIs let you express relationships between components more naturally than a single component with a complex prop-based API. (kentcdodds.com/blog/compound-components-with-react-hooks)

A key aspect is implicit state: a parent component like `<select>` stores state and shares it with children so they render themselves accordingly, without that state being directly accessible in the markup. In React, the article shows this with Reach UI's `<Menu />` example, where `<Menu>`, `<MenuButton>`, `<MenuList>`, and `<MenuItem>` share implicit state and expose a readable API. (kentcdodds.com/blog/compound-components-with-react-hooks)

The article demonstrates implementing compound components using React context and hooks. A `<Toggle>` component creates `ToggleContext`, holds `on` state with `React.useState`, creates a `toggle` callback with `React.useCallback`, memoizes the context value with `React.useMemo`, and provides it through `ToggleContext.Provider`. Child components—`ToggleOn`, `ToggleOff`, and `ToggleButton`—consume the context via a custom `useToggleContext` hook, which throws if used outside `<Toggle>`. The article also mentions an alternative implementation using `React.cloneElement` and notes a custom `useEffectAfterMount` hook to avoid firing `onToggle` on initial mount. (kentcdodds.com/blog/compound-components-with-react-hooks)

- Compound components are two or more components designed to work together, usually parent and child, to create a more expressive and flexible API (e.g., `<select>` and `<option>`).
- The pattern relies on implicit state: a parent component stores shared state and makes it available to children without exposing it directly in the markup.
- A React hooks implementation can use `React.createContext`, `useState`, `useCallback`, and `useMemo` to provide shared state from a parent like `<Toggle>` to children like `<ToggleOn>`, `<ToggleOff>`, and `<ToggleButton>`.
- A custom context hook (`useToggleContext`) can enforce that compound children are rendered within the parent by throwing an error if the context is missing.
- The article references an alternative `React.cloneElement` approach and uses a custom `useEffectAfterMount` hook to avoid calling the toggle callback on initial mount.