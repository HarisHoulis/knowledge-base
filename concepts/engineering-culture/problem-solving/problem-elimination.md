---
domain: engineering-culture
subdomain: problem-solving
concept: problem-elimination
title: Don't Solve Problems, Eliminate Them
sources:
  - title: "Don't Solve Problems, Eliminate Them"
    url: "https://kentcdodds.com/blog/don-t-solve-problems-eliminate-them"
    author: "Kent C. Dodds"
    date: "2021-05-11"
---

# Don't Solve Problems, Eliminate Them

Kent C. Dodds argues that humans are natural problem seekers, often inventing solutions to problems they don't yet have. For example, he recalls advising his sister against building a custom app when existing tools like Zoom, Tito, and Google Calendar already met her needs. Instead, the article recommends avoiding problems altogether by using off-the-shelf solutions until those tools prove insufficient, at which point actual experience gives you context to solve the real problem.

When a problem is unavoidable, the goal should be to eliminate it rather than solve it. Dodds explains that solving a problem leaves you captive to maintaining the solution, whereas eliminating the problem removes the need for ongoing upkeep. He cites Tesla's electric vehicles and gigacasting, which remove entire classes of mechanical issues and manufacturing steps. In software, React hooks eliminated the code-reuse complexity of HOCs and render props, and the official context API removed the need for Redux in many state-sharing cases.

Dodds also highlights Remix as a framework designed around problem elimination. Its nested routing handles shared layouts, loader functions prevent over-fetching, direct form support sidesteps client-side state management, and automatic loader re-calls solve cache invalidation. Trade-offs are inevitable, but the goal is to trade large, chronic problems for smaller, easier ones. The article urges readers to stop seeking problems, try to eliminate genuine ones, and only solve them if elimination is impossible.

- Don't solve problems you don't have yet; use existing solutions until they become a real bottleneck.
- When a genuine problem appears, first attempt to eliminate it; maintaining a solution is a hidden long-term cost.
- Tech history shows elimination in action: React hooks and context API replaced HOC/render-prop complexity and many Redux uses.
- Frameworks like Remix eliminate classes of web development issues (layout reuse, over-fetching, form handling, cache invalidation) by changing the approach.
- Trade-offs are unavoidable; aim to replace big problems with smaller ones instead of accumulating layered fixes.