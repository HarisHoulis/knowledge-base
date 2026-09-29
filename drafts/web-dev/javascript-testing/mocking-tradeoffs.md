---
domain: web-dev
subdomain: javascript-testing
concept: mocking-tradeoffs
title: The Merits of Mocking
sources:
  - title: "The Merits of Mocking"
    url: "https://kentcdodds.com/blog/the-merits-of-mocking"
    author: "Kent C. Dodds"
    date: "2018-11-05"
---

# The Merits of Mocking

Mocking lets you fake dependencies so you can test otherwise impractical flows. Kent C. Dodds gives the example that testing a checkout process without mocking could cost a lot in credit card fees, so a fake charging service is used instead (Kent C. Dodds, 2018). But mocking has a cost: it severs the real-world connection between the code under test and the mocked dependency, so passing with a fake does not guarantee production success with the real version (Kent C. Dodds, 2018). Mocking is therefore a trade-off, usually trading confidence for practicality (Kent C. Dodds, 2018).

For UI unit and integration tests, Dodds has a rule: never make actual network calls; instead mock the module responsible for network calls. He also mocks animation libraries to avoid waiting for animations before elements are removed from the page. Otherwise, most UI tests use real production code. For E2E tests, he avoids mocking anything, except for backend services that should hit fake or test services rather than real credit card services (Kent C. Dodds, 2018).

Saving a few milliseconds per test is not a good reason to mock. Shallow rendering and extreme component mocking are faster, but only by milliseconds; if rendering the full component tree is slow, that points to a real performance bug worth addressing. Trading confidence for a minute or two faster test suite is a bad trade. When mocking is needed, Jest provides strong utilities; Dodds demonstrates simulating Jest's inline mock functionality in pure Node using require.cache to replace a module export with a mock function (Kent C. Dodds, 2018).

- Mocking enables testing of otherwise impractical or costly flows, such as credit card charging, by faking dependencies.
- Mocking severs the real-world connection to the mocked dependency, so it trades confidence for practicality.
- In UI unit/integration tests, mock network calls and animation libraries but otherwise use real production code; in E2E tests, avoid mocking except fake/test backend services.
- Do not mock just to save milliseconds; slow full renders indicate a performance bug, and trading confidence for a faster suite is a bad trade.
- When mocking is warranted, Jest's utilities help, and inline mock behavior can be simulated in raw Node by replacing module exports via require.cache.