---
domain: web-dev
subdomain: javascript-runtimes
concept: runtime-acquisition
title: Deno is joining Cloudflare
sources:
  - title: "Deno is joining Cloudflare"
    url: "https://simonwillison.net/2026/Oct/9/deno-is-joining-cloudflare/"
    date: "2026-10-09"
---

# Deno is joining Cloudflare

Cloudflare is acquiring Deno outright, with the stated goal of building on `celld` to "make workerd self-hosting a first-class supported way to build and run apps using the Workers programming model" (Cloudflare blog). However, Cloudflare will only support the Deno runtime for another year with monthly bug-fix and security releases, after which it will end development of the runtime; Deno will remain open source and others are welcome to continue it.

Deno and Node.js creator Ryan Dahl agreed with the decision in a Hacker News comment, saying he no longer thinks Deno is where he can do the most important work. He argues Deno is well engineered with good ideas but "ultimately is not solving big problems," having been "sucked into the gravity well of node compatibility," which forces it to behave exactly as Node does. He questions the value of reimplementing Node given that it works, and says marginal performance, UX, or security benefits are not enough.

Dahl says he is now interested in building powerful new abstractions, citing `celld`, which depends only on object storage for coordination and persistence. He describes it as not just a slightly different API for the file system or network, but "an entirely new model for server development."

The author notes that his favorite Deno feature has long been its permissions system, which lets a script specify exactly which files and folders it can read and write and which network hosts it can access. Node.js has a similar permissions model, added in Node v20.0.0 (April 2023) and declared stable in Node v22.13.0 (January 2025), but it does not yet support allow-listing specific network hosts—networking is either on or off.

- Cloudflare is acquiring Deno, aiming to build on `celld` to make workerd self-hosting a first-class way to run Workers-model apps.
- Cloudflare will support the Deno runtime for one more year of monthly bug-fix and security releases, then end its development; Deno stays open source.
- Ryan Dahl agreed with the decision, saying Deno is well engineered but "not solving big problems" and was pulled into Node compatibility.
- Dahl is now focused on new abstractions like `celld`, which relies only on object storage for coordination and persistence.
- Deno's permissions system (file/folder and network-host allow-listing) remains a standout feature; Node's permissions model lacks per-host network allow-listing.