---
domain: web-dev
subdomain: react-state-management
concept: state-colocation
title: Application State Management with React
sources:
  - title: "Application State Management with React"
    url: "https://kentcdodds.com/blog/application-state-management-with-react"
    author: "Kent C. Dodds"
    date: "2020-07-21"
---

# Application State Management with React

In this article, Kent C. Dodds argues that React developers often over-engineer state management by reaching for libraries like Redux for all state, when React itself provides a solid solution. He suggests that the key is to map state to the application's component tree structure, keeping state colocated with the components that need it. While Redux solved the prop-drilling problem, it often leads to putting all state into a central store, including simple UI state, which adds unnecessary indirection and complexity. Dodds explains, 'React is a state management library' and emphasizes using built-in features first.

Dodds recommends lifting state up and using component composition to avoid prop drilling. When shared state is needed across distant components, React's Context API—now officially supported—combined with hooks offers a clean solution. He demonstrates a `CountProvider` with a custom `useCount` hook, and notes that different parts of the app tree can have their own providers, keeping state close to where it is used. This colocation improves performance and simplifies code splitting.

The article also distinguishes between 'server cache' state and 'UI state,' recommending a caching library like react-query for server data rather than managing it as React state. On performance, Dodds advises checking whether components really need to re-render after a state change; following colocation practices usually prevents performance problems.

- React itself is a state management library; use local state and lifting state up as the first approach.
- Avoid prop drilling with component composition before reaching for React Context.
- Use Context for shared state, but keep providers close to where they are needed, not global.
- Separate server cache (use react-query) from UI state to manage them appropriately.
- Performance issues are often caused by unnecessary re-renders; colocation reduces them.