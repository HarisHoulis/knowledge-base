---
domain: web-dev
subdomain: react-testing
concept: shallow-rendering-tradeoffs
title: Why I Never Use Shallow Rendering
sources:
  - title: "Why I Never Use Shallow Rendering"
    url: "https://kentcdodds.com/blog/why-i-never-use-shallow-rendering"
    author: "Kent C. Dodds"
    date: "2018-07-23"
---

# Why I Never Use Shallow Rendering

Kent C. Dodds argues against enzyme's shallow rendering because it violates two testing goals: tests should fail when a real bug would break the component, and tests should keep passing after backward-compatible refactors. Shallow rendering, he says, does the opposite: it breaks on implementation refactors while potentially missing broken application behavior (source).

Shallow rendering only inspects the React elements returned by a component's render method rather than rendering child components, running lifecycle methods, or interacting with the DOM. As a result, child components such as Fade/CSSTransition are not actually rendered, so a change that breaks them can escape the test (source).

He responds to common justifications: calling instance methods or reading state tests implementation details users cannot see; speed gains are marginal (milliseconds) and can be offset with Jest watch mode; and “unit testing” isolation is too heavy-handed because shallow rendering skips all child components, including in-file ones. He favors integration testing and explicit mocks (source).

React Testing Library embodies his principle that tests should resemble how software is used. It deliberately omits shallow rendering, static rendering, component instances, props/state access, and component-name queries. The article shows an RTL test that mocks react-transition-group explicitly and verifies user-visible behavior; shallow snapshots are dismissed as implementation-detail noise (source).

- Shallow rendering makes tests break on refactors and miss real breakage because it tests implementation details rather than user-observable behavior.
- It only inspects the render output's React elements; it does not render child components, run lifecycle methods, or interact with the DOM.
- Common reasons for shallow rendering—method calls/state, speed, unit isolation—are weak; speed differences are milliseconds and isolation can be achieved with explicit mocks.
- Prefer integration-style tests with React Testing Library and explicit Jest mocks that resemble user usage.
- React Testing Library intentionally cannot do shallow rendering, instance/props/state access, or component-name queries; shallow snapshots are brittle implementation details.