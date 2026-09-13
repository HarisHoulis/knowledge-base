---
domain: web-dev
subdomain: react-testing
concept: avoid-test-user
title: Avoid the Test User
sources:
  - title: "Avoid the Test User"
    url: "https://kentcdodds.com/blog/avoid-the-test-user"
    author: "Kent C. Dodds"
    date: "2019-05-24"
---

# Avoid the Test User

Kent C. Dodds argues that a UI component has only two real users: the end user interacting with it and the developer rendering it. Using a `<UserSettings />` example, he explains that these users define the component’s contract and are the only ones that matter when maintaining it. If a change affects the developer API or end-user experience, outside work may be required; internal refactorings that change neither do not require such updates (Kent C. Dodds, “Avoid the Test User”).

Dodds connects this to testing by repeating his principle that the more tests resemble how software is used, the more confidence they provide. Tests that assert implementation details introduce a third, unwanted “test user.” This test user does not pay the bills like the end user and does not affect the rest of the system like the developer user, so testing for them provides confidence in something nobody cares about (Kent C. Dodds, “Avoid the Test User”).

He concludes that writing tests with implementation details is all downside and no upside. Tests should focus on the developer user and the end user. When such tests break, that should signal that other changes may be needed elsewhere, rather than forcing maintainers to account for a test user. He also notes that mocking and testing implementation details can sometimes be necessary (Kent C. Dodds, “Avoid the Test User”).

- UI components have two real users: the end user interacting with the component and the developer rendering it.
- Testing implementation details creates a third “test user” that nobody actually cares about.
- Tests should resemble how software is used so they provide meaningful confidence.
- Writing tests with implementation details is described as all downside and no upside.
- When tests break, treat it as a cue to make needed changes for the real users, not the test user.