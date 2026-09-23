---
domain: web-dev
subdomain: react-components
concept: downshift
title: Introducing downshift for React
sources:
  - title: "Introducing downshift 🏎 for React ⚛️"
    url: "https://kentcdodds.com/blog/introducing-downshift-for-react"
    author: "Kent C. Dodds"
    date: "2017-08-23"
---

# Introducing downshift for React

downshift is a minimal React primitive for building “item selection” components such as autocomplete, typeahead, dropdown, select, and combobox. It manages user interaction, state, and most accessibility, while leaving all rendering to the developer, avoiding the larger API surface and rendering constraints of libraries that render the input and menu themselves (kentcdodds.com).

Its API relies on a render callback and “prop getters.” The source contains no React.createElement or JSX; instead, the render function receives state and helpers like getInputProps, getItemProps, getLabelProps, and getMenuProps, which the developer spreads onto their own elements. This allows custom filtering, async item loading, or even no input at all for dropdown use cases (kentcdodds.com).

downshift also uses controlled props for isOpen, selectedItem, inputValue, and highlightedIndex, mirroring React’s controlled input pattern: passing one of these props makes downshift reference that prop instead of tracking it internally. Accessibility was a key focus, with an audit by Marcy Sutton and VoiceOver testing; the author claims it is the most accessible component of its kind based on his survey (kentcdodds.com).

The library is smaller than comparable solutions—its UMD build was 14.34kb uncompressed—and works with preact. A preact-habitat experiment produced a frameworkless autocomplete in less than 26kb including downshift, preact, and preact-habitat. It was built for PayPal’s country and recipient selectors, used in CodeSandbox, and the author encourages the community to build downshift-powered features on top of it (kentcdodds.com).

- downshift is a React primitive for item selection components that handles state, interaction, and accessibility but does not render UI.
- It uses the render prop pattern and prop getters (getInputProps, getItemProps, etc.), with no React.createElement or JSX in its source.
- Controlled props for isOpen, selectedItem, inputValue, and highlightedIndex let consumers take full state control.
- Accessibility was audited and tested with VoiceOver; the author claims it is the most accessible component of its kind.
- It is small (14.34kb UMD uncompressed), works with preact, and was built for PayPal’s country/recipient selectors.