---
domain: web-dev
subdomain: javascript-testing
concept: snapshot-testing
title: Effective Snapshot Testing
sources:
  - title: "Effective Snapshot Testing"
    url: "https://kentcdodds.com/blog/effective-snapshot-testing"
    author: "Kent C. Dodds"
    date: "2017-10-30"
---

# Effective Snapshot Testing

Kent C. Dodds responds to Justin Searls' criticisms of snapshot testing. Searls argues snapshots can become tests you don't understand, fail to encode developer intent, are generated files developers often do not scrutinize, and tend to produce high false negatives because they serialize integrated systems with side effects; when they fail, developers often just delete and re-record them instead of investigating (Kent C. Dodds, "Effective Snapshot Testing"). Dodds agrees these pitfalls are real and has experienced them personally, but clarifies that snapshot testing is simply an assertion, like `expect('foo').toBe('foo')`, and can be valuable when used effectively (Kent C. Dodds, "Effective Snapshot Testing").

Dodds says snapshots shine for error messages/logs in developer tools, for testing Babel plugins via `babel-plugin-tester` where asserting on ASTs would be prohibitively difficult, and for CSS-in-JS styling via `jest-glamor-react`. In these cases, snapshots can communicate intent through titles and before/after output, such as Babel plugin input/output separated by arrows, or rendered HTML with applicable CSS (Kent C. Dodds, "Effective Snapshot Testing").

The biggest thing to avoid is huge snapshots. Dodds says snapshots longer than a few dozen lines create major maintenance issues; he cites a 640-line snapshot that nobody reviewed and was only nuked and retaken on changes. He recommends smaller, focused snapshots or converting them to explicit assertions when possible, while noting huge snapshots are not entirely useless because unexpected changes can reveal broader impact than anticipated. He also mentions the `no-large-snapshots` ESLint rule for `eslint-plugin-jest` (Kent C. Dodds, "Effective Snapshot Testing").

To make snapshots more effective, Dodds recommends custom serializers, such as one that normalizes file paths to be project-relative and cross-platform, and `snapshot-diff`, which serializes only the difference between two states like a git diff. This reduces noise and false negatives when asserting on before/after React component states, and he points to Rogelio Guzman's talk "Jest Snapshots and Beyond" for more on custom serializers (Kent C. Dodds, "Effective Snapshot Testing").

- Snapshot testing is an assertion, not a replacement for expressing author intent; it can suffer from false negatives and nuke-and-rerecord habits.
- Use snapshots where they shine: error/log messages, Babel plugin output with `babel-plugin-tester`, and CSS-in-JS styles with `jest-glamor-react`.
- Avoid huge snapshots; keep snapshots small and focused, and prefer explicit assertions when possible.
- Custom serializers and `snapshot-diff` can make snapshots more meaningful by normalizing output and showing only the difference between states.