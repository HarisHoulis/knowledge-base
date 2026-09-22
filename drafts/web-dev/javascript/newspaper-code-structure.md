---
domain: web-dev
subdomain: javascript
concept: newspaper-code-structure
title: Newspaper Code Structure
sources:
  - title: "Newspaper Code Structure"
    url: "https://kentcdodds.com/blog/newspaper-code-structure"
    author: "Kent C. Dodds"
    date: "2015-05-18"
---

# Newspaper Code Structure

The article argues that code should read like a newspaper article: important information at the top and details at the bottom. The author compares a common module structure, where exports and functions are scattered, with a rewritten version that places all exports at the top of the file, making the module's API immediately obvious to anyone reading the code, including on GitHub. The author states this structure makes consuming and maintaining a file much easier because you know exactly what the module exports just by looking at the top (source).

The suggested approach relies on JavaScript function declaration hoisting, which allows function declarations to appear after a return statement inside a closure. In the example, `getBar()` returns an object whose methods are function declarations placed later inside the function body; `longFunction` and `meToo` are also declared after the export statement but remain available because of hoisting. The author says this leverages a JavaScript "quirk" and lets readers ignore implementation details unless they are interested in them (source).

The author notes that this pattern breaks down with ES6 classes because class methods must be structured inside the class body, and long methods can recreate the original readability problem. The author does not offer a definitive solution for classes, but suggests keeping files and functions small to mitigate the issue. The author also emphasizes that readability should not depend on an IDE or editor, since code is often read on GitHub or without tooling (source).

- Put exports and the module API at the top of the file, with implementation details below.
- JavaScript function declarations are hoisted, so helper functions can be declared after the return statement to keep the API visible first.
- Scattered exports make it difficult to discover what a module provides; the author cites a 2000+ line Backbone.View as an example of the problem.
- The pattern is harder to apply to ES6 classes because methods must live inside the class body; keeping files and functions small helps.
- Readability should work for anyone, regardless of editor or IDE, especially when viewing code on GitHub.