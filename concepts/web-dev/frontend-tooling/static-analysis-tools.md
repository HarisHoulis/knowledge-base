---
domain: web-dev
subdomain: frontend-tooling
concept: static-analysis-tools
title: Eliminate an Entire Category of Bugs with a Few Simple Tools
sources:
  - title: "Eliminate an entire category of bugs with a few simple tools"
    url: "https://kentcdodds.com/blog/eliminate-an-entire-category-of-bugs-with-a-few-simple-tools"
    date: "2020-05-07"
---

# Eliminate an Entire Category of Bugs with a Few Simple Tools

The article presents ESLint, Prettier, and TypeScript as static code analysis tools that should be considered testing tools. ESLint analyzes code for potential errors without running it, catching subtle bugs like incorrect operator precedence around `in`. Prettier formats code to make intent clearer, for example by adding parentheses around `a && b || c` to expose evaluation order, while still allowing developers to override with explicit grouping.

- ESLint statically analyzes code to automatically catch subtle potential bugs.
- Prettier auto-formats code to make expression intent obvious, reducing cognitive load and team inconsistency.
- TypeScript adds inline static type checking, acting like automated tests that catch invalid usages, e.g., passing a wrongly shaped object to a function.
- These tools provide fast, low-effort confidence and serve as the foundational layer in the Testing Trophy approach.