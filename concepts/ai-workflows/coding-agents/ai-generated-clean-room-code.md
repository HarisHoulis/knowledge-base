---
domain: ai-workflows
subdomain: coding-agents
concept: ai-generated-clean-room-code
title: Paint.NET uses Claude to rewrite Direct2D for WINE
sources:
  - title: "Quoting Rick Brewster"
    url: "https://simonwillison.net/2026/Sep/2/rick-brewster/"
    author: "Simon Willison"
    date: "2026-09-02"
---

# Paint.NET uses Claude to rewrite Direct2D for WINE

Rick Brewster, author of Paint.NET, describes how the project now ships an internal, clean-room reverse-engineered rewrite of Direct2D specifically for WINE, triggered by the /wine flag. This 180,000-line codebase was generated largely by Claude, an AI coding assistant, because Direct2D was the biggest hurdle for Paint.NET on WINE and could not simply be disabled. Brewster credits Claude for making the effort possible, noting it would otherwise never have happened (Simon Willison, 2026).

The code is described as 'vibe coded,' meaning it has not been thoroughly reviewed and is more 'trust me bro' style. Brewster explains that reviewing 180,000 lines is impractical given the rest of Paint.NET is ~700,000 lines accumulated over 20 years. While Claude sometimes worked with exceptional speed and cleverness—including reverse-engineering Direct2D's effect formulas—it also required significant babysitting, especially around COM reference counting (initially missing AddRef) and certain design/architecture decisions (Simon Willison, 2026).

- Direct2D was the major blocker for Paint.NET on WINE, and disabling it was not an option.
- Claude generated a from-scratch 180,000-line clean-room Direct2D implementation for WINE, shipped in PaintDotNet.Windows.Direct2D1.Managed.dll.
- The code is 'vibe coded' and not thoroughly reviewed, highlighting the trust gap in large AI-generated codebases.
- AI assistance required manual correction for COM resource management and architectural missteps, yet succeeded at complex reverse-engineering tasks.