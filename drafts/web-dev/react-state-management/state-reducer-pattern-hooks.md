---
domain: web-dev
subdomain: react-state-management
concept: state-reducer-pattern-hooks
title: The State Reducer Pattern with React Hooks
sources:
  - title: "The State Reducer Pattern with React Hooks"
    url: "https://kentcdodds.com/blog/the-state-reducer-pattern-with-react-hooks"
    author: "Kent C. Dodds"
    date: "2020-04-06"
---

# The State Reducer Pattern with React Hooks

Kent C. Dodds revisits the state reducer pattern he originally developed for use in downshift, a render-prop "headless" input component that manages state like isOpen, selectedItem, highlightedIndex, and inputValue. Since React Hooks now handle logic-sharing better than render props, he shows how the pattern transfers to hooks. The core value is inversion of control: the API author lets the API consumer control how state updates happen internally. For example, downshift's default closes the menu on selection, but a multi-select use case needs the menu to stay open, which the pattern enables.

The mechanics are a five-step flow: the end user performs an action, the dev calls dispatch, the hook determines the necessary changes, the hook calls the developer's code for further changes (the inversion of control), and the hook applies state changes. Using a contrived useToggle example, Dodds starts from a useState-based hook and shows how a consumer could supply a modifyStateChange function to intercept updates — such as blocking toggling after four clicks — but this initial API also blocked the Switch On/Off buttons unintentionally.

To fix that, the callback is renamed reducer and receives an action with a type, with the hook exporting its own toggleReducer and actionTypes so consumers can call the base reducer and adjust results selectively (e.g. only override on when action.type === actionTypes.toggle). The implementation then rewrites the hook from useState to useReducer, passing the consumer's reducer to useReducer and defaulting to toggleReducer when none is given. The final hook exports useToggle, actionTypes, and toggleReducer, so consumers can either use the built-in reducer or supply their own for full control.

Dodds notes the pattern works best on complex hooks and components like downshift, and that downshift has plans to ship a hook implementation.

- The state reducer pattern implements inversion of control, letting API consumers modify how a hook/component updates state internally.
- Converting the hook to useReducer makes combining the library's reducer with a consumer-provided reducer straightforward.
- Exporting actionTypes and the base reducer (toggleReducer) lets consumers delegate to defaults while selectively overriding specific action types.
- A default reducer parameter (reducer = toggleReducer) keeps the common case simple while enabling full control for advanced users.
- The pattern is most valuable for complex hooks/components such as downshift, and the article notes downshift plans to implement a hook.