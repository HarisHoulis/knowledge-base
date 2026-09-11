---
domain: web-dev
subdomain: abstraction-design
concept: inversion-of-control
title: Inversion of Control
sources:
  - title: "Inversion of Control"
    url: "https://kentcdodds.com/blog/inversion-of-control"
    author: "Kent C. Dodds"
    date: "2019-11-18"
---

# Inversion of Control

Kent C. Dodds describes the common lifecycle of reusable abstractions: they start simple, then accumulate options and branches to support new use cases, leading to bundle size, maintenance, implementation, and API complexity (Dodds, 2019). He argues that inversion of control (IoC) can mitigate these problems by shifting responsibility from the abstraction to the caller. Instead of adding flags and conditionals, the abstraction accepts a function or component that lets users decide behavior.

Using a contrived `filter` function, Dodds shows how an options object with multiple boolean flags explodes into many supported combinations, while an IoC version that takes a predicate function is simpler and supports arbitrary use cases (Dodds, 2019). The trade-off is a potentially less convenient API, but he notes that simpler higher-level APIs can be built on top of the IoC primitive, giving users both convenience and flexibility. Users can compose the building blocks themselves to handle custom needs without waiting for new features.

Dodds applies IoC to React with two patterns: compound components, where users compose `Menu`, `MenuButton`, `MenuList`, and `MenuItem` to control rendering; and state reducers, where users can override state transition logic (Dodds, 2019). These patterns demonstrate how IoC gives control to the consumer, reducing the need for prop proliferation and special-case handling. The article concludes that IoC is a powerful principle for keeping abstractions simple and maintainable.

- Traditional reusable abstractions tend to accumulate options and branches, causing bundle size, maintenance, implementation, and API complexity.
- Inversion of control flips responsibility: the abstraction does less and the caller does more, often by accepting a function or composed components.
- Control-inverted APIs can be used to build simpler higher-level APIs, allowing users to handle custom cases without requesting new features.
- React patterns like compound components and state reducers are practical applications of inversion of control.