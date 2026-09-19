---
domain: web-dev
subdomain: react
concept: render-props
title: Answers to common questions about render props
sources:
  - title: "Answers to common questions about render props"
    url: "https://kentcdodds.com/blog/answers-to-common-questions-about-render-props"
    author: "Kent C. Dodds"
    date: "2018-02-12"
---

# Answers to common questions about render props

Kent C. Dodds answers common questions about React’s render props pattern. On performance, he points to Ryan Florence’s “React, Inline Functions, and Performance,” summarizing its advice: write code naturally, measure interactions to find slow paths, and use PureComponent/shouldComponentUpdate only when needed, skipping prop functions unless they are used in lifecycle hooks for side effects. He adds that if inlining the render prop function is a concern, you can define it as a class method instead (source).

On messy render functions, Mark Erikson asked about large render props. Dodds agrees most examples put all logic in the render function, but because render props are just functions called with arguments, they can be handled flexibly: you can extract the UI into a regular function component, pass the render prop arguments as props, or use a block-bodied arrow function rather than an implicit return (source).

On lifecycle hooks, Dodds explains that render prop arguments are available in render, and you can forward them to a separate component’s props so lifecycle methods like componentDidUpdate can access them. He also mentions Donavon’s preferred Component Injection pattern, where a component is passed as a prop, and Donavon’s render-props library (source).

In conclusion, Dodds says render props encapsulate a component’s logic without sacrificing customizability and simplicity in the markup, and he points to Jared Palmer’s awesome-react-render-props list for more examples (source).

- Performance concerns are addressed by Ryan Florence’s advice: write naturally, measure interactions, and avoid premature optimization; use PureComponent/shouldComponentUpdate only when needed.
- Render prop functions can be non-inline methods if inlining is a performance concern.
- Large render functions are not inherently problematic; render props are just functions, so you can extract UI into separate components or use block-bodied functions.
- To access render prop arguments in lifecycle hooks, forward them as props to a regular class component; Component Injection is an alternative pattern.
- Render props encapsulate logic while preserving customizable markup.