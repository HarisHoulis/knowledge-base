---
domain: engineering-culture
subdomain: software-correctness
concept: software-correctness-and-supply-chain-security
title: Software Correctness & Supply Chain Security, with Sean Allen
sources:
  - title: "Software correctness & supply chain security, with Sean Allen"
    url: "https://newsletter.pragmaticengineer.com/p/software-correctness"
    author: "Gergely Orosz"
    date: "2026-11-10"
---

# Software Correctness & Supply Chain Security, with Sean Allen

In this interview, Sean Allen (distinguished engineer at Antithesis and Pony core contributor) defines software correctness as whether a program does what is expected, framed in terms of invariants — guarantees the software upholds. He notes that teams often don't know upfront what they expect their software to do, and offers a pragmatic definition: correct software serves its business purpose and doesn't wake anyone up at 2 a.m. with an outage (the same definition he uses for 'beautiful code').

Allen contrasts language families: the ALGOL family (Python, Perl, Ruby, C, C++) versus the ML family (Standard ML, OCaml, F#, and Rust as the most famous ML-influenced language). ML-style sum types combined with exhaustive pattern matching turn 'forgot to handle the new case' bugs into compilation errors. Despite caring deeply about correctness, Allen is anti-testing in the traditional sense: he argues manual testing is the worst way to ensure correctness, and that you should do as much as possible before testing — ideally making illegal states unrepresentable in the type system. He does love TDD as a mechanism for designing great APIs, and describes how his literal 'hard-code the answer' approach to TDD katas pushes people toward property-based testing once inputs are randomized.

For distributed systems and databases, Allen advocates 'workloads' — a combination of inputs that drive the code and validation of expected behavior — rather than simple property-based examples. He cites the Bank Test for stress-testing ACID isolation guarantees, and warns that naive random operation selection tends to stay near where it started, like a drunk walk, rarely triggering interesting paths such as disk swapping, garbage collection, or resharding. On quality, he pushes back on treating quality as late CI/CD 'gates', preferring validation techniques built in from the start. He also argues tech debt only hurts if you have to pay it back (often disregarded during rewrites), that there's no simple fix for supply chain security because robust languages like 'E' are unpopular while popular languages assume a trustworthy ecosystem, and that garbage collection hurts performance but doesn't have to — as shown by his predictably performant approach in Pony. His closing advice: go slow to go fast by investing in upfront design and alignment.

- Correctness is about invariants — software doing what's expected — and 'correct enough' means serving its business purpose without 2 a.m. outages.
- ML-family languages (OCaml, F#, Rust) with sum types and exhaustive matching turn unhandled cases into compile errors, catching bugs before testing.
- Manual testing is the worst way to ensure correctness; prefer making illegal states unrepresentable, and use workloads (inputs + validation) like the Bank Test for distributed systems.
- Quality shouldn't be a late CI/CD gate; build validation and feedback into development from the start.
- Supply chain attacks have no simple fix: robust languages like 'E' are unpopular, while popular languages assume a trustworthy ecosystem.