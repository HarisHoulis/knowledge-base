---
domain: web-dev
subdomain: accessibility
concept: accessible-form-labels
title: Please stop building inaccessible forms (and how to fix them)
sources:
  - title: "Please stop building inaccessible forms (and how to fix them)"
    url: "https://kentcdodds.com/blog/please-stop-building-inaccessible-forms-and-how-to-fix-them"
    author: "Kent C. Dodds"
    date: "2019-02-04"
---

# Please stop building inaccessible forms (and how to fix them)

According to the source, HTML is accessible by default when semantic HTML is used properly, and this article focuses on ensuring form controls are properly labeled. It notes that visually placing text like “Username:” above an `<input>` does not associate that text as a label; without a programmatic label, screen reader users must guess what an input expects when it receives focus (source).

To fix this, the source recommends associating labels with inputs in one of four ways, ordered by preference: `<label for="username">` with `<input id="username">`; `<input aria-labelledby="username">` pointing to a `<label id="username">`; wrapping the input inside the label; or using `<input aria-label="Username">`. The author prefers the for/id approach, finds the wrapping approach workable but harder to style and test with `getByLabelText` without a selector, and dislikes `aria-label` alone because it removes a visible label (source).

The source also advises developers to test forms using only the keyboard, because many forms are impossible to use without a mouse. It notes that proper label association expands the clickable area to include the label, which helps checkboxes and mobile users, and enables `getByLabelText` so tests better resemble how software is used. It recommends using `eslint-plugin-jsx-a11y` and references W3C labeling controls guidance and WCAG technique H44 (source).

- Semantic HTML makes most form controls accessible by default, but labels must be programmatically associated.
- Visual label text alone is insufficient; use `label[for]` + `input[id]`, `aria-labelledby`, a wrapping label, or `aria-label` in preference order.
- The for/id method is preferred; `aria-label` alone is discouraged because it removes the visible label.
- Properly associated labels increase the clickable area, helping checkboxes and mobile users, and support `getByLabelText` for user-centric tests.
- Test forms with keyboard only and use `eslint-plugin-jsx-a11y`.