---
domain: web-dev
subdomain: react
concept: react-context-api-migration
title: Migrating to React's New Context API
sources:
  - title: "Migrating to React's New Context API"
    url: "https://kentcdodds.com/blog/migrating-to-reacts-new-context-api"
    author: "Kent C. Dodds"
    date: "2018-04-23"
---

# Migrating to React's New Context API

The article describes migrating compound components from React’s legacy context API to the official context API released in React 16.3.0 [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api). The old API required string keys, `childContextTypes`/`getChildContext`, and static `contextTypes` on consumers; the author disliked the indirection of strings and attaching static properties [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api). It also did not allow context values to be updated through a `shouldComponentUpdate` that returned `false` [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api).

In the new API, `React.createContext` returns a context object with `Provider` and `Consumer` components. Providers pass values explicitly, and consumers use a render-prop API, which the author finds composable and simpler than the old string-based indirection [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api). The new API also handles updates through `shouldComponentUpdate` returning `false` [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api).

A common pitfall is passing a new object to `Provider`’s `value` on every render, such as `value={{on: this.state.on, toggle: this.toggle}}`, because that re-renders all consumers even if state did not change [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api). The author recommends providing a value that only changes when state changes, for example `value={this.state}`, and notes that putting the `toggle` method into state feels odd but is not a big deal [source](https://kentcdodds.com/blog/migrating-to-reacts-new-context-api).

- React 16.3 introduced an official context API, replacing the legacy string-based context API.
- Old context required `childContextTypes`, `getChildContext`, and consumer `contextTypes`, and had problems with updates when `shouldComponentUpdate` returned `false`.
- The new API uses `React.createContext` with `Provider` and render-prop `Consumer` components, removing string indirection and enabling composability.
- Avoid creating a new object for the `Provider` `value` prop on every render, since it re-renders all consumers; use a value that changes only when needed.