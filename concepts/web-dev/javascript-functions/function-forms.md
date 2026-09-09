---
domain: web-dev
subdomain: javascript-functions
concept: function-forms
title: Function forms
sources:
  - title: "Function forms"
    url: "https://kentcdodds.com/blog/function-forms"
    author: "Kent C. Dodds"
    date: "2020-04-05"
---

# Function forms

Kent C. Dodds explains his preferred conventions for choosing among JavaScript function forms—function declarations, function expressions, arrow functions, and object methods—in typical React components. He shows a Counter component that mixes an arrow function for the increment callback and a function declaration for the component itself, then notes the frequency of reader questions about this mixing (Dodds, 2020). The author traces his early JavaScript habits, when arrow functions did not exist, and his initial rule of using function expressions for callbacks and object properties, while using function declarations elsewhere due to hoisting of the function definition (Dodds, 2020). With the later introduction of arrow functions and object method syntax, he refined his loose rules: use arrow functions for callbacks, use object methods for multiline or non-returning functions, prefer arrow functions when leveraging implicit return or lexical `this`, and fall back to function declarations otherwise (Dodds, 2020). He acknowledges these are subjective and not meant as hard rules or ESLint-enforced standards, adding that naming functions can sometimes improve debugging (Dodds, 2020).

- Mix arrow functions and function declarations in React code deliberately, based on context.
- Function declarations are preferred by the author for their hoisting behavior.
- Arrow functions are useful for callbacks and for implicit return or lexical `this`.
- These are loose personal rules, not strict practices to enforce with linting.