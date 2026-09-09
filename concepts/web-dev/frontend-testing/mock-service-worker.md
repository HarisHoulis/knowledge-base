---
domain: web-dev
subdomain: frontend-testing
concept: mock-service-worker
title: Stop mocking fetch
sources:
  - title: "Stop mocking fetch"
    url: "https://kentcdodds.com/blog/stop-mocking-fetch"
    author: "Kent C. Dodds"
    date: "2020-06-03"
---

# Stop mocking fetch

Kent C. Dodds argues that mocking the `client` or `window.fetch` in tests leads to low confidence, duplicated mock implementations, and a slower feedback loop. He suggests that mocking at the fetch level forces tests to re-implement backend behavior across many test files, often missing important details like headers and authentication. He instead recommends using Mock Service Worker (MSW) to intercept network requests at the service worker level, allowing tests to exercise real fetch calls while returning realistic responses. This approach increases confidence, reduces boilerplate, and enables reuse of the same server handlers in both tests and browser development. MSW also supports colocation for error/edge cases by letting individual tests override handlers while preserving isolation via `server.resetHandlers()`.

- Mocking the API client or window.fetch hides integration bugs and often requires duplicating backend logic in every test.
- MSW intercepts real fetch requests, so tests fail correctly if fetch is used improperly.
- The same MSW server handlers can be shared between tests and browser development, improving workflow.
- MSW allows per-test handler overrides for edge cases while resetting automatically for isolation.