---
domain: engineering-culture
subdomain: testing-practices
concept: approval-testing
title: Kotlin Refactoring: Introducing Approval Tests with http4k
sources:
  - title: "Kotlin Refactoring - Tidying Up"
    url: "https://www.youtube.com/watch?v=MxzAr4UBOs0"
    author: "Pairing with Duncan"
    date: "2021-12-03T20:54:33+00:00"
---

# Kotlin Refactoring: Introducing Approval Tests with http4k

In this video, Duncan from Gilded Rows walks through a refactoring session for their stock control system. They discovered that an earlier expedient edit had left malformed HTML in a template—specifically, a table header tag was closed incorrectly with a 'td' tag. Although browsers like Chrome automatically fix this during rendering, it's still wrong and should be corrected. The existing tests also duplicated the expected rendered output, meaning any template change required editing both the template and the test expectation in two places, which is tedious and error-prone.

To solve this, Duncan introduces approval tests using http4k's built-in support. He adds a test library dependency to build.gradle, extends the test class with an approval testing annotation, and uses `approver.assertApproved(response)` to verify the HTTP response. The first test run fails because there is no approved baseline, resulting in an `.actual` file being written. After inspecting the output, he approves it, creating an `.approved` file that serves as the expected result. From then on, any change to the rendered HTML causes a test failure with a diff, allowing the developer to either approve the change deliberately or fix the code to maintain the previous output. They then correct the malformed template and approve the updated output.

The workflow significantly reduces duplication and makes tests more explicit about what the system should produce. Approval tests integrate well with IDE plugins, making it easy to review and approve changes. This approach is particularly useful when the exact output is complex and manually writing expectations is impractical.

- The team fixed a malformed HTML tag that browsers tolerated but was still incorrect in the source.
- Approval tests replace manually duplicated expected test strings with baseline `.approved` files.
- In http4k, using `approver.assertApproved(response)` captures actual output and fails on any unexpected change.
- IntelliJ plugin support allows easy approval of new output, either accepting a change or fixing the code to preserve the baseline.