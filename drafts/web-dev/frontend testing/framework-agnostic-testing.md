---
domain: web-dev
subdomain: frontend testing
concept: framework-agnostic-testing
title: React is an implementation detail
sources:
  - title: "React is an implementation detail"
    url: "https://kentcdodds.com/blog/react-is-an-implementation-detail"
    author: "Kent C. Dodds"
    date: "2018-10-20"
---

# React is an implementation detail

Kent C. Dodds argues that React is an implementation detail, so tests should not be tied to React itself. He connects this to the testing philosophy taught in TestingJavaScript.com: avoid testing implementation details, and the same approach can apply to other frameworks (Kent C. Dodds, "React is an implementation detail", 2018).

React Testing Library is a very small library, and its real core is DOM Testing Library, which is framework-agnostic. Dodds points to a course example that uses DOM Testing Library to test a jQuery plugin, showing that the tooling is not React-specific (Kent C. Dodds, 2018).

Because most modern frameworks are component-based, Dodds says 99% of tests written with these tools will look basically the same regardless of framework. The hardest part is getting DOM from a component into the document, and the course includes a module demonstrating that with 11 frameworks and libraries (Kent C. Dodds, 2018).

- React is an implementation detail, so tests should avoid depending on React-specific details.
- React Testing Library is small; DOM Testing Library is the framework-agnostic core.
- DOM Testing Library can be used with non-React tools, such as a jQuery plugin.
- Tests written with these tools tend to look the same across frameworks.
- The course shows how to render component DOM into the document for 11 frameworks and libraries.