---
domain: web-dev
subdomain: react-context
concept: react-context-hooks
title: React Hooks and the Future of React Context
sources:
  - title: "React Hooks: What's going to happen to react context?"
    url: "https://kentcdodds.com/blog/react-hooks-whats-going-to-happen-to-react-context"
    date: "2018-12-17"
---

# React Hooks and the Future of React Context

The article discusses how React's official context API evolved from a render-prop-based Consumer API to simpler consumption patterns. The context API was powerful, but consuming multiple contexts with render props could create deeply nested components, such as wrapping LanguageConsumer around ThemeConsumer, which the author found less than ideal despite React's composability (source).

React 16.6 introduced a convenience API called contextType, allowing class components to define a static contextType and access a single context through this.context. The author appreciated this for common single-context cases (source).

React Hooks, specifically the alpha useContext hook, let function components read multiple contexts directly, e.g. const theme = useContext(ThemeContext). This removes render-prop nesting and produces less code that is easier to read, refactor, and maintain. The author stresses that hooks are opt-in and backward compatible, enabling incremental adoption even in large React codebases, and concludes that React continues to simplify real-world development (source).

- The new context API's render-prop Consumer can lead to heavy nesting when consuming multiple contexts.
- React 16.6 added contextType, a convenience for class components consuming a single context via this.context.
- The alpha useContext hook lets function components read multiple contexts directly, reducing nesting and improving readability.
- React Hooks are opt-in and backward compatible, allowing incremental adoption in existing codebases.
- The author praises React for continuing to simplify code that is easier to read, refactor, and maintain.