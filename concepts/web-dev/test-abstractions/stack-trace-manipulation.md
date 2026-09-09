---
domain: web-dev
subdomain: test-abstractions
concept: stack-trace-manipulation
title: Improve test error messages of your abstractions
sources:
  - title: "Improve test error messages of your abstractions"
    url: "https://kentcdodds.com/blog/improve-test-error-messages-of-your-abstractions"
    date: "2020-05-18"
---

# Improve test error messages of your abstractions

Custom test helpers often obscure where a failure actually happened. When an assertion is wrapped inside a utility function, the resulting Jest codeframe points to the assertion line inside the helper, not the test case that called it. This forces developers to dig through the stack trace to find the relevant call site, which is especially painful when the helper is used many times across a test suite.

The article demonstrates how to fix this by manipulating the error's stack trace before Jest formats it. Since Jest constructs its codeframe from the first relevant line of the stack, removing all frames from the utility function upward causes the codeframe to point directly to the call site. A simple approach is to filter out lines containing the helper name, but a cleaner, more robust solution is using Node's `Error.captureStackTrace(error, helperFunction)`, which automatically omits frames above `helperFunction`.

This technique is applicable not only to internal test utilities but also to published libraries. The author notes that Jest already filters out node_modules stack frames, but tools like DOM Testing Library still use this approach to provide helpful error messages for async utilities such as `waitFor`. Understanding how to adjust stack traces can greatly improve the debugging experience for custom assertion helpers.

- Assertion wrappers can hide the failing test call site in Jest's codeframe.
- Jest derives its codeframe from the first relevant stack trace line.
- Use `Error.captureStackTrace(error, helper)` to remove the helper's frames and show the call site.
- The technique is useful for custom test utilities and async testing helpers like `waitFor`.