---
domain: web-dev
subdomain: javascript-testing
concept: migrating-to-jest
title: Migrating to Jest
sources:
  - title: "Migrating to Jest"
    url: "https://kentcdodds.com/blog/migrating-to-jest"
    author: "Kent C. Dodds"
    date: "2016-11-14"
---

# Migrating to Jest

Kent C. Dodds describes migrating test suites from AVA and Mocha to Jest. He initially championed AVA, but as the testbase grew to hundreds of tests, performance became poor: his MacBook Pro fans spun up and the machine became unreliable during test runs. The slowdown led his team to skip githooks with `--no-verify`, which caused broken builds from simple issues like linting errors and failed tests. AVA's power-assert assertions also sometimes caused weird issues that took time to diagnose and fix.

After considering Mocha, a Twitter/GitHub discussion involving Dan Abramov, Trevor D. Miller, and Christoph Pojer convinced Dodds to try Jest again. He found it fast and easy to set up, and eventually swapped AVA for Jest in his open source module generator. For client-side migration, his coworker Jamund Ferguson did most of the work moving React tests from AVA; they used Kenneth Skovhus's jest-codemods and replaced proxyquire with Jest's built-in mocking. Old Mocha UI tests migrated relatively simply because Jest works with most Mocha globals.

The server-side migration of about 300 Mocha tests was an absolute nightmare. Problems stemmed from dependencies doing archaic things and some legitimate Jest bugs. Dodds tried five different approaches and ended up manually changing every test over about two weeks. Issues included polyfilling `JSON.parse`, `requireindex` not working, and errors thrown in bluebird promises with poor stack traces. He notes his experience was not typical.

Dodds says the client-side migration was absolutely worth it, and he thinks the server-side migration was worth it after his PR merged. He praises Jest for performance as test count grows, a powerful API with good defaults, easy code coverage, interactive watch mode, strong mocking, and snapshot assertions for React components, server responses, and redux state. Stats cited: UI tests went from 144ms per test before to 28ms per test after; server tests went from 111ms per test before to 116ms per test after. He expects the ms/test gap to widen with more tests because Jest runs tests in parallel.

- AVA performance degraded as the test suite grew, leading the team to use `git push --no-verify`, which caused broken builds and slowed the team.
- Client-side migration from AVA/Mocha to Jest was aided by jest-codemods and Jest's compatibility with Mocha globals; proxyquire was replaced by Jest mocking.
- Server-side migration of ~300 Mocha tests was unusually difficult, taking about two weeks, five approaches, and manual changes due to dependency issues and Jest bugs.
- Jest's features—code coverage, interactive watch mode, mocking, snapshots, and parallelization—made the migration worthwhile, though server-side value was still preliminary.
- Reported stats: UI tests improved from 144ms/test to 28ms/test; server tests were roughly flat at 111ms/test before and 116ms/test after.