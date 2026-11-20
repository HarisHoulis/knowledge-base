---
domain: engineering-culture
subdomain: testing-practices
concept: run-on-test-decomposition
title: Decompose Run-On Tests
sources:
  - title: "Decompose Run-On Tests"
    url: "https://newsletter.kentbeck.com/p/decompose-run-on-tests"
    author: "Kent Beck"
    date: "2026-10-13"
---

# Decompose Run-On Tests

Kent Beck describes the "run-on test"—a test that interleaves setup, operations, and assertions in a single long sequence—and argues it violates the "specific" property of the Test Desiderata: when a later assertion fails, you cannot tell whether the immediately preceding operation or an earlier one left the world in a wonky state, turning a failure into a debugging problem. He notes he writes such tests when exploring, since each new discovery naturally gets appended to the largest existing bit of testing, which explains the power-law distribution of test sizes.

His remedy is a mechanical decomposition. Copy the test and delete everything after the first assertion, giving it a long, explanatory name that tells a reader what could go wrong when it fails (e.g. `initializationProducesConsistentNamesAndExperiments` rather than `testInitialization`). Then copy again, keeping setup, the next operation, and the next assertion, deleting any setup that is now irrelevant, and repeat until the last assertion. Finally, delete the original test and optionally extract shared setup into a `setUp` function.

The resulting suite has the same coverage as the original run-on, but only if you commit to running the tests together and keeping them all working. Later tests lack the earlier assertions, which feels odd at first, but trusting the suite as a whole (the "composeable" property) lets you simplify tests. Coding in discovery mode is fine; leaving the relics of past ignorance around to trip colleagues is not.

- A run-on test chains setup, operations, and assertions, so a failure doesn't reveal which operation caused it.
- Run-ons arise naturally during exploratory coding, where each new insight is appended to the largest existing test.
- Decompose by copying the test once per assertion, trimming irrelevant setup and preceding operations at each stage.
- Give each short test a long, explanatory name describing what could go wrong, since the name is read in the context of a failure.
- The decomposed suite preserves coverage only if the tests are run and maintained together, which enables trusting and simplifying the suite.