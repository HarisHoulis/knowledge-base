---
domain: web-dev
subdomain: frontend-tooling
concept: zero-config-tooling
title: Tools without config
sources:
  - title: "Tools without config 🛠📦"
    url: "https://kentcdodds.com/blog/tools-without-config"
    author: "Kent C. Dodds"
    date: "2017-09-26"
---

# Tools without config

Kent C. Dodds writes that teams repeatedly spend time setting up and maintaining tooling for testing, client-side bundling, and linting. In practice, developers get configs working and move on, so tooling becomes less than optimized and linters fall out of date (Kent C. Dodds, 2017). PayPal's project generator only bootstraps projects, leaving all config and update burden to users, which Dodds calls a Sisyphean task.

Inspired by create-react-app and its react-scripts package, Dodds created paypal-scripts. create-react-app offers a single tool dependency and no configuration via CLI scripts for build and test; paypal-scripts keeps great defaults but, unlike create-react-app, allows custom configuration because PayPal needed broader use cases (Kent C. Dodds, 2017). Rather than react-app-rewired's approach, paypal-scripts assumes built-in config unless the user provides config, such as a .babelrc or babel property in package.json, making behavior more predictable. It also exposes built-in config so users can compose custom config with it, e.g., using paypal-scripts/babel as a preset plus a custom plugin.

Dodds also created kcd-scripts for his open-source projects, encoding his preferences in a CLI and reducing config and dependencies across many npm packages. He recommends that anyone maintaining more than a handful of projects create and use a similar tool, and suggests forking kcd-scripts if desired (Kent C. Dodds, 2017).

- Tooling setup and maintenance is a recurring productivity drain, especially when configs are left unoptimized or outdated.
- create-react-app's react-scripts inspired paypal-scripts: a single tool dependency with strong defaults and CLI scripts.
- paypal-scripts allows custom configuration and exposes built-in config for composition, unlike create-react-app's no-config approach.
- kcd-scripts encodes Dodds's own project preferences and removes config/dependencies across many npm packages.
- Dodds recommends maintainers of multiple projects build or fork a custom scripts tool.