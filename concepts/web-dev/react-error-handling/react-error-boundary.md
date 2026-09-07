---
domain: web-dev
subdomain: react-error-handling
concept: react-error-boundary
title: Use react-error-boundary to handle errors in React
sources:
  - title: "Use react-error-boundary to handle errors in React"
    url: "https://kentcdodds.com/blog/use-react-error-boundary-to-handle-errors-in-react"
    date: "2020-07-20"
---

# Use react-error-boundary to handle errors in React

This article explains why simple try/catch blocks fail to handle runtime errors in React rendering. Because React itself invokes components, errors thrown inside child components cannot be caught by a try/catch in the parent—only an Error Boundary can intercept them [source]. The recommended solution is the react-error-boundary package, which provides a declarative ErrorBoundary component with a FallbackComponent prop, avoiding the need to hand-write class-based error boundaries [source].

- try/catch in a parent component cannot catch errors thrown by React child components because React calls those components, not the developer.
- react-error-boundary offers an ErrorBoundary component that declaratively handles runtime render errors via a FallbackComponent.
- Error recovery is supported through resetKeys and onReset props, allowing users to retry after entering invalid state.
- Error Boundaries do not catch event handler, async, SSR, or boundary-own errors; use the useErrorBoundary hook's showBoundary to forward those errors to the nearest boundary.