---
domain: web-dev
subdomain: react-testing
concept: react-testing-library-common-mistakes
title: Common Mistakes with React Testing Library
sources:
  - title: "Common mistakes with React Testing Library"
    url: "https://kentcdodds.com/blog/common-mistakes-with-react-testing-library"
    author: "Kent C. Dodds"
    date: "2020-05-04"
---

# Common Mistakes with React Testing Library

Kent C. Dodds, creator of React Testing Library, catalogs suboptimal patterns he still sees in tests and explains why they are problematic and how to improve them (Dodds, 2020). Each mistake is labeled by importance: low is mostly opinion, medium may cause bugs or unnecessary work, and high should definitely be followed because tests may lack confidence or be problematic (Dodds, 2020).

The article advises installing the official Testing Library ESLint plugins, avoiding the old `wrapper` variable name for `render`’s return value, and not manually calling `cleanup` because it now happens automatically (Dodds, 2020). It recommends using `screen` instead of destructuring queries from `render`; using `jest-dom` assertions such as `toBeDisabled` for better error messages; and not wrapping `render` or `fireEvent` in `act` unnecessarily, since those utilities are already wrapped and `act` warnings usually signal an unexpected issue (Dodds, 2020).

For queries, Dodds says to query the DOM as closely as possible to how end-users interact with it, following the “Which query should I use?” guide (Dodds, 2020). He recommends `*ByRole` with accessible names and querying by actual text rather than test IDs or `container.querySelector`, avoiding unnecessary or incorrect accessibility attributes, using `@testing-library/user-event` over `fireEvent` where possible, and reserving `query*` variants only for checking non-existence (Dodds, 2020). The source text begins discussing `waitFor` versus `find*` but is truncated (Dodds, 2020).

- Install and use the Testing Library ESLint plugins to avoid several common mistakes.
- Use `screen` for queries and debugging; `cleanup` is automatic, and `wrapper` is unnecessary for `render`’s return value.
- Query by role/accessible name and user-visible text instead of test IDs or `container.querySelector`; avoid adding unnecessary ARIA attributes.
- Use `jest-dom` assertions, avoid unnecessary `act` wrapping, and prefer `@testing-library/user-event` over `fireEvent` where possible.
- Use `query*` variants only to assert non-existence; `get*` and `find*` provide more helpful errors.