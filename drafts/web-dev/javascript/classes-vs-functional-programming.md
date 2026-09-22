---
domain: web-dev
subdomain: javascript
concept: classes-vs-functional-programming
title: Classes, Complexity, and Functional Programming
sources:
  - title: "Classes, Complexity, and Functional Programming"
    url: "https://kentcdodds.com/blog/classes-complexity-and-functional-programming"
    author: "Kent C. Dodds"
    date: "2017-06-06"
---

# Classes, Complexity, and Functional Programming

Kent C. Dodds argues that JavaScript classes add complexity, largely through the `this` keyword, and that functions plus plain objects are often simpler for maintainable code (Dodds, 2017). He first shows a `Person` class where methods live on the prototype, allowing many instances to share method references. The cost is that understanding the code requires objects, functions/closures, `this`, and prototype inheritance.

`this` is hard because its value is determined by how a function is called and can differ each time; ES5 `bind` and ES2015 arrow functions exist to manage it (Dodds, 2017, quoting MDN). Detaching a method (`const getGreeting = person.getGreeting`) loses `this` and throws; React class components hit the same issue when handlers are passed to `onClick` without binding.

A functional alternative uses pure functions and immutable plain objects, such as `setName` returning `Object.assign({}, person, { name: strName })`. This avoids `this`, reduces state to track, and makes unit testing easy by calling functions with inputs and asserting outputs. He notes functional programming is about being easier to understand so long as it is fast enough, and performance concerns are often lower priority.

He also presents the Module pattern/Revealing Module pattern as another `this`-free approach using closures and objects. Its trade-off is that every instance gets its own copy of functions, unlike class prototype sharing. Classes remain useful for hot code and React components with state/lifecycle; private class fields or WeakMaps can address privacy but do not remove `this` complexity. Conclusion: classes are an optimization, not a simplification.

- `this` is determined by call site and adds cognitive load; detaching or passing methods as callbacks commonly breaks code.
- A functional style with pure functions and plain objects avoids `this` and makes unit testing straightforward.
- The Module pattern avoids `this` but creates per-instance function copies; classes share methods via the prototype.
- Classes can help performance-critical code and React state/lifecycle components, but for most cases functions and objects are simpler.