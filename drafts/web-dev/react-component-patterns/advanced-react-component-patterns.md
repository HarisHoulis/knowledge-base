---
domain: web-dev
subdomain: react-component-patterns
concept: advanced-react-component-patterns
title: Updated Advanced React Component Patterns
sources:
  - title: "💯 UPDATED: Advanced React Component Patterns ⚛️"
    url: "https://kentcdodds.com/blog/updated-advanced-react-component-patterns"
    author: "Kent C. Dodds"
    date: "2018-06-01"
---

# Updated Advanced React Component Patterns

Kent C. Dodds announces that his Advanced React Component Patterns course has been completely updated and re-recorded, with a follow-along CodeSandbox (source). The update was prompted by React 16.3.0, whose new APIs improved the usability of several component patterns (source).

The biggest change is the Context API, which makes compound components more flexible and enables lessons on validating Context Consumers and preventing unnecessary rerenders of consumers (source). Render props lessons were also re-recorded, and prop collections and prop getters remain because they are still useful (source).

The update adds a new state reducer pattern, which Dodds implemented in downshift, plus expanded and simplified control props lessons (source). The provider pattern is now covered in a single lesson because the Context API is a built-in implementation of it, and Higher Order Components are simplified using React.forwardRef (source). The course is 20 minutes shorter than the previous version despite extra lessons, because React keeps getting better at enabling these patterns (source).

- The course was fully re-recorded and updated for React 16.3.0.
- The Context API improves compound components, consumer validation, and rerender control.
- A new state reducer pattern is added, based on downshift, along with expanded control props lessons.
- The provider pattern is condensed into one lesson because Context API is a built-in provider pattern.
- Higher Order Components are updated to use React.forwardRef.