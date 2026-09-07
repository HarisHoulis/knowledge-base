---
domain: web-dev
subdomain: css-custom-properties
concept: css-variables
title: Super Simple Start to CSS Variables
sources:
  - title: "Super Simple Start to css variables"
    url: "https://kentcdodds.com/blog/super-simple-start-to-css-variables"
    date: "2020-10-28"
---

# Super Simple Start to CSS Variables

The article introduces CSS variables, also known as CSS custom properties, as a platform feature for styling. The author clarifies that the technical term is "CSS Custom Properties" and that it is often called "CSS Variables" interchangeably. They provide a minimal example where a custom property is defined on the :root pseudo-class and consumed with the var() function, showing how to set a default text color.

- CSS Variables and CSS Custom Properties are the same thing, with the latter being the technical term.
- Define custom properties on selectors like :root and use var(--name) to apply them, with scoped definitions overriding inherited ones via the cascade.
- Custom property values can be changed at runtime via JavaScript using element.style.setProperty('--name', value).
- The article provides simple, practical examples of scoping and dynamic updates.