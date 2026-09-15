---
domain: web-dev
subdomain: react-testing
concept: testing-react-hooks
title: React Hooks: What's Going to Happen to My Tests?
sources:
  - title: "React Hooks: What's going to happen to my tests?"
    url: "https://kentcdodds.com/blog/react-hooks-whats-going-to-happen-to-my-tests"
    author: "Kent C. Dodds"
    date: "2018-12-24"
---

# React Hooks: What's Going to Happen to My Tests?

Kent C. Dodds addresses concerns that refactoring React class components to function components with hooks will break existing tests. Enzyme tests that call `.instance()` or `.state()` depend on class component internals and will fail once components become function components, because there is no component instance. The recommended fix is to avoid implementation details and write tests that interact with the UI as a user would, using React Testing Library; such tests pass unchanged when a Counter class component is converted to a function component with `useState` ([Kent C. Dodds, 2018](https://kentcdodds.com/blog/react-hooks-whats-going-to-happen-to-my-tests)).

- Avoid Enzyme APIs like `.instance()` and `.state()` because they rely on class component instances and break when refactoring to hooks.
- Write tests with React Testing Library that exercise user-visible behavior, so tests continue passing during class-to-hooks refactors.
- `useEffect` is not equivalent to lifecycle methods; effects are scheduled after render and can be covered by `act`/React Testing Library integration.
- Render props can be preserved while extracting custom hooks, allowing gradual adoption; test custom hooks with a render-prop wrapper or `renderHook` from `@testing-library/react`.
- Good tests and type definitions make refactors safer, but only if they do not depend on implementation details.