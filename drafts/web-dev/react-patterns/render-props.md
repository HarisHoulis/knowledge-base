---
domain: web-dev
subdomain: react-patterns
concept: render-props
title: When to NOT use Render Props
sources:
  - title: "When to NOT use Render Props"
    url: "https://kentcdodds.com/blog/when-to-not-use-render-props"
    author: "Kent C. Dodds"
    date: "2018-03-26"
---

# When to NOT use Render Props

The post is kept for historical purposes and states that with react@16.8.0+ the answer is to rarely use render props and almost always use a custom hook, because hooks are almost always the superior approach (source).

Every abstraction comes with a cost, so before using render props you should understand what problem it solves and whether you actually have that problem; if not, you incur the cost of abstraction without the benefits (source). Render props fundamentally solve React component logic reuse and can abstract away imperative code into a declarative API, as illustrated by Ryan Florence's `<Tone />` example (source).

Use render props when you want to reuse component logic or abstract away imperative code (source). Alternative patterns are rarely necessary: HOCs like react-redux's `connect` can provide a cleaner interface for common cases, but render props can still be used to implement HOCs and providers (source). The rule is to start with a render prop, then build common-case components or HOCs on top so common and advanced users both win (source).

- With React 16.8.0+, prefer custom hooks over render props; render props are only for rare cases.
- Render props solve component logic reuse and can abstract imperative code into a declarative API.
- Evaluate abstraction cost: if you do not have the problem render props solve, do not use them.
- HOCs and providers can offer cleaner common-case interfaces, but render props can implement them.
- Start with a render prop for logic reuse or imperative abstraction, then layer common-case components/HOCs for usability.