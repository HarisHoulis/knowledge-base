---
domain: web-dev
subdomain: javascript
concept: pass-by-value
title: JavaScript Pass By Value Function Parameters
sources:
  - title: "JavaScript Pass By Value Function Parameters"
    url: "https://kentcdodds.com/blog/javascript-pass-by-value-function-parameters"
    date: "2021-03-23"
---

# JavaScript Pass By Value Function Parameters

The article explains why changing a variable after passing it to a function does not affect the function's captured parameter. In JavaScript, function arguments are passed by value, not by reference. When a function is called, the engine creates a new variable for each argument, effectively assigning it the value of the passed variable. Thus, reassigning the original variable later has no effect on the parameter variable inside the function (kentcdodds.com).

A common misconception is that closures capture variables by reference. In the example, the inner logger closes over the parameter `arg`, not the outer variable `fruit`. To observe updates, you can pass an object and mutate its property, since objects are shared by reference. The article demonstrates using a `Ref` object wrapper to achieve live updates, illustrating the distinction between reassigning a variable and mutating the value it points to.

- JavaScript function arguments are passed by value, meaning the parameter variable holds a copy of the value at call time.
- Closures capture the parameter variables, not the outer variables that were used as arguments.
- Reassigning the original variable does not change the captured parameter value.
- To share live updates, pass an object and mutate a property on it rather than reassigning the outer variable.