---
domain: web-dev
subdomain: frontend-component-design
concept: make-impossible-states-impossible
title: Make Impossible States Impossible
sources:
  - title: "Make Impossible States Impossible"
    url: "https://kentcdodds.com/blog/make-impossible-states-impossible"
    author: "Kent C. Dodds"
    date: "2018-09-10"
---

# Make Impossible States Impossible

The article introduces the phrase “make impossible states impossible,” which Kent C. Dodds first heard from David Khourshid at React Rally 2017 and notes is popular in the Elm community (Kent C. Dodds, 2018). The core idea is to design APIs so that invalid or contradictory state combinations cannot be expressed, avoiding ambiguous questions like how to render a component with conflicting props.

Using an `Alert` component example, the article shows that boolean props such as `success`, `warning`, and `danger` allow impossible combinations like `<Alert success warning>`. This raises unclear rendering choices and maintenance problems. The proposed fix is to replace multiple booleans with a single `type` prop whose valid values represent the possible states, making it impossible to select more than one state at a time.

Dodds concludes that converting a boolean value to an enum is only one mechanism for achieving this, and that the broader concept can simplify component and application state. He recommends David Khourshid’s talk and xstate for further ideas. A bonus section shows a Babel macro example that replaces `line` and `column` imports with the source location where they appear, illustrating custom compile-time transforms.

- Design component APIs so contradictory or invalid states cannot be represented.
- Replace multiple boolean flags with a single enum-like `type` prop to allow only one valid state.
- The phrase is attributed to David Khourshid’s React Rally 2017 talk and is also popular in the Elm community.
- The concept generalizes beyond booleans and can simplify component and application state.
- A bonus Babel macro example demonstrates compile-time replacement of imports with source line/column values.