---
domain: web-dev
subdomain: code-organization
concept: colocation
title: Colocation
sources:
  - title: "Colocation"
    url: "https://kentcdodds.com/blog/colocation"
    author: "Kent C. Dodds"
    date: "2019-06-17"
---

# Colocation

Kent C. Dodds argues that code should be placed as close to where it is relevant as possible, a principle he calls colocation (Kent C. Dodds, "Colocation"). He illustrates this by comparing colocated code comments to a separate DOCUMENTATION.md or docs/ directory, which creates maintainability, applicability, and ease-of-use problems because docs get out of sync, are missed by people editing src/, and force context switching.

The same benefits apply to HTML/view templates, CSS, tests, state, and utility files. Modern frameworks like React and Vue put view logic and templates in the same file; CSS-in-JS colocates styles with components; unit tests should live with the file or group of files they test so maintainers see the module is tested and remember to update tests. Local state reduces re-rendering and is easier to maintain than distant state. Extracting a function into a shared utils/ directory can leave dead code and tests after the original component is deleted.

Exceptions can still follow the principle: a README.md can document a feature folder like authentication, integration tests can live in that folder, and end-to-end tests belong at the project root because they span beyond src/ and do not map to src/ files. Colocation also makes open-source extraction easier: a component folder can be copy/pasted and published to npm. Dodds recommends deleting ESLint rules like react/no-multi-comp and suggests re-evaluating separation of concerns.

- Place code as close to where it is relevant as possible; things that change together should be located as close as reasonable.
- Colocation improves maintainability, applicability, and ease of use by keeping comments, templates, CSS, tests, and state near related code.
- Separate docs/, test/, or utils/ directories risk stale knowledge, missed dependencies, dead code, and unnecessary cognitive load.
- Exceptions still follow the principle: feature READMEs and integration tests can live in feature folders, while E2E tests belong at the project root.
- Colocation eases open-source extraction and argues against rules like react/no-multi-comp.