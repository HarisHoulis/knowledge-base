---
domain: web-dev
subdomain: react-testing
concept: act-warning
title: Fixing React's "not wrapped in act(...)" warning
sources:
  - title: "Fix the "not wrapped in act(...)" warning"
    url: "https://kentcdodds.com/blog/fix-the-not-wrapped-in-act-warning"
    author: "Kent C. Dodds"
    date: "2020-02-03"
---

# Fixing React's "not wrapped in act(...)" warning

Kent C. Dodds explains that React's `act(...)` warning appears when a component updates state outside the test's expected interaction flow, often because asynchronous work continues after the test has finished (Dodds, 2020). The warning is useful because it can reveal gaps in tests, such as failing to assert that a loading state resolves after an async submit (Dodds, 2020). React itself handles updates inside its callstack, but asynchronous code, resolved promises, or timer-driven updates may need to be wrapped in `act` or awaited via React Testing Library's async utilities (Dodds, 2020).

The recommended fix is usually to wait for the async behavior to finish using a user-visible assertion, such as `waitForElementToBeRemoved` for a "Saving..." indicator, rather than manually calling `act` (Dodds, 2020). React Testing Library's async utilities already wrap `act` automatically, so direct use should be rare (Dodds, 2020). Dodds notes that the warning is applied to function components with hooks but not class components, because adding it broadly to classes would create too many warnings for existing tests (Dodds, 2020).

For cases not covered by React Testing Library utilities, manual `act` can be necessary. Examples include advancing Jest fake timers with `jest.advanceTimersByTime` and testing custom hooks whose returned functions trigger state updates (Dodds, 2020). An alternative for mocked promises is to return a promise from the mock and await it inside `async act`, though Dodds says this is less preferable because it may not catch missing state updates (Dodds, 2020).

- The `act(...)` warning signals that React state updated unexpectedly, often because async work completed after the test interaction (Dodds, 2020).
- Prefer adding assertions that wait for async UI changes, such as `waitForElementToBeRemoved`, instead of manually wrapping interactions in `act` (Dodds, 2020).
- React Testing Library's async utilities already include `act`, so direct use of `act` should be rare (Dodds, 2020).
- Manual `act` is needed for cases like advancing Jest fake timers or calling custom hook functions that update state outside React Testing Library utilities (Dodds, 2020).
- The warning is primarily applied to function components/hooks, not class components, to avoid widespread warnings in existing class-based tests (Dodds, 2020).