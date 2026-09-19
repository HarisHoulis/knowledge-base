---
domain: web-dev
subdomain: javascript-testing
concept: javascript-mocking
title: But really, what is a JavaScript mock?
sources:
  - title: "But really, what is a JavaScript mock?"
    url: "https://kentcdodds.com/blog/but-really-what-is-a-javascript-mock"
    author: "Kent C. Dodds"
    date: "2018-03-19"
---

# But really, what is a JavaScript mock?

The article builds a definition of a JavaScript mock by testing a `thumbWar` function that depends on a non-deterministic `getWinner` utility. Because `getWinner` is treated like an unreliable third-party service, mocking is presented as a practical way to make tests deterministic and to assert that the integration works, rather than only checking that the winner is one of the players (source).

It then walks through progressively better mocking techniques. First, monkey-patching the imported `utils` namespace requires saving and restoring the original function; adding a `mock.calls` array allows assertions about call count and arguments. Next, `jest.fn` replaces the manual mock metadata with built-in Jest mock tracking and assertions such as `toHaveBeenCalledTimes` (source).

The article then introduces `jest.spyOn`, `mockImplementation`, and `mockRestore` to simplify setup and cleanup. It notes that mutating an imported namespace violates the `import/namespace` ESLint rule and relies on Babel/CommonJS behavior, not ES module semantics. To avoid teaching bad habits, it recommends `jest.mock` and manual mocks in a `__mocks__` directory, with `jest.requireActual` for partial mocks (source).

- Mocking is especially useful when a dependency is unreliable or non-deterministic, such as a third-party service.
- Manual monkey-patching requires restoring the original value and adding custom call tracking to assert call count and arguments.
- Jest utilities like `jest.fn`, `spyOn`, `mockImplementation`, and `mockRestore` replace manual mock bookkeeping with built-in spy/mock behavior.
- Mutating an imported module namespace is non-spec-compliant and relies on Babel/CommonJS behavior; `jest.mock` simulates the module system to swap in a mock safely.
- A `__mocks__` directory enables reusable module mocks, and `jest.requireActual` helps when only some functions in a module should be mocked.