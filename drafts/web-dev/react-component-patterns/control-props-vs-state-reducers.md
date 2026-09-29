---
domain: web-dev
subdomain: react-component-patterns
concept: control-props-vs-state-reducers
title: When to use Control Props or State Reducers
sources:
  - title: "When to use Control Props or State Reducers"
    url: "https://kentcdodds.com/blog/control-props-vs-state-reducers"
    author: "Kent C. Dodds"
    date: "2018-06-11"
---

# When to use Control Props or State Reducers

Both control props and state reducers expose state management to component consumers, though their APIs differ. Control props, as in `<input value={...} onChange={...} />`, let consumers fully control state from outside the component (source). State reducers, supported by downshift but not built-in React elements, let consumers intercept and modify state changes, e.g., preventing a menu from closing after an item is selected (source).

Control props are more powerful because they allow complete external control over state. In the Toggle example, changing the input text controls the toggle, and clicking the toggle controls the input, requiring the consumer to manage state and change handlers in a class component (source). The cost is that the consumer must completely manage the component's state themselves (source).

State reducers do not require consumers to manage the component's state themselves, though they can manage some of their own state as needed. In the toggle click-limit example, a state reducer returns `on: false` after four clicks while the component tracks click count internally (source). This can be simpler than a control prop for such cases. The biggest limitation is that a state reducer cannot set state outside the component's normal `setState` calls, so it could not implement the first example (source).

Choose control props when you need complete external control, and state reducers when you want to influence state changes with less state-management overhead (source).

- Control props allow complete control over a component's state from outside, but require the consumer to manage state and change handlers (source).
- State reducers let consumers intercept and modify state changes without owning all of the component's state, as shown by downshift keeping the menu open after an item click (source).
- State reducers cannot set state outside the component's normal `setState` calls, limiting them for scenarios that need full external control (source).
- Use state reducers for lighter state-change interception; use control props when complete external state control is required (source).