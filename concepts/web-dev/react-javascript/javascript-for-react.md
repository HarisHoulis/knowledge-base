---
domain: web-dev
subdomain: react-javascript
concept: javascript-for-react
title: JavaScript to Know for React
sources:
  - title: "JavaScript to Know for React"
    url: "https://kentcdodds.com/blog/javascript-to-know-for-react"
    author: "Kent C. Dodds"
    date: "2020-07-15"
---

# JavaScript to Know for React

Kent C. Dodds argues that React, unlike other frameworks, intentionally keeps you close to JavaScript: JSX compiles to plain JavaScript, React Hooks simplified the component API, and the framework provides minimal abstraction. Because of this, being effective with React depends heavily on knowing core JavaScript features and functional programming patterns such as closures. The article therefore serves as a practical guide to the modern JavaScript syntax and language features that are most commonly encountered when writing React components (Dodds, 2020).

- Mastering JavaScript closures is essential for understanding React component behavior.
- Modern JS syntax like template literals, shorthand properties, arrow functions, and destructuring are used constantly in React for cleaner component code.
- Rest/spread syntax and parameter defaults appear frequently when building reusable components with props.
- ESModules help organize code, and React's lazy loading relies on dynamic imports.
- Array methods (find, some, every, includes, map, filter, reduce) are crucial for common data-transformation and list-rendering patterns, while nullish coalescing (`??`) and optional chaining (`?.`) provide safe handling of missing values.
- Promises and async/await are foundational for working with React's ecosystem and asynchronous APIs.