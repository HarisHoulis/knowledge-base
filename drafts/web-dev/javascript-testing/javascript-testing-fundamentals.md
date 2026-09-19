---
domain: web-dev
subdomain: javascript-testing
concept: javascript-testing-fundamentals
title: What Is a JavaScript Test? Building a Minimal Testing Framework
sources:
  - title: "But really, what is a JavaScript test?"
    url: "https://kentcdodds.com/blog/but-really-what-is-a-javascript-test"
    author: "Kent C. Dodds"
    date: "2018-01-01"
---

# What Is a JavaScript Test? Building a Minimal Testing Framework

A JavaScript test is code that throws an error when the actual result of something does not match the expected output; the comparison that checks this is called an assertion [1]. Pure functions, like the `sum` and `subtract` functions in a `math.js` module, are relatively easy to test because they always return the same output for a given input and do not change surrounding state [1].

The article builds up testing concepts step by step: first with a plain `if (actual !== expected) throw new Error(...)`, then with Node's built-in `assert.strictEqual`, then with a custom `expect(actual).toBe(expected)` assertion library, and then with a `test(title, callback)` helper that catches errors, labels each test, and allows all tests in a file to run without bailing on the first failure [1]. Helpful error messages are described as one of the most important parts of testing frameworks or assertion libraries [1].

A test runner is the next layer: it can search for test files and run them, though building a full framework involves many additional features [1]. The article switches to Jest, which provides `test` and `expect` as global objects, so the custom implementations can be removed [1]. Jest reports failures with color, test titles, and the code where the error was thrown, making the error output more helpful [1].

The conclusion is that a JavaScript test simply sets up some state, performs some action, and makes an assertion on the new state; frameworks also offer helpers like `beforeEach` and `describe` and many more assertions such as `toMatchObject` or `toContain` [1].

- A JavaScript test is code that throws an error when the actual result does not match the expected output; the comparison is an assertion.
- Assertions can be hand-written, use Node's `assert` module, or come from libraries/frameworks such as Jest's `expect`.
- Wrapping tests in named `test()` callbacks isolates failures and reports which test broke instead of stopping at the first error.
- A test runner discovers and runs test files; Jest supplies `test` and `expect` globally and gives helpful, colored failure output with code context.
- Testing pure functions is straightforward, while stateful code requires setting up state before firing events or making assertions.