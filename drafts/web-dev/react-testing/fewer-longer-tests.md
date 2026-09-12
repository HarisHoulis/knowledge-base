---
domain: web-dev
subdomain: react-testing
concept: fewer-longer-tests
title: Write fewer, longer tests
sources:
  - title: "Write fewer, longer tests"
    url: "https://kentcdodds.com/blog/write-fewer-longer-tests"
    author: "Kent C. Dodds"
    date: "2019-08-26"
---

# Write fewer, longer tests

The article argues against splitting component tests into many small cases, especially following a strict “one assertion per test” rule. Using a `Course` component that loads data and can error, it shows a “bad” example where separate tests share mutable variables like `utils` and `alert`, rely on `beforeAll`, and are not isolated. These tests can also produce React `act` warnings because asynchronous work happens between test blocks (source).

The recommended approach combines related assertions into workflow-level tests: one test for the successful course-loading flow and one for the error flow. This keeps tests isolated, removes shared mutable state, reduces nesting, and avoids the `act` warning. The article notes that Jest’s failure output now includes the rendered DOM and exact failing line, so long tests are easy to debug; the one-assertion rule is outdated (source).

The underlying principle is to model each test on a manual tester’s workflow: use a single “Arrange” per test and as many “Act” and “Assert” steps as needed. The author warns against rendering the same component multiple times in one test block, though re-renders are acceptable when testing prop updates. In the appendix, `act` warnings are often caused by async work resolving after the test completes; fixes include waiting for the promise, using React Testing Library’s `wait`, or—best—including that assertion in a longer test (source).

- Avoid one assertion per test: combining assertions into workflow-level tests prevents isolation problems, shared mutable state, and async `act` warnings.
- Each test should represent a single manual-tester workflow: one Arrange, with as many Act and Assert steps as needed.
- Modern Jest failure output shows the DOM and exact failing line, making multiple assertions per test easy to diagnose.
- The `act` warning often means async work is resolving after the test completes; fix it by waiting, using RTL’s `wait`, or folding the assertion into a longer test.
- Do not render the same component multiple times in one test block; re-renders are okay when testing prop updates.