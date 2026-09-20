---
domain: web-dev
subdomain: react
concept: react-as-javascript
title: The Beginner's Guide to ReactJS: Teaching React as Just JavaScript
sources:
  - title: "The Beginner's Guide to ReactJS"
    url: "https://kentcdodds.com/blog/the-beginners-guide-to-reactjs"
    date: "2017-12-18"
---

# The Beginner's Guide to ReactJS: Teaching React as Just JavaScript

Kent C. Dodds describes the design of his beginner React course, which keeps every lesson as an isolated `index.html` file with no tooling, so nothing gets in the way of learning ([source](https://kentcdodds.com/blog/the-beginners-guide-to-reactjs)). The course starts from a blank slate: the first lesson builds `index.html` from scratch and initially uses `document.createElement` for a "Hello World," introducing React APIs gradually ([source](https://kentcdodds.com/blog/the-beginners-guide-to-reactjs)).

Central to the course is the idea that React is "just JavaScript"—objects and functions. He uses `console.log` on `React.createElement` to demonstrate that React elements are plain JavaScript objects, not magic ([source](https://kentcdodds.com/blog/the-beginners-guide-to-reactjs)). He warns against starting beginners with JSX and instead shows JSX as a straightforward abstraction over `React.createElement`, including syntax tips and a lesson on conditionally rendering elements ([source](https://kentcdodds.com/blog/the-beginners-guide-to-reactjs)).

He argues that nailing these fundamentals gives learners a solid understanding: creating React elements is not magic and JSX is a simple abstraction. Once they understand that, learning the rest of React comes more easily ([source](https://kentcdodds.com/blog/the-beginners-guide-to-reactjs)).

- Keep beginner React lessons isolated in plain `index.html` files with no tooling.
- Start from scratch with `document.createElement` before introducing React.
- Use `console.log(React.createElement(...))` to show React elements are plain JavaScript objects.
- Don't start with JSX; teach it as an abstraction over `React.createElement`.
- Understanding these fundamentals makes the rest of React easier to learn.