---
domain: web-dev
subdomain: react-testing
concept: avoid-testing-implementation-details
title: Testing Implementation Details
sources:
  - title: "Testing Implementation Details"
    url: "https://kentcdodds.com/blog/testing-implementation-details"
    author: "Kent C. Dodds"
    date: "2020-08-17"
---

# Testing Implementation Details

Kent C. Dodds explains why testing implementation details in React components is harmful, leading to false negatives and false positives. He defines implementation details as things users of the code do not typically use, see, or know about, and identifies the two real users of a component: end-users and developers who pass props. Tests should exercise the component the way these users do, focusing on rendered output and props.

- Testing implementation details causes false negatives: tests break during refactors even when behavior is unchanged.
- Implementation detail tests can also produce false positives, passing even when the component is broken for users (e.g., the button is not wired to the handler).
- Because enzyme APIs like state(), instance(), and shallow rendering expose implementation details, they encourage brittle tests.
- React Testing Library guides you away from implementation details by querying rendered output the way users see it.
- To decide what to test, consider the production users of the code and write instructions for manually testing that behavior.