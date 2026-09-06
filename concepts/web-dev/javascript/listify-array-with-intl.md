---
domain: web-dev
subdomain: javascript
concept: listify-array-with-intl
title: Listify a JavaScript Array
sources:
  - title: "Listify a JavaScript Array"
    url: "https://kentcdodds.com/blog/listify-a-java-script-array"
    author: "Kent C. Dodds"
    date: "2021-02-18"
---

# Listify a JavaScript Array

The article demonstrates how to format arrays into human-readable lists, arguing that `.join(', ')` is insufficient. It introduces the `Intl.ListFormat` API, which supports multiple locales and options like `style` (`long`, `short`, `narrow`) and `type` (`conjunction`, `disjunction`, `unit`), automatically handling grammar and punctuation such as the Oxford comma.

- `Intl.ListFormat` provides a standardized way to format lists with locale-aware conjunctions, disjunctions, and units.
- Options include `style` (`long`, `short`, `narrow`) and `type` (`conjunction`, `disjunction`, `unit`), affecting output like 'Sojourner, Opportunity, Spirit, Curiosity, and Perseverance'.
- The API supports many locales, making it unnecessary to hand-roll list formatting for internationalization.
- The author initially wrote a custom `reduce`-based `listify` function but later simplified it by wrapping `Intl.ListFormat`, showing preference for platform APIs when possible.
- Browser support should be verified via caniuse.com or MDN, and TypeScript may require custom type declarations for `Intl.ListFormat`.