---
domain: web-dev
subdomain: react-internals
concept: iterable-functions
title: Rendering a Function with React by Making It Iterable
sources:
  - title: "Rendering a function with React"
    url: "https://kentcdodds.com/blog/rendering-a-function-with-react"
    author: "Kent C. Dodds"
    date: "2017-11-13"
---

# Rendering a Function with React by Making It Iterable

Kent C. Dodds describes a hack used with an internal PayPal `react-i18n` module whose `getContent` API is “sorta-curried” (Kent C. Dodds, 2017). If a content path had a typo, `getContent` returned a string like `{pages.typo.nav.about}`, but chaining another call on that missing path tried to invoke a string and crashed the app (Kent C. Dodds, 2017).

The change was to return a curried function when content is missing, so further calls would not crash. But this created a new problem: React rendered nothing for the missing path, hiding the diagnostic placeholder that would help developers notice broken content, even though the module also logged to the console (Kent C. Dodds, 2017).

To make the missing-path value render visibly, Dodds first tried monkey-patching `toString`, which failed with React’s warning that functions are not valid React children. Stepping through the stack led to `reconcileChildFibers`, where React checks child values as object, string/number, array, or iterator before throwing or warning (Kent C. Dodds, 2017). Because the returned value had to remain a function, he made the function iterable via `Symbol.iterator`, returning `{ done, value: pathAsString }`; React then treated it as an iterable and rendered the missing path string (Kent C. Dodds, 2017). He notes the feature was removed in React 16 and should not be relied on (Kent C. Dodds, 2017).

- The internal `getContent` API is sorta-curried: missing paths previously returned a string placeholder, but chaining calls on that string caused app-crashing errors.
- Changing missing paths to return a curried function prevented crashes, but React rendered nothing, so the missing path was no longer visible.
- React’s `reconcileChildFibers` accepts objects, strings/numbers, arrays, and iterators as children; functions trigger a warning.
- Making the content getter function iterable via `Symbol.iterator` let React render the full missing path string.
- The article warns this React feature was removed in React 16 and should not be relied on.