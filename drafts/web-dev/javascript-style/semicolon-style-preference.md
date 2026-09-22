---
domain: web-dev
subdomain: javascript-style
concept: semicolon-style-preference
title: Semicolons in JavaScript: A preference
sources:
  - title: "Semicolons in JavaScript: A preference"
    url: "https://kentcdodds.com/blog/semicolons-in-javascript-a-preference"
    author: "Kent C. Dodds"
    date: "2015-11-16"
---

# Semicolons in JavaScript: A preference

The article argues that omitting semicolons in JavaScript source is safe only when tooling handles the risks. It explains Automatic Semicolon Insertion (ASI) makes the debate possible, but says you should not rely on ASI. If you compile with Babel or minify with terser, semicolons are added back in the shipped code, and the problems with relying on ASI go away. You also need ESLint with the `no-unexpected-multiline` rule enabled, and your build pipeline should fail if that rule is broken.

Once compilation/uglification and linting are in place, the semicolon question becomes a matter of preference. The author prefers omitting semicolons because they dislike a linter or editor telling them to add something unnecessary, and they find the code looks cleaner. An update notes that after adopting Prettier, it is really about what you like to look at, and the author uses `eslint-config-prettier` to let Prettier manage it.

The article also addresses the argument that semicolons help newcomers. The author says that has not been their experience and that their code has not become less clear, maintainable, or readable without semicolons. The conclusion is conditional: if you do not compile/uglify and lint properly, do not omit semicolons because it is not a preference then; if you do have those safeguards, you can choose based on preference.

- Relying on ASI is a bad idea; omit semicolons only if compilation/minification adds them back for production.
- Enable ESLint's `no-unexpected-multiline` rule and make the build fail when it is broken.
- With proper compilation/uglification and linting, semicolon use becomes a preference rather than a correctness issue.
- The author prefers no semicolons; with Prettier, it becomes an aesthetic choice managed by tooling.
- Without proper tooling, the author does not recommend omitting semicolons.