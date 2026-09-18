---
domain: web-dev
subdomain: react-state-management
concept: prop-drilling
title: Prop Drilling
sources:
  - title: "Prop Drilling"
    url: "https://kentcdodds.com/blog/prop-drilling"
    author: "Kent C. Dodds"
    date: "2018-05-21"
---

# Prop Drilling

Prop drilling (also called threading) is the process of passing data through the React component tree to reach parts of the tree that need it. In the example, Toggle holds on/toggle state; after refactoring, Switch accepts on and onToggle only so it can forward them to SwitchMessage and SwitchButton, even though Switch itself does not need them (source).

The article argues prop drilling is good because it is explicit. Explicit prop passing makes it easier to track where values are initialized, updated, and used, and to answer whether code can be modified/deleted without breaking anything—unlike global variables or AngularJS non-isolate $scope/$rootScope patterns (source).

Problems arise as applications grow. Drilling through many layers can make refactoring data shapes, over-forwarding props, under-forwarding plus abusing defaultProps, and renaming props midway difficult to manage (source).

To avoid issues: don't break out components prematurely, inline render methods when possible, avoid defaultProps for required props, keep state as close to where it's relevant as possible, and use React's Context API for things truly necessary deep in the tree; context remains statically traceable unlike global variables (source).

- Prop drilling is explicit prop passing through component layers; it can improve maintainability by making data flow statically traceable.
- Problems emerge as apps grow: refactoring data shapes, over-forwarding props, under-forwarding with misleading defaultProps, and renamed props.
- Reduce drilling by not breaking out components prematurely, keeping state local, and avoiding defaultProps for required props.
- Use React Context for data truly needed deep in the tree; unlike global variables, context sources and consumers can still be found statically.