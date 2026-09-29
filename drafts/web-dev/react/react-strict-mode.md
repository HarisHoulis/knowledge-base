---
domain: web-dev
subdomain: react
concept: react-strict-mode
title: How to Enable React Strict Mode
sources:
  - title: "How to Enable React Strict Mode"
    url: "https://kentcdodds.com/blog/react-strict-mode"
    date: "2019-03-04"
---

# How to Enable React Strict Mode

React Strict Mode is enabled by wrapping part or all of an app in `<React.StrictMode>`. It was added by Brian Vaughn in January 2018, and it surfaces development-only warnings when components use suboptimal or unsafe APIs, such as string refs, unsafe lifecycle methods, legacy context, and findDOMNode (Kent C. Dodds, 2019).

Strict Mode also intentionally runs certain callbacks and methods twice in development only: class constructors, render methods (including function components), setState updater functions, getDerivedStateFromProps, the React.useState initializer, and the React.useMemo callback. This is meant to expose side effects in methods that should be idempotent; the warnings and double calls disappear in production, and code continues to work (Kent C. Dodds, 2019).

For third-party components that trigger Strict Mode warnings, the article suggests opening a PR to the project or vendoring/forking the dependency. It recommends incrementally adopting Strict Mode by wrapping only parts of the app, since `<React.StrictMode>` can be used at any depth, so teams can opt new features into strict checks without being overwhelmed by warnings everywhere (Kent C. Dodds, 2019).

- Wrap components in `<React.StrictMode>` to get development-only warnings for unsafe APIs like string refs, unsafe lifecycles, legacy context, and findDOMNode.
- Strict Mode double-invokes certain callbacks/methods in development (constructor, render, setState updater, getDerivedStateFromProps, useState initializer, useMemo callback) to reveal side effects.
- Warnings and double invocation only occur in development; production behavior is unaffected, and UNSAFE_ lifecycle prefixes can silence warnings.
- Adopt incrementally by wrapping selected parts of the app; for third-party warnings, consider a PR or vendoring/forking the dependency.