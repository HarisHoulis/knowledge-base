---
domain: web-dev
subdomain: javascript-testing
concept: testing-abstractions
title: Demystifying Testing
sources:
  - title: "Demystifying Testing"
    url: "https://kentcdodds.com/blog/demystifying-testing"
    author: "Kent C. Dodds"
    date: "2018-10-11"
---

# Demystifying Testing

Kent C. Dodds addresses confusion about where to start with testing, noting that abstractions in software evolve until only their creators fully understand them, leaving others to take terms, APIs, and tools at face value (Kent C. Dodds, 2018). He lists common testing concepts—assertions, testing frameworks, describe/it/beforeEach/afterEach/test, mocks/stubs/test doubles/spies, and various test types—and argues that being able to explain them, not just identify them, makes engineers more effective at using and teaching them.

The core claim is that testing abstractions are not magic; they are code, and they are easier to learn by doing (Kent C. Dodds, 2018). He shows that no tools are required to write a simple test: require a function, compare its result to an expected value, throw an error if they differ, run the file with Node, and optionally run it on CI to gain confidence that changes won’t break the codebase.

Once the fundamentals are understood, using existing tools becomes more meaningful. Dodds says his favorite is the Jest testing platform because it is capable and fully featured, and he is creating a course that will let learners implement parts of testing tools from scratch to accelerate their understanding and help them write maintainable tests that instill confidence (Kent C. Dodds, 2018).

- Testing abstractions such as assertions, testing frameworks, mocks, and test types are code, not magic, and understanding them improves both teaching and usage.
- You do not need tools to write a simple test: compare an actual result to an expected value and throw an error if they differ.
- A basic test file can be run with Node and placed on CI to provide confidence against regressions.
- Dodds recommends Jest as his favorite testing platform and is building a course to help engineers implement testing abstractions from scratch.