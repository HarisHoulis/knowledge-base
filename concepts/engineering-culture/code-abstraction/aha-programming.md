---
domain: engineering-culture
subdomain: code-abstraction
concept: aha-programming
title: AHA Programming
sources:
  - title: "AHA Programming"
    url: "https://kentcdodds.com/blog/aha-programming"
    date: "2020-06-22"
---

# AHA Programming

This article critiques dogmatic adherence to DRY (Don't Repeat Yourself) and WET (Write Everything Twice), proposing instead AHA (Avoid Hasty Abstractions). The author shares a personal experience where a bug required fixes in eight places due to heavy code duplication, illustrating the pain of duplication. Conversely, they encountered over-abstraction in an AngularJS codebase where pseudo-inheritance was so confusing that they wished the code had been duplicated instead. This establishes the core tension between premature abstraction and duplication.

- DRY can lead to harmful over-abstraction when applied rigidly; 'prefer duplication over the wrong abstraction' (Sandi Metz).
- WET (Write Everything Twice) is also dogmatic, but allows duplication up to three times before abstracting.
- AHA stands for Avoid Hasty Abstractions: write abstractions when they feel right, after seeing duplicate code in multiple places where commonalities are clear.
- Optimize for change first: because future requirements are unknown, premature abstractions often become wrong and harder to refactor than simple duplication.
- Use tools like jsinspect to find duplication opportunities, but don't abstract until confident about the use cases.