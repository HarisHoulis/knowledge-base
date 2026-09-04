---
domain: web-dev
subdomain: remix-framework
concept: remix-user-experience-and-code-simplicity
title: Why I Love Remix
sources:
  - title: "Why I Love Remix"
    url: "https://kentcdodds.com/blog/why-i-love-remix"
    author: "Kent C. Dodds"
    date: "2021-11-13"
---

# Why I Love Remix

Kent C. Dodds explains his enthusiasm for the Remix web framework, emphasizing that it enables building excellent user experiences while keeping the application code simple and maintainable. He states that Remix manages complex concerns like state and race conditions automatically, so developers avoid common pitfalls such as stale data and manual fetch handling. The framework relies on web platform APIs and supports server rendering and progressive enhancement, making sites fast and resilient even on poor network connections. Remix's declarative APIs for loaders, actions, forms, and error boundaries reduce boilerplate and allow fully typed client-server communication. Dodds highlights how Remix allows building full-featured apps without complex GraphQL clients or layout components, and simplifies optimistic UI and authentication. Overall, he concludes that Remix lets him write simple code while delivering a high-quality user experience.

- Remix automatically handles difficult state management, race conditions, and stale data issues, improving user experience without extra work.
- The framework promotes progressive enhancement: forms work via standard HTML even before JavaScript loads.
- Declarative APIs for data loading, mutations, and errors simplify the code and keep it close to web platform standards.
- Remix enables deploying the same app to any platform with adapter changes, and avoids data overfetching without needing GraphQL.
- The better you get at Remix, the better you get at the web because it uses built-in platform APIs.