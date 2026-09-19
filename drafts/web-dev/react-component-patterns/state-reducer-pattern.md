---
domain: web-dev
subdomain: react-component-patterns
concept: state-reducer-pattern
title: The state reducer pattern
sources:
  - title: "The state reducer pattern ⚛️ 🏎"
    url: "https://kentcdodds.com/blog/the-state-reducer-pattern"
    author: "Kent C. Dodds"
    date: "2018-02-19"
---

# The state reducer pattern

The post describes a downshift issue where a user wanted different state behavior: preventing the menu from closing when an item is selected. It frames this as a common tension in UI libraries: they must make decisions about how a component works and how it looks, and the more decisions they make, the less flexible they become [source]. Downshift uses a render prop to leave appearance to consumers and control props to allow complete control over internal state [source].

To reduce boilerplate for tweaking behavior, the author introduced a prop first called modifyStateChange, later generalized as the state reducer pattern. The state reducer is a function that receives the current state and upcoming changes, and returns the changes that should actually be applied [source]. The upcoming changes include a type from downshift's stateChangeTypes so the reducer can apply logic only for specific events, such as keyDownEnter or clickItem [source].

The example state reducer prevents isOpen from becoming false after selection by returning the upcoming changes but preserving the current isOpen and highlightedIndex for those change types [source]. The author positions the pattern between uncontrolled and controlled components: it does not enable anything beyond control props, but it reduces wiring and boilerplate for customizing how a library works [source]. A simplified toggle component example is provided to illustrate implementation [source].

- UI libraries must balance making behavioral decisions for usefulness against remaining flexible for varied use cases [source].
- The state reducer pattern lets consumers intercept and modify upcoming state changes before they are applied [source].
- A state reducer receives current state and upcoming changes, and returns the changes to apply, not the full state [source].
- Changes include a type from downshift's stateChangeTypes so reducers can target specific interactions like keyDownEnter or clickItem [source].
- The pattern reduces boilerplate compared with control props while still sitting between uncontrolled and controlled component approaches [source].