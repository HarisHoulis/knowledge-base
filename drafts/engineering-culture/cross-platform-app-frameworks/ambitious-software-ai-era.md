---
domain: engineering-culture
subdomain: cross-platform-app-frameworks
concept: ambitious-software-ai-era
title: Building Ambitious Software — Dioxus in the Age of AI
sources:
  - title: "Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition"
    url: "https://www.youtube.com/watch?v=H7vFrcNWXzs"
    author: "Jonathan Kelley"
    date: "2026-09-11"
---

# Building Ambitious Software — Dioxus in the Age of AI

Jonathan Kelley opened the first commit to Dioxus five years ago, spending his last summer as an undergraduate on a cross-platform app framework written in Rust rather than taking an internship or doing AI research (Kelley, "Building ambitious software"). In 2021 Rust was still niche but growing, and its pitch of native performance, a solid type system, and simple cross-compilation sold him. The idea was straightforward: write all apps in Rust using HTML and CSS as markup, borrowing React-style reactivity, so developers could reuse web components and tooling — with no VM, no IPC, and no JavaScript, unlike React Native (which he calls janky) or Flutter (too slow).

Challenging React Native and Flutter proved extremely ambitious: there were few off-the-shelf components, so reactivity, font rendering, hot reloading, and application bundling all had to be built from scratch. Tasks like building a web browser were just necessary steps along the way (Kelley). Today Dioxus supports cross-platform support, native rendering, Rust hot reload, and bundle splitting, letting users ship a full-stack web app from the same codebase as their iOS and Android apps. The project has nearly 37,000 GitHub stars, millions of downloads, and an estimated 200 million cumulative end users, with apps ranging from AI assistance to voting software, data science tools, and a satellite collision-avoidance system.

Two of the most ambitious sub-projects are Blitz and Subsecond (Kelley). Blitz is a lightweight but fully featured HTML/CSS rendering engine: the browser-grade CSS engine extracted from Firefox, a custom HTML DOM, and a hybrid GPU rendering pipeline. Compared to RAM- and storage-heavy Electron apps, Blitz apps ship in under 5 MB bundles and use under 50 MB of RAM at runtime. Subsecond is a generic hot reload engine for Rust, C, and C++ that watches for edits, recompiles only what changed, and patches the running app in place in about 100 milliseconds — described as the only hot reload engine for native compiled code with such wide language and runtime support, working on every major system and compiling to WebAssembly.

Kelley notes that every line of code in Dioxus was painstakingly written by hand until very recently, maintained by a tiny team reviewing code themselves on a frequent but ambitious release cadence (Kelley). The shift: over the past six months, AI coding agents got really, really good — specifically at Rust.

- Dioxus began as a 2021 undergrad summer project: a Rust cross-platform app framework using HTML/CSS for markup and React-inspired reactivity, avoiding VMs, IPC, and JavaScript.
- Because almost no off-the-shelf components existed, the team had to build reactivity, font rendering, hot reloading, and bundling from scratch, treating even a web browser as a necessary step.
- Dioxus now claims ~37,000 GitHub stars, millions of downloads, and ~200M cumulative end users, with cross-platform, native rendering, hot reload, and bundle splitting.
- Blitz is a lightweight HTML/CSS engine (Firefox-derived CSS engine, custom DOM, GPU pipeline) yielding <5 MB bundles and <50 MB RAM versus Electron; Subsecond hot-patches Rust/C/C++ in ~100 ms.
- All Dioxus code was written by hand until recently, when AI coding agents — particularly strong at Rust — changed the team's workflow.