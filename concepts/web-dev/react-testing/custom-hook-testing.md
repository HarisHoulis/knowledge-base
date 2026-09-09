---
domain: web-dev
subdomain: react-testing
concept: custom-hook-testing
title: How to test custom React hooks
sources:
  - title: "How to test custom React hooks"
    url: "https://kentcdodds.com/blog/how-to-test-custom-react-hooks"
    date: "2020-03-22"
---

# How to test custom React hooks

The article explains that testing reusable custom React hooks requires simulating how they are actually used, i.e. inside a component, because hooks can only be called in a React component body. Directly invoking a hook in a test throws an invalid hook call error, and mocking the built-in React hooks is discouraged because it undermines the test's ability to verify real behavior. The author recommends writing tests that mirror manual usage by rendering a component that consumes the hook and interacting with that component (source: https://kentcdodds.com/blog/how-to-test-custom-react-hooks).

- Custom hooks are not pure functions; they must be tested through a React component context.
- Mocking built-in React hooks reduces confidence and should be avoided.
- For a straightforward hook, render a wrapper component that uses the hook and interact with its DOM.
- When a UI wrapper is awkward, use a small test component with act() to inspect the hook's returned values.
- @testing-library/react's renderHook offers a clean API to test hook logic by exposing result.current and supporting act() updates.