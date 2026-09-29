---
domain: web-dev
subdomain: react-performance
concept: slow-renders-before-re-renders
title: Fix the Slow Render Before You Fix the Re-render
sources:
  - title: "Fix the slow render before you fix the re-render"
    url: "https://kentcdodds.com/blog/fix-the-slow-render-before-you-fix-the-re-render"
    author: "Kent C. Dodds"
    date: "2019-09-09"
---

# Fix the Slow Render Before You Fix the Re-render

The article distinguishes React's render phase (calling components to create React elements), reconciliation (comparing new elements with previous ones), and commit (applying DOM updates). It notes that a re-render does not necessarily cause a DOM update, so an "unnecessary re-render" can occur without changing the DOM (source).

React batches DOM updates to avoid repeated slow layout work, and while the commit phase can be slow, much of the render/reconciliation work is fast even on low-end mobile devices (source). The article argues that when an app feels janky, the likely problem is a slow render—code doing expensive work during the render phase—rather than unnecessary re-renders (source).

If you reduce re-renders while leaving a slow render in place, you may end up with a worse experience and more complicated code (source). The recommended approach is to profile the interaction with browser profiling tools and React DevTools, identify the slowest parts, fix those slow renders first, then re-evaluate whether unnecessary re-renders still matter (source).

- React's update pipeline is render → reconciliation → commit; only the commit phase updates the DOM.
- A re-render does not imply a DOM update, so "unnecessary re-renders" are often not the real bottleneck.
- Slow render-phase work is more likely to cause jank; fix that before optimizing re-renders.
- Reducing re-renders while slow renders remain can worsen UX and increase code complexity.
- Use browser profilers and React DevTools profiler to locate slow renders, then verify fixes.