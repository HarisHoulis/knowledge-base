---
domain: engineering-culture
subdomain: testing
concept: aha-testing
title: AHA Testing: Avoid Hasty Abstraction in Tests
sources:
  - title: "AHA Testing 💡"
    url: "https://kentcdodds.com/blog/aha-testing"
    author: "Kent C. Dodds"
    date: "2019-04-07"
---

# AHA Testing: Avoid Hasty Abstraction in Tests

The AHA Programming Principle (Avoid Hasty Abstraction) can be applied to writing maintainable tests. Most tests fall into one of two extremes on the spectrum of abstraction: ANA (Absolutely No Abstraction) or DRY (Don't Repeat Yourself). Finding a sweet spot in the middle is key (Kent C. Dodds, 2019).

ANA testing duplicates setup code across every test, making it hard to see what actually differs between test cases. The article shows an ExpressJS route handler test where two nearly identical tests differ only in the user's location, but the duplication obscures this. The litmus test: how easy is it to determine the difference between assertions of two similar tests and what causes that difference? ANA makes this very difficult.

DRY testing often leads to overuse of `describe`/`it` nesting, `beforeEach`, shared variables, and conditional logic in test utilities. This can make tests harder to understand and maintain because you have to trace through layers of abstraction to see what each test does.

AHA testing advocates for mindful abstraction. For example, a `setup` function (a Test Object Factory) can provide default values and accept overrides, making the unique inputs for each test explicit. For React components, a `renderLoginForm` helper can return user-event helpers. For pure functions, `jest-in-case` or `test.each` can reduce boilerplate while clearly listing inputs and outputs. The conclusion: it takes less work to write and maintain tests that have mindful abstractions applied to them.

- AHA (Avoid Hasty Abstraction) balances between ANA (no abstraction) and DRY (over-abstraction) to improve test maintainability.
- ANA tests duplicate setup, obscuring the unique difference between test cases; a litmus test is how easily you can spot what causes different assertions.
- DRY tests often use excessive nesting, shared variables, and conditional logic in utilities, making tests harder to follow and maintain.
- Mindful abstractions like a setup function (Test Object Factory) enable overriding only relevant inputs, making differences explicit (e.g., user location).
- For pure functions, jest-in-case or test.each reduce boilerplate while clearly listing inputs and outputs.