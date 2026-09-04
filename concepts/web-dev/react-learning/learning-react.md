---
domain: web-dev
subdomain: react-learning
concept: learning-react
title: How to React
sources:
  - title: "How to React ⚛️"
    url: "https://kentcdodds.com/blog/how-to-react"
    author: "Kent C. Dodds"
    date: "2021-11-03"
---

# How to React

Kent C. Dodds shares advice on learning React effectively, emphasizing the importance of understanding abstractions by weighing their benefits and costs. He recommends starting with JavaScript and modern JS features before diving into React, as React is heavily JavaScript-based and 90% of React proficiency comes from strong JavaScript knowledge ("Start with JavaScript + Modern JS"). He suggests free resources like JavaScript30 and his own ES6 workshop.

He advocates learning React itself without tooling, using plain HTML files and progressive enhancement, as demonstrated in his free egghead course "The Beginner's Guide to React." He advises against premature dependency adoption, suggesting developers feel the pain a dependency solves before adding it. For real-world apps, he recommends using Remix as a React framework, and for state management, he notes that React's built-in useState and lifting state up often suffice, calling React an application state management library and stating "you don't need Redux" ("State management"). He also recommends Tailwind CSS for styling once CSS grows beyond a few hundred lines.

The overall pattern is to delay abstraction and tooling until the need is clear, following a path from plain JavaScript, to React fundamentals, to dependencies and frameworks like Remix, and finally to deeper React patterns.

- Understand the benefit and cost of any abstraction before adopting it; avoid paying cost for problems you don't have.
- Start with plain JavaScript and modern ES features because React is mostly JavaScript — 90% of React effectiveness is JS knowledge.
- Learn React without tooling first (e.g., via index.html files) to avoid complexity and appreciate what React actually does.
- Do not add dependencies or state management libraries like Redux until you feel the pain they solve; React's built-in state may be enough.
- When building real apps, use a framework like Remix for routing and data management, and consider Tailwind CSS for styling at scale.