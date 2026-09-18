---
domain: web-dev
subdomain: react
concept: jsx
title: What is JSX?
sources:
  - title: "What is JSX?"
    url: "https://kentcdodds.com/blog/what-is-jsx"
    author: "Kent C. Dodds"
    date: "2018-07-09"
---

# What is JSX?

JSX is a syntax extension that compiles to `React.createElement` calls, allowing UI to be expressed as regular JavaScript expressions that can be assigned to variables (source). The `React.createElement(elementType, props, ...children)` API accepts a string or function as element type, a props object or `null`, and children as rest arguments or a `children` prop/array (source).

Interpolations inside `{}` are left alone and must be JavaScript expressions because they act as the right-hand side of object assignments or function-call arguments (source). This lets variables, conditionals, and mapped arrays be dynamically injected into props and children, as shown by examples like `<div>Hello {subject}</div>` and `items.map((i) => <span key={i.id}>{i.content}</span>)` (source).

A `React.createElement` call returns a simple element object such as `{ type, key, ref, props, _owner, _store }` (source). Renderers like `ReactDOM.render` interpret that object to create DOM nodes or other output (source). Understanding the compiled output lets developers compile JSX in their head and use the abstraction more powerfully (source).

- JSX compiles to `React.createElement` calls and is a regular JavaScript expression.
- `createElement` takes an element type, props, and children; multiple children can be passed as arguments or an array.
- Interpolations `{}` must contain JavaScript expressions and are used for dynamic props/children.
- `createElement` returns a plain element object that renderers interpret.
- Compiling JSX mentally helps use React effectively.