---
domain: web-dev
subdomain: react-libraries
concept: downshift-2-release
title: downshift 2.0.0 Released: Accessibility, React Native, ReasonReact, Simpler API, and Improved Docs
sources:
  - title: "downshift 2.0.0 released 🎉"
    url: "https://kentcdodds.com/blog/downshift-2-0-0-released"
    author: "Kent C. Dodds"
    date: "2018-06-15"
---

# downshift 2.0.0 Released: Accessibility, React Native, ReasonReact, Simpler API, and Improved Docs

downshift 2.0.0 was released with a focus on improved accessibility, led primarily by Michael Ball. The release adds a new `getMenuProps` prop getter, which helps add `aria-` attributes to the rendered menu and was also instrumental in fixing a bug with React Portals. Many examples were updated to use more semantically correct elements (source).

The release also highlights React Native support and official ReasonReact bindings, allowing downshift to be used on more platforms. The API was simplified by dropping the `render` prop in favor of only `children`, aligning with React's official context API. Documentation was reorganized to make useful props like `itemToString` more apparent, and a new examples site was launched on CodeSandbox (source).

TypeScript definitions were improved, primarily by @stereobooster, and Flow type definitions are now generated from the TypeScript definitions. The project also launched a Spectrum community for discussions and support. The post thanks numerous open source contributors for making the release possible (source).

- Accessibility improvements add a `getMenuProps` prop getter and `aria-` attributes, and fix a React Portals bug (source).
- The `render` prop is dropped in favor of `children` to align with React's context API (source).
- React Native and ReasonReact support are officially highlighted, with official Reason bindings available (source).
- Improved TypeScript definitions and generated Flow types provide better type safety; docs and examples were improved, including a new CodeSandbox examples site (source).
- A Spectrum community was launched for downshift discussions and support (source).