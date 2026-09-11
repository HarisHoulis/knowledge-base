---
domain: web-dev
subdomain: ui-testing
concept: resilient-ui-tests
title: Making your UI tests resilient to change
sources:
  - title: "Making your UI tests resilient to change"
    url: "https://kentcdodds.com/blog/making-your-ui-tests-resilient-to-change"
    author: "Kent C. Dodds"
    date: "2019-10-07"
---

# Making your UI tests resilient to change

UI tests often select elements by CSS class names, but this is brittle: adding another button with the same class breaks the selector, and styling concerns can conflict with testing concerns when class names are removed for CSS-in-JS (source). Kent C. Dodds argues that tests should resemble how software is used, because users do not care about class names (source).

Instead, use Testing Library queries that find elements the way users find them: by role, label, placeholder, text contents, display value, alt text, title, or test ID, in that order of recommendation (source). For example, query a username field with `getByRole('textbox', { name: /username/i })`, a password field with `getByLabelText('password')`, and a submit button with `getByRole('button', { name: /sign in/i })` (source).

When other queries cannot reliably select an element, use `data-testid` to make the test-to-source relationship explicit, avoiding a `getByClassName` query (source). This approach also works for end-to-end tests; if shipping test attributes is a concern, they can be compiled away with `babel-plugin-react-remove-properties`, though the source suggests that concern is often overstated (source). The conclusion is that tests resembling actual usage are more resilient to change and provide more value, and needing to change tests during refactors or feature additions indicates brittle tests (source).

- Avoid selecting UI elements by CSS class names because class names are primarily for styling and create brittle, implicit coupling between tests and source code.
- Prefer user-facing Testing Library queries such as role, label, placeholder, text, display value, alt text, title, and test ID, in the recommended order.
- Use `data-testid` as a fallback when no reliable user-facing query exists, since it makes the test-to-source relationship explicit.
- Tests that resemble how software is used are more resilient to change and provide more confidence.
- If needed, test ID attributes can be removed from production builds with `babel-plugin-react-remove-properties`.