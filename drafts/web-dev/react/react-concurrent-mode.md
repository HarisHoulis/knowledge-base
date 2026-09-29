---
domain: web-dev
subdomain: react
concept: react-concurrent-mode
title: How to Enable React Concurrent Mode
sources:
  - title: "How to Enable React Concurrent Mode"
    url: "https://kentcdodds.com/blog/how-to-enable-react-concurrent-mode"
    author: "Kent C. Dodds"
    date: "2019-11-04"
---

# How to Enable React Concurrent Mode

React's experimental Concurrent Mode was published in the experimental release channel, which does not honor semver and may contain bugs ([How to Enable React Concurrent Mode](https://kentcdodds.com/blog/how-to-enable-react-concurrent-mode)). To try it, install `react@experimental` and `react-dom@experimental`, then verify your app, build, tests, and type checking still work before making any other change.

To enable Concurrent Mode, replace `ReactDOM.render(<App />, rootEl)` with `ReactDOM.unstable_createRoot(rootEl).render(<App />)`. After that, verify everything still works; new console errors may be React bugs or may come from unsupported features such as String Refs, Legacy Context, `findDOMNode`, or lifecycle methods with the `unsafe_` prefix.

Concurrent Mode primarily enables time slicing and Suspense for asynchronous operations. The source demonstrates a Suspense experiment using `React.unstable_useTransition`, `React.Suspense`, an error boundary, and a resource that throws a promise, but warns that the Suspense API is low-level and likely to change.

For production, the article recommends undoing all changes and restoring stable React and `ReactDOM.render`, because shipping experimental software as foundational as React is ill-advised. It also recommends enabling Strict Mode incrementally as a prerequisite, since apps that do not pass Strict Mode are unlikely to work well in Concurrent Mode.

- Concurrent Mode is experimental, does not honor semver, and may have bugs, so it should be tried carefully ([How to Enable React Concurrent Mode](https://kentcdodds.com/blog/how-to-enable-react-concurrent-mode)).
- Enable it by installing `react@experimental` and `react-dom@experimental`, then replacing `ReactDOM.render` with `ReactDOM.unstable_createRoot(rootEl).render(<App />)`.
- After enabling, unsupported features such as String Refs, Legacy Context, `findDOMNode`, and `unsafe_` lifecycle methods may cause breakage.
- Concurrent Mode enables time slicing and Suspense for async UI, but the Suspense APIs shown are low-level and experimental.
- For production, undo experimental changes and consider enabling Strict Mode incrementally first.