---
domain: web-dev
subdomain: developer-tooling
concept: app-devtools
title: Make Your Own DevTools
sources:
  - title: "Make your own DevTools"
    url: "https://kentcdodds.com/blog/make-your-own-dev-tools"
    author: "Kent C. Dodds"
    date: "2020-02-17"
---

# Make Your Own DevTools

The article describes building “App DevTools”: development tools that live inside the app repo and run in the app itself, rather than as a browser extension. The author found extensions indirect, limited, and hard to customize for temporary personal needs, so he created code that loads in the app and can control the app/environment [1]. A small React demo shows controlling a feature toggle, but the approach can do “just about anything” [1].

The setup uses a `loadDevTools` wrapper before app render. It enables DevTools by default in development, optionally in production via query string or localStorage, and disables explicitly when requested. The actual DevTools code is loaded through a dynamic `import()`, so it is not bundled with production app code; if not needed, the callback runs immediately. The app waits to render until DevTools install, allowing them to adjust the global environment first. The author emphasizes limiting user-experience impact because “users care about how you write code” [1].

A notable feature is “local” DevTools: a `dev-tools.local.js` file that is loaded if present but ignored via `.gitignore`, so individual developers can run personal scripts/automations without committing them or affecting others. The article suggests using this power to auto-fill forms, listen to URL changes, show model/validation state, or switch backend environments. It warns not to ship code that only works with DevTools enabled and to test with DevTools disabled. In production-enabled cases, App DevTools helped triage production issues and were useful to backend, QA, and product people [1].

- App DevTools are in-repo, in-app tools that replace or complement browser extensions and can control feature toggles, forms, backend environments, and more.
- `loadDevTools` checks query params/localStorage and `NODE_ENV`, dynamically imports DevTools so they stay out of the production bundle, and delays app render until installation completes.
- A `.local.js` convention lets individual developers run private DevTools code that is gitignored.
- The author warns to protect UX (bundle size/render time) and test with DevTools disabled to avoid shipping DevTools-dependent code.
- App DevTools proved useful beyond frontend devs, including backend, QA, and product, especially for production triage.