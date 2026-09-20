---
domain: web-dev
subdomain: react-component-patterns
concept: prop-getters
title: How to give rendering control to users with prop getters
sources:
  - title: "How to give rendering control to users with prop getters"
    url: "https://kentcdodds.com/blog/how-to-give-rendering-control-to-users-with-prop-getters"
    author: "Kent C. Dodds"
    date: "2017-10-02"
---

# How to give rendering control to users with prop getters

Prop getters are a React pattern that lets component authors hand rendering control to users. They work with the render prop pattern: a function returns props when called, and users spread those props onto the right elements to connect the component's behavior to their own markup [source](https://kentcdodds.com/blog/how-to-give-rendering-control-to-users-with-prop-getters).

The article explains the pattern through `react-toggled`. Its `getTogglerProps` function returns `aria-controls`, `aria-expanded`, spreads any user-provided props, and composes `onClick` as `callAll(props.onClick, this.toggle)` [source](https://kentcdodds.com/blog/how-to-give-rendering-control-to-users-with-prop-getters). This solves the conflict that occurs when both the component and the user need an `onClick` handler. If users instead spread a plain props object alongside their own props, one `onClick` overrides the other, breaking either the user's handler or the toggle behavior [source](https://kentcdodds.com/blog/how-to-give-rendering-control-to-users-with-prop-getters).

The `callAll` helper calls every provided function if it exists, so both handlers run. The `Toggle` component uses `this.props.children` as a render prop and unwraps it for Preact compatibility, returning state and helpers to the user [source](https://kentcdodds.com/blog/how-to-give-rendering-control-to-users-with-prop-getters). The result is that the component handles generic logic while users decide what to render and how to style it based on state. The article lists `downshift`, `react-toggled`, `dub-step`, and `react-stepper-primitive` as projects using the prop getters pattern.

- Prop getters are functions that return props for users to spread onto elements, enabling render-prop components to delegate rendering.
- They allow safe composition of props like `onClick` via `callAll(props.onClick, this.toggle)`, so component and user handlers both run.
- Passing a plain object instead of using a prop getter can cause user props and component props to override each other.
- The pattern is used in `downshift`, `react-toggled`, `dub-step`, and `react-stepper-primitive`.