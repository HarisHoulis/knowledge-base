---
domain: web-dev
subdomain: react
concept: react-hooks-suspense
title: Introducing a Course on Simplifying React Apps with Hooks and Suspense
sources:
  - title: "Introducing a new course: Simplify React Apps with React Hooks and Suspense"
    url: "https://kentcdodds.com/blog/introducing-a-new-course-simplify-react-apps-with-react-hooks-and-suspense"
    author: "Kent C. Dodds"
    date: "2018-12-03"
---

# Introducing a Course on Simplifying React Apps with Hooks and Suspense

The article announces a course that refactors a modern React codebase using class components into function components using React Hooks and Suspense. The course covers state, side effects, async code, caching, and more by taking an existing app and converting it as much as possible to function components (source). It notes that React Hooks is alpha and subject to change, while React Suspense was officially released as stable in React 16.6.0 with limited support for React.lazy (source).

The course walks through practical refactors: converting render-prop and class components to hooks like useReducer, useContext, useEffect, and useState; handling deep object comparison with useRef; safely setting state on mounted components; extracting custom hooks such as useSetState, usePrevious, useDeepCompareEffect, and useQuery; and refactoring lifecycle methods like componentDidMount and componentWillUnmount into useEffect (source). It also shows how to replace react-loadable with React.lazy and Suspense, and how to preload components with useEffect so users do not wait after finishing a form (source).

- The course refactors a class-based React app to function components using Hooks and Suspense, covering state, effects, async code, and caching (source).
- It demonstrates custom hooks like useSetState, useSafeSetState, usePrevious, useDeepCompareEffect, and useQuery to encapsulate and reuse logic (source).
- React Suspense became stable in 16.6.0 with limited React.lazy support, allowing replacement of react-loadable (source).
- React Hooks is alpha and subject to change, with a 16.x roadmap provided by the React team (source).
- useEffect is used for preloading components and for handling mount/unmount concerns previously handled by class lifecycle methods (source).