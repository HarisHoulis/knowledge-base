---
domain: engineering-culture
subdomain: open-source-contribution
concept: learning-open-source-codebases
title: How I Learn an Open Source Codebase
sources:
  - title: "How I learn an Open Source Codebase"
    url: "https://kentcdodds.com/blog/how-i-learn-an-open-source-codebase"
    author: "Kent C. Dodds"
    date: "2018-05-14"
---

# How I Learn an Open Source Codebase

Kent C. Dodds answers a common question he receives—how to learn an open source codebase and understand other people's code. His foundational observation, repeated from his "Open Source Stamina" post, is that you contribute best to something you use regularly: sustainable contributions come from projects you use often, because your familiarity with the use cases helps you understand the code (kentcdodds.com).

He lays out a sequence of steps. First, read the contributing guidelines, found in `README.md` or `CONTRIBUTING.md`; if none exists, file an issue asking the maintainer to create one or explain what they expect. When setting up the project locally, install dependencies and make sure the tests pass before making changes—otherwise you risk mistaking pre-existing test failures for problems caused by your own change, something he admits has happened to him (kentcdodds.com).

Then follow the code in your head starting from the entry point you care about, such as a function call or a CLI invocation with a certain argument; this looks intimidating in large projects but is more manageable than it appears. Reading and running the tests helps, and deliberately breaking things is another way to learn. Logging via `console.log` and stepping through with debuggers—ideally in browser DevTools, with a link to Paul Irish's article on debugging Node.js with Chrome DevTools—are tried-and-true mechanisms; he also suggests running the project's code in the context of your own application, referencing his "Spelunking in node_modules" post (kentcdodds.com).

Finally, he recommends asking someone on the project to walk you through part of the code, and making it worth their time by offering to record the conversation and publish it, since new-contributor material is valuable to maintainers. He lists examples, including "Why, What, and How of React Fiber with Dan Abramov and Andrew Clark," "React events in depth," "JavaScript & React Testing with Jest," and "Contributing to ReactJS" (kentcdodds.com).

- Contribute to projects you use regularly—familiarity with the use cases makes the code easier to understand.
- Read the contributing guidelines (`README.md` / `CONTRIBUTING.md`) first, and ask maintainers to write one if missing.
- Set up the project and confirm tests pass before changing anything, so pre-existing failures aren't misattributed to your change.
- Learn by following code from an entry point, reading/running tests, breaking things, and using console.log or DevTools stepping (including running the code inside your own app).
- Ask a maintainer to walk you through the code and offer to record and publish the conversation as a resource for new contributors.