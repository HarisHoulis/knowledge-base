---
domain: web-dev
subdomain: React component patterns
concept: render-props-composition
title: Compose Render Props
sources:
  - title: "Compose Render Props"
    url: "https://kentcdodds.com/blog/compose-render-props"
    author: "Kent C. Dodds"
    date: "2018-04-09"
---

# Compose Render Props

Kent C. Dodds explains that the render prop pattern's real power is as a building block for components that have useful opinions. Downshift, which he created, is positioned as primitives for enhanced input components, and libraries like mui-downshift and evergreen-ui build on it by adding visual opinions and defaults while retaining the logic (Dodds, 2018).

To illustrate composition, Dodds describes a livestreamed amount input component with currency selection and special input behavior, such as changing font size as it grows. Although the initial three implementations share the layout `{currencyCode}{input}{currencyCodeSelect}`, their styles differ; he expects future layout and style variations (Dodds, 2018).

He plans layers of abstraction from top to bottom: a styles component, a layout component, and a logic component. Initially there is one logic component, one layout component, and three style components. If a future component needs the same behavior but a different layout, a new layout and style can be built on the logic component, reusing about 90% of the work (Dodds, 2018).

The benefit is clear separation of functionality, which improves flexibility, deletability, and usability of the API (Dodds, 2018).

- Render props serve as primitives and building blocks for higher-level components with opinions.
- Downshift separates enhanced selection input logic, while libraries like mui-downshift and evergreen-ui layer visual styling and defaults on top.
- The amount input example is split into style, layout, and logic layers.
- This layering enables reuse: new layouts and styles can be added atop the same logic component, improving flexibility and deletability.