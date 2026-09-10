---
domain: engineering-culture
subdomain: code-quality-and-maintainability
concept: optimize-for-change
title: Why users care about how you write code
sources:
  - title: "Why users care about how you write code"
    url: "https://kentcdodds.com/blog/why-users-care-about-how-you-write-code"
    author: "Kent C. Dodds"
    date: "2019-12-23"
  - title: "I hate almost all software"
    url: "http://tinyclouds.org/rant.html"
    author: "Ryan Dahl"
    date: "2011-10"
---

# Why users care about how you write code

Kent C. Dodds agrees with Ryan Dahl's 2011 assertion that "the only thing that matters in software is the experience of the user," but argues its implications are broader than Dahl suggested: user experience is indirectly yet strongly coupled to how software is built. He illustrates this with a past job where he was asked to add a single checkbox and label to a popover; because the logic lived in a 1,000-line Backbone view extending a 2,000-line view, with leaky abstractions and no tests, a task he estimated at a week took nearly three weeks and introduced a frightening number of bugs. Had the component been built with SOLID principles (DRY, SRP, etc.), he estimates the feature could have taken a day or less.

Dodds argues that users do not care about the latest JS framework, build tool, const vs. let, semicolons, tabs, git merging strategy, or deployment service — but they do care when poor code means waiting weeks instead of days for a feature. Our measure of success should be how well we deliver what the user wants, and no more; tool choices should be based on that fundamental goal. Latest tech and good UX are not mutually exclusive, and the latest technology can be a great way to accomplish that goal.

The practical argument is that developers waste time debating minutiae with little impact — semicolons (no), indentation width (two spaces) — while the choices that make a significant impact are solid design patterns, linting (only good rules), testing, continuous integration, delivery, and deployment. These are the basis for an app that delivers a quality user experience, and since requirements change and a great app is never truly finished, the guiding principle is: **optimize for change.**

The takeaway is to be intentional about what you argue about: behind every firm opinion, ensure it is founded on what's best for the people using your software, and if that connection is tenuous, it may not be worth arguing about. Dodds closes with concrete tooling advice to delete eslint-config-react and eslint-config-airbnb in favor of eslint-config-react-app, and to use Prettier.

- User experience is indirectly but strongly coupled to how code is written, built, and deployed — unmaintainable code causes real user-visible delays (a one-week feature took three weeks).
- The decision rule: our measure of success should be how well we deliver what the user wants, and tool choices should be based on that goal rather than endless debate over minutiae like semicolons and tabs.
- Focus energy on choices that matter: solid design patterns (SOLID/DRY/SRP), linting, testing, continuous integration, delivery, and deployment.
- Optimize for change — requirements change, so how you build determines how quickly and easily you can ship new features while keeping the product polished.
- Be intentional about what you argue about: ensure each opinion is founded on what's best for users of the software; tenuous connections aren't worth arguing over.