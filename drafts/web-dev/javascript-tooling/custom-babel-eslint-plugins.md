---
domain: web-dev
subdomain: javascript-tooling
concept: custom-babel-eslint-plugins
title: Writing Custom Babel & ESLint Plugins to Improve DX and UX
sources:
  - title: "How writing custom Babel & ESLint plugins can increase productivity & improve user experience"
    url: "https://kentcdodds.com/blog/how-writing-custom-babel-and-eslint-plugins-can-increase-productivity-and-improve-user-experience"
    author: "Kent C. Dodds"
    date: "2017-07-17"
---

# Writing Custom Babel & ESLint Plugins to Improve DX and UX

Building applications gets harder as teams and codebases grow, and tools like ESLint and Babel help manage that growth by preventing bugs and migrating code so developers can focus on domain problems (source). Although both have large plugin communities, the problems a team faces are often unique, so custom plugins are frequently needed; custom ESLint plugins can statically prevent a bug without running code and, once added, prevent it everywhere, unlike tests (source). Examples from PayPal include enforcing a localization library, React controlled component behavior, button type attributes, analytics data attributes, and import boundaries across apps (source).

Custom Babel plugins allow code manipulation either at build time or as one-time codemods, which the author argues are far more powerful than regex find/replace (source). Examples include react-loadable and babel-plugin-import-inspector for code-splitting, babel-plugin-lodash for automatic cherry-picking of Lodash methods, and a custom plugin for glamorous.rocks that loaded locale-specific strings based on a LOCALE environment variable (source). Major-release codemods from React and Webpack can also be written as Babel plugins and run with babel-codemod (source).

Babel and ESLint both operate on an Abstract Syntax Tree (AST), which is how the computer sees code; Babel's babylon parser turns code strings into an AST (a JavaScript object), then Babel plugins transform it while ESLint plugins inspect it for patterns to discourage (source). The author notes he does not have a computer science degree and learned about ASTs just a year earlier, and says working with ASTs helped him understand JavaScript better (source). He encourages developers to try it and points to his Frontend Masters course and free resources (source).

- Custom ESLint plugins statically prevent recurring bugs across the entire codebase, not just in one area (source).
- Custom Babel plugins enable build-time optimizations, codemods, and reducing tedious APIs, often outperforming regex-based changes (source).
- Both Babel and ESLint work by parsing code into an AST, then transforming or inspecting that tree (source).
- Examples include PayPal's custom ESLint rules, babel-plugin-lodash, react-loadable's import inspector, and a localization Babel plugin for glamorous.rocks (source).
- Learning resources mentioned include a Frontend Masters course, babel-plugin-handbook, asts-workshop, and egghead.io AST lessons (source).