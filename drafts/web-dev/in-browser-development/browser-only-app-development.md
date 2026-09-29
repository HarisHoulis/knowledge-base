---
domain: web-dev
subdomain: in-browser-development
concept: browser-only-app-development
title: Building Production Apps 100% in the Browser
sources:
  - title: "Building Production Apps 100% in the browser"
    url: "https://kentcdodds.com/blog/building-production-apps-100-in-the-browser"
    author: "Kent C. Dodds"
    date: "2018-01-15"
---

# Building Production Apps 100% in the Browser

Kent C. Dodds describes building two production apps entirely in the browser without downloading source code. The first, Typing for Kids, was built solely in CodeSandbox using its GitHub integration and deployed via Netlify, with state kept in a top-level component and only three components total (kentcdodds.com). It depends only on react, react-dom, and animate.css, and uses create-react-app’s service worker plus a manifest.json to work offline and be installable like an app (kentcdodds.com).

The second app, Repeat Todo, was an authenticated version built for his wife using Firebase for authentication and storage. It also avoids react-router and redux, uses glamorous for styling components, and includes render-prop components for Firebase auth and data (kentcdodds.com). Because Firebase does not work well with arrays and order mattered, he stored items as an object and manually maintained order values (kentcdodds.com). Like Typing for Kids, it works offline via the service worker and can be an installable PWA on Android phones (kentcdodds.com).

The article argues that modern browser-based tools level the playing field: they are free, require no downloads, and make it possible to build production applications directly in the browser (kentcdodds.com). Dodds also recommends learning by building real, small solutions to problems faced by yourself or loved ones, rather than only consuming content (kentcdodds.com).

- Both apps were built 100% in the browser using CodeSandbox, GitHub integration, and Netlify, without ever downloading the source code locally.
- Typing for Kids is a 3-file app with state in the top-level component, no redux or react-router, and uses react, react-dom, and animate.css.
- Repeat Todo adds Firebase for auth/storage/offline support, uses glamorous and render props, and stores ordered data as an object because Firebase handles arrays poorly.
- Both apps leverage create-react-app’s service worker and manifest to work offline and be installable as PWAs.
- The author advocates building real, small projects to learn effectively rather than only consuming content.