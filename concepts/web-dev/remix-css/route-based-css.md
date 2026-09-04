---
domain: web-dev
subdomain: remix-css
concept: route-based-css
title: How Remix makes CSS clashes predictable
sources:
  - title: "How Remix makes CSS clashes predictable"
    url: "https://kentcdodds.com/blog/how-remix-makes-css-clashes-predictable"
    author: "Kent C. Dodds"
    date: "2021-10-13"
---

# How Remix makes CSS clashes predictable

CSS clashes happen because the cascade makes it hard to know whether a style change will have unintended effects. Traditional solutions include naming conventions, pre-processors, CSS modules, CSS-in-JS, and utility classes, but these all still require the CSS to be present on every page. Remix offers a simpler approach: route modules can declare which CSS files they need via the `links` export, and Remix automatically adds those `<link>` tags when the route is active and removes them when the route changes. This ensures a CSS file is only loaded on the pages that actually use it, so you can statically determine which routes a given CSS file affects without needing namespacing (kentcdodds.com, 2021).

The author illustrates the behavior with an example: an `about.css` file turns page `h1`s blue while on `/about`, but the `<link>` tag is removed when navigating away, so the `h1` returns to its normal color. This is described as a "brilliantly simple feature unique to Remix" that gives developers confidence in the impact of their CSS edits. For reusable component styles, the author advises placing their CSS on every page that uses the component (often the root route), but then you must be mindful of namespacing relative to other active CSS files. Ultimately, the author recommends using Tailwind CSS for most styling because it sidesteps cascade issues and adds useful constraints, but acknowledges Remix's route-based CSS is a great fallback for one-off or non-Tailwind styles.

- Remix connects CSS files to route modules using the `links` export, loading them only when the route is active and removing them when the route is no longer active.
- This makes the impact of CSS changes predictable and statically knowable, eliminating the need for manual namespace classes or CSS-in-JS for page-specific styles.
- For reusable components, CSS must be loaded on every page that uses the component—typically via the root route—and then namespacing relative to other active styles is still important.
- The author recommends Tailwind as a primary styling solution but values Remix's route-level CSS handling for maintainable one-off styles.