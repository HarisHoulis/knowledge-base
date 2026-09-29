---
domain: web-dev
subdomain: react-component-patterns
concept: mixing-component-patterns
title: Mixing Component Patterns
sources:
  - title: "Mixing Component Patterns"
    url: "https://kentcdodds.com/blog/mixing-component-patterns"
    author: "Kent C. Dodds"
    date: "2018-05-07"
---

# Mixing Component Patterns

The article demonstrates how to combine multiple React component patterns—Compound Components, Render Props, Component Injection, Provider Pattern, and Higher Order Components—into a single Toggle component (source). It provides a CodeSandbox with extensive comments and a condensed implementation.

The Toggle uses React context as a Provider, exposes static subcomponents like Toggle.Consumer, Toggle.On, Toggle.Off, and Toggle.Button, and uses getUI to support children as arrays/elements, class components, or functions (render props). It also includes withToggle HOC to pass toggle state to wrapped components (source).

The author notes this is not to encourage every component to be implemented this way, but to show how these patterns can be used together for an extremely flexible API when useful. If choosing only one pattern, he recommends render props because all other patterns can be implemented on top of it and it is simplest from a consumer's point of view (source).

- A single component can combine Compound Components, Render Props, Component Injection, Provider Pattern, and HOCs by using React context and a getUI helper.
- Toggle.Consumer, Toggle.On, Toggle.Off, and Toggle.Button are static compound components built on ToggleContext.Consumer.
- getUI supports children as a React element/array, a class component (via React.createElement), or a function (render prop).
- withToggle is a HOC that consumes ToggleContext and forwards refs while hoisting non-React statics.
- Author recommends render props as the single pattern to choose because other patterns can be built on it and it is simplest for consumers.