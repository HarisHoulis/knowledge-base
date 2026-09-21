---
domain: web-dev
subdomain: css-in-js
concept: glamorous
title: Introducing glamorous 💄
sources:
  - title: "Introducing glamorous 💄"
    url: "https://kentcdodds.com/blog/introducing-glamorous"
    author: "Kent C. Dodds"
    date: "2017-04-04"
---

# Introducing glamorous 💄

Kent C. Dodds introduced glamorous, a React component styling library, after building something for PayPal and tiring of manually combining glamor CSS classes with React components (source). He tried styled-components and liked its composable API, but needed right-to-left conversion and had concerns about its size and dynamic capabilities (source).

glamorous offers a similar API to styled-components, uses glamor under the hood, has a footprint under 5kb gzipped, and is positioned for good performance (source). It supports hover states, child selectors, media queries, keyframes, theming with a ThemeProvider, nested themes, global styles through glamor, and server-side rendering (source).

It also merges glamor class names automatically and provides a jsxstyle-inspired API for unnamed styled elements such as Div and A (source). CSS Grid is supported via @supports, and the library is from PayPal (source).

- glamorous is a React component styling library with a styled-components-inspired API, a <5kb gzipped footprint, and performance via glamor.
- It was created after styled-components lacked RTL conversion, a hard requirement, and raised size/dynamic capability concerns.
- Features include hover states, child selectors, media queries, keyframes, ThemeProvider theming, nested themes, global styles, SSR, and automatic glamor class-name merging.
- It also exposes a jsxstyle-inspired unnamed component API (e.g. Div, A) and supports CSS Grid via @supports.