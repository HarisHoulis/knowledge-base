---
domain: web-dev
subdomain: javascript-modules
concept: module-usability
title: Improving the Usability of Your Modules
sources:
  - title: "Improving the usability of your modules"
    url: "https://kentcdodds.com/blog/improving-the-usability-of-your-modules"
    author: "Kent C. Dodds"
    date: "2017-11-06"
---

# Improving the Usability of Your Modules

The article describes improvements made to `react-i18n`, an internationalization module that automatically loads server-rendered content from the DOM. The original module performed side-effects at the root level on import, parsing `#react-messages` immediately. This forced users to manage import timing, caused cryptic errors in application and test environments, and made initialization hard to customize (kentcdodds.com). The author refactored those side-effects into an exported `init` function, so consumers explicitly control when initialization happens. This also made it possible to provide better error messages if the module is used before initialization (kentcdodds.com).

The second improvement was making the module more generic. Originally it assumed the localization JSON root key was a file name and the rest was nested file content. After refactoring, `getContent` no longer cared about that structure; it only expects a nested JavaScript object and supports calls like `getContent('pages/home.header.title')` or `getContent('pages/home')('header.title')`. The author calls this “sota-curried” because it resembles currying without being true currying (kentcdodds.com). This made the module more useful to other teams and actually simplified the implementation (kentcdodds.com).

The author cautions that generalizing a library requires balancing usability with YAGNI. The extra effort was justified because the module was being inner-sourced and needed to support varied use cases, but premature optimization in features or complexity should be avoided (kentcdodds.com).

- Avoid side-effects when a module is imported; export functions such as `init` that perform side-effects when the user chooses.
- Import-time side-effects make apps and tests fragile and can produce cryptic errors when the environment is not ready.
- Make modules generic when it does not add too much complexity; avoid assuming one application’s data shape.
- Refactoring `react-i18n` to a generic `getContent` API decoupled it from `react-content-loader` and simplified the implementation.
- Balance generic design with YAGNI and beware premature optimization in features and complexity, not just performance.