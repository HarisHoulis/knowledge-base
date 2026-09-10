---
domain: web-dev
subdomain: javascript-testing
concept: make-your-test-fail
title: Make Your Test Fail
sources:
  - title: "Make Your Test Fail"
    url: "https://kentcdodds.com/blog/make-your-test-fail"
    author: "Kent C. Dodds"
    date: "2020-02-24"
---

# Make Your Test Fail

Kent C. Dodds argues that a passing test is not enough: you must verify the test can fail when the behavior it covers is broken. He demonstrates with an `isPasswordAllowed` function and tests that appear to check non-alphanumeric, digit, uppercase, and lowercase requirements, but all `false` cases fail only because the passwords are too short. Commenting out the digit check still leaves all tests green, showing they provide false confidence (kentcdodds.com).

He warns that such tests are worse than worthless because they give a false sense of security and discourage writing good tests. Code coverage may not reveal the issue because the lines can be covered by the valid-password test, and line hit counts are easy to overlook. He also notes common related mistakes like bare `expect(thing)` with no assertion and empty snapshots, which `eslint-plugin-jest` can help catch (kentcdodds.com).

The fix is to write each negative test with a password that satisfies all other requirements but violates the one under test. Then commenting out the corresponding implementation line makes the test fail. For example, `isPasswordAllowed('Ab3efgh')` should fail for missing non-alphanumeric, `isPasswordAllowed('Ab.efgh')` for missing digit, etc. This ensures tests actually protect against regressions and provide value rather than false security (kentcdodds.com).

- A test that cannot fail when the tested behavior breaks is worse than worthless because it gives false confidence.
- Negative tests must isolate the condition under test by satisfying all other requirements.
- Code coverage can miss this problem because lines may be covered without the assertion exercising the specific condition.
- Avoid bare expectations and empty snapshots; use eslint-plugin-jest rules and prefer non-snapshot assertions when possible.