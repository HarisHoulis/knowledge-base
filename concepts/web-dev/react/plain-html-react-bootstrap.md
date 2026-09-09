---
domain: web-dev
subdomain: react
concept: plain-html-react-bootstrap
title: Super Simple Start to React
sources:
  - title: "Super Simple Start to React"
    url: "https://kentcdodds.com/blog/super-simple-start-to-react"
    author: "Kent C. Dodds"
    date: "2020-04-24"
---

# Super Simple Start to React

In this blog post, Kent C. Dodds demonstrates how to get a minimal React application running in a single index.html file without any build tools. The key idea is to remove all abstractions and add them back one at a time, so you understand exactly what role each piece—React, ReactDOM, and Babel—plays in rendering a user interface. He starts with plain vanilla JavaScript and DOM manipulation, then swaps in React's createElement API, then adds JSX with Babel's standalone in-browser compiler.

By the end, the final setup includes React and ReactDOM loaded via UMD script tags from unpkg, plus Babel standalone to compile JSX in the browser. The example renders "Hello World" into a root div. Dodds warns that this approach is not recommended for production, but it is a useful foundation for learning React's core abstractions and understanding how React elements are turned into real DOM nodes. The post links to his Beginner's Guide to React for further learning.

- Strip away all build tools and start with a plain index.html to isolate what React, ReactDOM, and Babel each do.
- React's createElement API creates plain JavaScript objects describing the UI; ReactDOM.render takes those elements and mounts them into the DOM.
- JSX is not understood by browsers; Babel compiles JSX into React.createElement calls.
- You can run Babel in the browser using @babel/standalone and a <script type="text/babel"> tag, but this setup is only for learning, not production.
- Final minimal setup requires three script tags: react, react-dom, and @babel/standalone.