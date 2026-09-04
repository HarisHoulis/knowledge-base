---
domain: web-dev
subdomain: react-remix
concept: remix-network-chasm
title: Remix: The Yang to React's Yin
sources:
  - title: "Remix: The Yang to React's Yin"
    url: "https://kentcdodds.com/blog/remix-the-yang-to-react-s-yin"
    author: "Kent C. Dodds"
    date: "2022-03-24"
---

# Remix: The Yang to React's Yin

This article argues that React, as a UI library, leaves a critical problem unsolved: managing the 'network chasm' between the client and server. Most React application state is actually a cache of server data, leading to complex caching logic and network waterfalls when data is fetched after component render. The author highlights how React Router's upcoming features—loaders and actions—begin to address this by decoupling data fetching from components and deriving data requirements from the URL, which helps avoid waterfalls and reduces cache-related bugs (Kent C. Dodds, 2022).

- React focuses on UI and local state, but web apps need a solution for the 'network chasm'—the gap requiring client-server data fetching and caching.
- Data fetching co-located in components causes waterfalls; fetching before render is necessary to optimize performance.
- React Router's loaders and actions shift data management closer to the URL, reducing client-side cache code and handling loading/error states, revalidation, and race conditions.
- Remix completes the bridge by moving data fetching and mutation code entirely to the server, enabling server rendering and reducing JavaScript bundle size.
- Remix allows server-side code to access databases and private APIs directly, simplifying the developer experience while keeping apps fast and resilient.