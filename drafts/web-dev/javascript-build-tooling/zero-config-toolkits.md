---
domain: web-dev
subdomain: javascript-build-tooling
concept: zero-config-toolkits
title: Concerning Toolkits: In Defense of Zero-Config Tools
sources:
  - title: "Concerning toolkits 🛠 📦"
    url: "https://kentcdodds.com/blog/concerning-toolkits"
    author: "Kent C. Dodds"
    date: "2018-01-29"
---

# Concerning Toolkits: In Defense of Zero-Config Tools

Kent C. Dodds argues for "toolkits" — defined, via Ronald Rey's awesome-toolkits, as "a set of tools in any form that allows you to create applications with no build configuration." Examples include react-scripts (what create-react-app leaves you with), parcel, preact-cli, ember-cli, and his own paypal-scripts/kcd-scripts. A toolkit is installed as a single dependency that normally ships a CLI for running project scripts; some focus narrowly on the build (parcel, preact-cli) while others cover testing, linting, releasing, and formatting. The goal is to cover as many use cases as possible without requiring configuration, while still permitting configuration when needed.

The core justification is maintenance cost. Dodds describes copy/pasting webpack configs across projects, then having to propagate every later improvement or tool update back to each one — a real pain once you have dozens of projects and multiple contributors. He cites a git diff replacing almost two dozen dependencies with one and deleting their configuration. His key claim: **"I can simply go to kcd-scripts, address any breaking changes, and push out a patch release with any version bumps to all underlying tools."** Most breaking changes in tools are config changes rather than source-code changes, so centralizing config pays off; when he switched bundlers from webpack to rollup, consumers needed no change at all. In team settings the duplication is concrete: at PayPal he found 635 webpack.config.js files, 897 .babelrc files, and 5,657 .eslintrc files internally, plus a support burden. Not every team can afford an expert in every tool, and consolidation lets people ship features instead of honing "webpack config jitsu."

He addresses two objections. First, "but use cases!" (Sean T. Larkin): toolkits either target *common* use cases rather than all of them — citing create-react-app's stated purpose of "the best experience for people getting started with React" — or remain configurable. React-scripts offers eject; other toolkits let you add config files (next.config.js, a jest property in package.json) or rewire (react-app-rewired). Paypal-scripts exposes its built-in config so you can require and tweak it without losing tool updates, and you can skip any script and use only the parts you want. Second, Rich Harris's discoverability objection: Dodds concedes the loss, but considers it a fine trade-off versus forcing configuration on the 80% who don't need it. Most devs using these tools don't know or care how they're configured — they just want to ship.

- Toolkits package many build/test/lint tools behind one dependency and CLI, defaulting to zero configuration while usually remaining configurable or ejectable.
- Centralizing config means one place to absorb breaking changes and version bumps — Dodds replaced nearly two dozen dependencies with one and later swapped webpack for rollup without consumers changing anything.
- Duplicated config is costly at scale: PayPal's internal GitHub had 635 webpack.config.js, 897 .babelrc, and 5,657 .eslintrc files, plus ongoing support load.
- Toolkits target common use cases, not all of them; escape hatches include ejecting (react-scripts), config files (next.config.js, jest.config.js), rewiring, or requiring the tool's exposed built-in config.
- Dodds accepts the discoverability trade-off raised by Rich Harris: forcing config on everyone to serve the 20% who need it would burden the 80% who don't.