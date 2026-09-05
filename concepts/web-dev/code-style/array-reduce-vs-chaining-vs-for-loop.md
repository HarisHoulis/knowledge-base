---
domain: web-dev
subdomain: code-style
concept: array-reduce-vs-chaining-vs-for-loop
title: Array reduce vs chaining vs for loop
sources:
  - title: "Array reduce vs chaining vs for loop"
    url: "https://kentcdodds.com/blog/array-reduce-vs-chaining-vs-for-loop"
    author: "Kent C. Dodds"
    date: "2021-05-24"
---

# Array reduce vs chaining vs for loop

Kent C. Dodds discusses a Node script where he used chained array methods (`map`, `filter`, `map`) to build shell commands for moving files [1]. He notes that some critics suggested using `reduce` to avoid multiple array passes, but he argues that for a one-off script, performance is a low priority, and the actual bottleneck was running the commands, not iterating over the array [1]. He demonstrates a `reduce` version and a `for...of` version, observing that `reduce` is more complex and the chain is simpler [1]. He concludes that he typically chooses between chaining and `for...of`, with `for...of` preferred when performance is a concern, and that he rarely uses `reduce` but may consider it case-by-case [1].

- Performance optimizations like using `reduce` to avoid extra array loops are often irrelevant in one-off scripts where the real bottleneck is elsewhere.
- Chaining `map`, `filter`, and `map` can be more readable and simpler than a single `reduce` that combines all steps.
- A `for...of` loop can provide a simple and performant alternative when iteration count is a genuine concern.
- Code simplicity is subjective; the author chooses between chaining and `for...of` based on context.
- The example script's heavy operation was executing shell commands, not array processing.