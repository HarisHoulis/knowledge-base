---
domain: web-dev
subdomain: react-testing
concept: testing-render-prop-components
title: Testing React Components That Use Render Props
sources:
  - title: "Testing ⚛️ components using render props"
    url: "https://kentcdodds.com/blog/testing-components-using-render-props"
    author: "Kent C. Dodds"
    date: "2018-01-08"
---

# Testing React Components That Use Render Props

Kent C. Dodds explains that render props are an implementation detail, so E2E tests generally should not change when a component uses a render prop component (source). The higher you go up the testing pyramid, the less implementation details matter; at the E2E level, you interact with the component as a user would (source).

For integration tests, Dodds recommends mounting the component and interacting with it normally, without indicating that it uses a render prop component. In his FruitAutocomplete example built on Downshift, tests check menu visibility, keyboard interaction, search, and selection through the rendered UI rather than through Downshift internals (source). He suggests testing the render prop component itself well, then adding high-level tests for consumers (source).

Unit tests are trickier. One approach is to extract the render prop function and export it, then call it directly in tests with stubbed Downshift props, but this requires stubbing what Downshift passes and exporting an implementation detail (source). Another approach is to mount the component, find Downshift, and access its render prop, but this couples the test to the implementation even more (source). Mocking downshift with jest.mock is noted as no better (source).

Dodds concludes that for components using render props, sticking with an integration test is preferable to unit testing the render function, because it provides more confidence. For components requiring providers like react-redux or React Router, he notes rendering within a provider and links to examples from his testing workshop (source).

- Render props are an implementation detail, so E2E tests should not need to change when a component uses a render prop component (source).
- Integration tests can mount the component and interact through the UI; the FruitAutocomplete example tests menu, keyboard, search, and selection without referencing Downshift (source).
- Unit testing a render prop is harder: options include exporting the render function and stubbing props, or accessing the render prop from the mounted component, but both couple tests to implementation details (source).
- Dodds recommends testing the render prop component well, then writing high-level tests for its consumers, and concludes integration testing is preferable here (source).