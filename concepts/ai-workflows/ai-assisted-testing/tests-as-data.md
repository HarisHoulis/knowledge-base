---
domain: ai-workflows
subdomain: ai-assisted-testing
concept: tests-as-data
title: Tests as Data: Ensuring AI-Generated Code Does What We Want
sources:
  - title: "Tests as data: ensuring AI-generated code does what we want"
    url: "https://martinfowler.com/articles/tests-as-data.html"
    author: "Martin Fowler"
---

# Tests as Data: Ensuring AI-Generated Code Does What We Want

Martin Fowler summarizes Matteo Vaccari's argument that automated testing becomes problematic when AI agents write both production and test code, since developers risk losing assurance that tests actually protect against functional errors. Vaccari makes three claims: when AI writes the code, developers become its customers; therefore customer tests, not developer tests, become the primary contract between humans and AI; and moving that contract into test data rather than test code makes it easier to protect from unexpected modifications by coding agents.

The approach optimizes for human-readable tests that establish a contract between humans and AI. Historically, DSL parsers and custom test runners were expensive to write and maintain, but AI now makes building them cheap, lowering the barrier to expressing tests as data.

- AI writing both production and test code undermines confidence that tests catch functional errors
- When AI writes the code, developers become customers, so customer tests become the primary human-AI contract
- Expressing tests as data rather than code protects the contract from agent modifications
- AI makes custom DSL parsers and test runners cheap, enabling human-readable test data