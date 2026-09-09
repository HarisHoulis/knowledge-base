---
domain: web-dev
subdomain: http-client
concept: custom-fetch-wrapper
title: Replace axios with a simple custom fetch wrapper
sources:
  - title: "Replace axios with a simple custom fetch wrapper"
    url: "https://kentcdodds.com/blog/replace-axios-with-a-simple-custom-fetch-wrapper"
    author: "Kent C. Dodds"
    date: "2020-03-30"
---

# Replace axios with a simple custom fetch wrapper

The article argues that for browser-based HTTP requests, a simple custom wrapper around the native fetch API is often preferable to using axios. It highlights benefits such as a smaller API surface, reduced bundle size, fewer dependency update issues, immediate bug fixes, and conceptual simplicity. The author demonstrates building a wrapper incrementally, starting with a basic function that calls fetch and parses JSON, then adding error handling by checking response.ok, support for JSON bodies via the body option, and automatic Authorization headers using a token stored in localStorage. Finally, it handles 401 responses by logging the user out and refreshing the page. The article concludes that while axios remains a valid choice, especially in Node.js, a tailored fetch wrapper can cover most browser use cases and can be extended with custom logic per request or per application.

- A custom fetch wrapper can replace axios in the browser, reducing bundle size and simplifying the API surface.
- Native fetch does not reject on HTTP error statuses, so the wrapper should check response.ok (or response.status) and reject manually.
- The wrapper can be extended to stringify JSON bodies, add Authorization headers from localStorage, and handle 401 responses by logging the user out.
- Further wrappers can be created around the base client for specific resources (e.g., list-items).