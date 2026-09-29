---
domain: web-dev
subdomain: ui-testing
concept: ui-testing-myths
title: UI Testing Myths
sources:
  - title: "UI Testing Myths"
    url: "https://kentcdodds.com/blog/ui-testing-myths"
    author: "Kent C. Dodds"
    date: "2018-11-08"
---

# UI Testing Myths

The article challenges three common beliefs about UI testing. Myth 1 says tests always break when code changes, but this is only true when tests focus on implementation details. Users do not care about implementation details or whether the app uses React, Angular, or jQuery, so tests generally should not care either. Many tools encourage testing implementation details, which leads to constant test rewrites.

Myth 2 says connected Redux components cannot be tested. The conventional approach is to isolate the component from Redux and test action creators and reducers separately, but that gives no confidence that they communicate correctly. Instead, testing the connected component with the real Redux store verifies rendering and that action creators, reducers, and components work together as they will in production. The same concepts apply to React Router and other providers like emotion’s Theme Provider.

Myth 3 says end-to-end tests are slow and brittle. This can also be true when tests are written incorrectly, such as repeating the full registration and login flow in every test. That duplication leads to page objects, which the author calls a poor practice. A better approach is to verify registration and login once, then skip those flows in later tests to reduce failures and speed things up. With tools like Cypress Testing Library, page objects become unnecessary, and tests are easier to maintain, more reliable, and faster.

- Tests should avoid implementation details and focus on user-visible behavior instead.
- Connected Redux components can be tested with the real store to verify integration, not just isolated units.
- E2E tests become slow and brittle when every test repeats full flows like registration and login.
- Verify authentication flows once and skip them in subsequent tests to reduce duplication and failure points.
- Page objects are unnecessary with tools like Cypress Testing Library, making tests easier to maintain and faster.