---
domain: web-dev
subdomain: react-state-management
concept: react-context-api
title: React's New Context API
sources:
  - title: "React's ⚛️ new Context API"
    url: "https://kentcdodds.com/blog/reacts-new-context-api"
    author: "Kent C. Dodds"
    date: "2018-02-05"
---

# React's New Context API

The article is now marked historical, noting that context isn't "new" and hooks offer better usage, but it explains React's new Context API as a solution to prop drilling: passing state from the top of a React tree to nested components without threading props through uninterested components (Kent C. Dodds, 2018).

The API consists of three parts: `React.createContext(initialValue)` returns an object with `Provider` and `Consumer`; the `Provider` accepts a `value` prop; and the `Consumer` requires a `children` function that receives the value and returns React elements. It was positioned as a first-class feature, unlike the old experimental context API that was warned against. The article notes that libraries like react-redux, MobX-react, React Router, and glamorous already use context internally (Kent C. Dodds, 2018).

For practical use, nested providers and consumers can be composed via utility components to reduce render-prop nesting. At publication, the new API was unreleased and planned for the next minor React release; the old context API would continue until the next major release, and a codemod was likely (Kent C. Dodds, 2018).

- The new Context API solves prop drilling by letting a Provider pass data to any Consumer below it in the tree.
- `React.createContext` returns a `Provider` and `Consumer`; the Provider takes a `value` prop, and the Consumer uses a function-as-children render prop.
- The old context API was experimental and discouraged; the new version was intended to become a first-class React feature.
- Popular libraries such as react-redux, MobX-react, React Router, and glamorous already rely on context internally.
- Compose providers/consumers with utility components to reduce nesting; the old API was slated to work until the next major React release, with a likely codemod.