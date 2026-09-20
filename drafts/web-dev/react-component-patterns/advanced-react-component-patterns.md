---
domain: web-dev
subdomain: react-component-patterns
concept: advanced-react-component-patterns
title: Advanced React Component Patterns
sources:
  - title: "Advanced React Component Patterns"
    url: "https://kentcdodds.com/blog/advanced-react-component-patterns"
    author: "Kent C. Dodds"
    date: "2017-12-05"
---

# Advanced React Component Patterns

The post announces two egghead.io courses, The Beginner's Guide to ReactJS and Advanced React Component Patterns, totaling about 2.5 hours of content with 18 videos each, and previews the patterns taught in the advanced course [source](https://kentcdodds.com/blog/advanced-react-component-patterns). The course starts from a simple toggle component and evolves it through each pattern so learners can see trade-offs and when each pattern is appropriate.

Patterns covered include compound components that share implicit state like HTML's <select> and <option>, using React.Children.map and then context; higher order components (HOCs), which return a component and are widely used by react-redux; and render props, which the author calls his favorite pattern and which delegates rendering responsibility to the user while providing state and functions [source](https://kentcdodds.com/blog/advanced-react-component-patterns).

The course also covers prop collections and getters for bundling common accessibility or interactivity props, state initializers with a reset helper, controlled components that move internal state into props, and the provider pattern using context and react-broadcast so it works through shouldComponentUpdate. It concludes by refactoring the toggle component into a redux component called "Rendux" [source](https://kentcdodds.com/blog/advanced-react-component-patterns).

- The course uses a single toggle component and refactors it through each pattern to highlight trade-offs.
- Compound components share implicit state like HTML's <select> and <option>, implemented with React.Children.map and context.
- Render props is the author's favorite pattern; HOCs are widespread but require extra work to hide implementation details.
- Other patterns include prop collections/getters, state initializers, controlled components, and provider.
- The course ends by refactoring the toggle component to a redux component called "Rendux".