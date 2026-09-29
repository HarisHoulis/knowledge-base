---
domain: web-dev
subdomain: react-testing
concept: react-testing-library
title: Introducing the react-testing-library
sources:
  - title: "Introducing the react-testing-library 🐐"
    url: "https://kentcdodds.com/blog/introducing-the-react-testing-library"
    author: "Kent C. Dodds"
    date: "2018-04-02"
---

# Introducing the react-testing-library

Kent C. Dodds introduces react-testing-library, a lightweight React DOM testing utility designed to encourage maintainable tests that avoid component implementation details and focus on user-visible behavior. The stated problem is that tests coupled to implementation details break during refactors even when functionality is unchanged, slowing down teams [Kent C. Dodds, “Introducing the react-testing-library”].

The library provides utility functions on top of react-dom and react-dom/test-utils. Its guiding principle is that tests should work with actual DOM nodes and query them like a user would—finding form elements by label text and links/buttons by their text—with data-testid as an escape hatch. This approach encourages accessibility and gives more confidence that the application works for real users. It is positioned as a replacement for enzyme, though the same guidelines can be followed with enzyme. React Native Testing Library offers a similar API for React Native [Kent C. Dodds, “Introducing the react-testing-library”].

Examples show render(<Component />), screen queries such as queryByText, getByLabelText, getByText, and findByRole, plus userEvent for typing and clicking. The test waits for async UI the way a manual tester would. The library is not a test runner or framework and is not specific to a testing framework, though Jest is recommended. Its API includes Simulate, wait, and render—which returns container and unmount—along with getByLabelText, getByPlaceholderText, getByText, getByAltText, and getByTestId. Matching supports case-insensitive substrings, regex, or a function, and each get* helper has a query* variant that returns null instead of throwing [Kent C. Dodds, “Introducing the react-testing-library”].

- Focus tests on user-visible DOM behavior instead of component implementation details, so refactors do not break tests unnecessarily.
- Query elements as users do—by label text and visible text—and use data-testid only as an escape hatch.
- Provides render, get*/query* helpers, wait, and Simulate on top of react-dom and react-dom/test-utils.
- Not a test runner or framework; it works with Jest or any testing framework.
- Positioned as a replacement for enzyme, with React Native Testing Library offering a similar API.