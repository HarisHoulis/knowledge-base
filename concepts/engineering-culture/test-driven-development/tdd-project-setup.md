---
domain: engineering-culture
subdomain: test-driven-development
concept: tdd-project-setup
title: Kotlin TDD - New Project and First Stories
sources:
  - title: "Kotlin TDD - New Project and First Stories"
    url: "https://www.youtube.com/watch?v=iTv2iJ4twjU"
    author: "Pairing with Duncan"
    date: "2021-11-03T13:25:18+00:00"
---

# Kotlin TDD - New Project and First Stories

The video demonstrates starting a new project using Test-Driven Development (TDD) and Extreme Programming (XP) practices. The author, Duncan, begins by negotiating user stories with a fictional customer for a Gilded Rose-like inventory system. The initial stories focus on adding items to stock and printing a list of items with name, sell-by date, and quality. Duncan emphasizes implementing the minimum amount of code for each story and using a practice called 'sit on your cards' to avoid looking ahead unnecessarily. He sets up a simple in-memory solution with tests as the store of state, and begins by creating a walking skeleton test to verify the test infrastructure works, then proceeds to create an Item class and a Stock class based on the first story. The approach highlights TDD's red-green-refactor cycle, writing production code only when tests fail.

- Use user stories to drive development in small increments, focusing on the current story only.
- Follow strict TDD: write a failing test before production code, then refactor.
- Start with a walking skeleton test to establish the test environment works.
- Defer concerns like persistence; use in-memory structures like lists for initial implementation.
- Apply the XP practice of 'sit on your cards' to avoid implementing future features prematurely.