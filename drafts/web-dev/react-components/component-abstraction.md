---
domain: web-dev
subdomain: react-components
concept: component-abstraction
title: When to break up a component into multiple components
sources:
  - title: "When to break up a component into multiple components"
    url: "https://kentcdodds.com/blog/when-to-break-up-a-component-into-multiple-components"
    author: "Kent C. Dodds"
    date: "2019-07-19"
---

# When to break up a component into multiple components

The article argues that any React application could technically be written as a single React component, but doing so would cause serious problems. These include performance issues from whole-app re-renders, poor code sharing and reusability, difficult state management, testing that becomes purely integration-level and prone to over-testing, painful collaboration with merge conflicts, inability to use third-party components and HOCs, and imperative APIs littered throughout lifecycle hooks rather than encapsulated in declarative components (Kent C. Dodds, 2019).

These problems are the reasons to write custom components. Kent C. Dodds' answer to when to split is: “When you experience one of the problems above, that's when you break your component into multiple smaller components. NOT BEFORE.” He emphasizes that this split is abstraction, and every abstraction comes with a cost, quoting Sandi Metz: “Duplication is far cheaper than the wrong abstraction” (Kent C. Dodds, 2019).

He notes that long JSX in a component is acceptable because JSX is just JavaScript expressions using declarative component APIs, and it is easier to keep than splitting prematurely and prop drilling everywhere. The conclusion is to feel free to break up components, but don't fear a growing component until real problems appear; maintaining it until it needs to be broken up is easier than maintaining a premature abstraction (Kent C. Dodds, 2019).

- Any React app could technically be written as one giant component, but that causes performance, state, testing, collaboration, third-party, and imperative-API problems.
- Break a component into multiple components only when you actually experience one of those problems, not before.
- Abstraction has a cost; duplication is often cheaper than the wrong abstraction.
- Long JSX is acceptable because JSX is just JavaScript expressions using declarative component APIs; premature splitting leads to prop drilling.
- Feel free to split components, but don't be afraid of a growing component until real problems appear.