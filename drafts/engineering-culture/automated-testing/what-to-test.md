---
domain: engineering-culture
subdomain: automated-testing
concept: what-to-test
title: Why You've Been Bad About Testing
sources:
  - title: "Why you've been bad about testing"
    url: "https://kentcdodds.com/blog/why-youve-been-bad-about-testing"
    author: "Kent C. Dodds"
    date: "2018-10-15"
---

# Why You've Been Bad About Testing

The post argues that testing mission-critical code is no longer a debate: automated tests are better than waiting for users to report bugs later. Yet developers still struggle with what to test, how much time to spend, what granularity to use, what to mock, and how to set up good testing tools and environments (source).

A major source of frustration is when tests must be rewritten every time the underlying code changes. Refactoring a component and breaking its tests adds friction to shipping and makes developers question why they are testing at all (source).

The author describes personally struggling with testing for years, rebuilding tools and even giving a full-hour talk on ES6, Webpack, Karma, and code coverage. He says he has already figured out much of the setup pain so others do not have to spend dozens of hours on it (source).

For deciding what to test, the post recommends a process: identify untested code that would be really bad if it broke, narrow it to a unit or few units, consider the code's users, write manual testing instructions for those users, and turn that list into an automated test (source).

- Mission-critical code should be tested automatically before users find bugs.
- Common struggles include choosing what to test, test granularity, mocking, tooling, environments, and duplicate code.
- Tests that break on every code change create friction and discourage developers from testing.
- A practical process is to find critical code, narrow to units, identify users, write manual verification steps, then automate them.
- The author has already invested time in testing tooling and offers techniques to reduce testing pain.