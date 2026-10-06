---
domain: system-design
subdomain: database-scalability
concept: scaling-databases-ai-era
title: Move Fast and Don't Break Things: Scaling Databases for the AI Era
sources:
  - title: "Move Fast and Don't Break Things: Scaling Databases for the AI Era — PlanetScale"
    url: "https://www.youtube.com/watch?v=uKUA1a0Kdfc"
    author: "AI Engineer"
    date: "2026-10-06"
---

# Move Fast and Don't Break Things: Scaling Databases for the AI Era

In this AI Engineer conference talk, Ben from PlanetScale argues that the old "move fast and break things" ethos—born in early Facebook engineering culture—can be replaced by "move fast without breaking anything" (PlanetScale talk). The urgency has increased because AI agents now write, release, and deploy code, and because demand for AI agents has driven user growth of 2x, 10x, or 100x within six months to two years, leaving infrastructure unable to keep up (PlanetScale talk). The speaker stresses this is a hard problem, not a blame game: scaling to tens or hundreds of millions of users is genuinely difficult, but the goal is three, four, or even five nines of availability where databases, applications, and users are all up and happy (PlanetScale talk).

The talk draws on a PlanetScale database-philosophy article and is framed around three questions: how to build systems that don't constantly fail regardless of user count; how to scale those principles to an app serving millions; and how AI agents can be used to do or assist with that work, making processes more optimized and coordinated (PlanetScale talk). PlanetScale's context is supporting fast-scaling AI companies such as Cursor, so the speaker treats scaling seriously as a core company concern (PlanetScale talk).

Two principles are highlighted. The first is insulation: components must be isolated so a failure in one does not bring down the whole system. The data plane—where the databases and the critical user data live—should be separated from governance layers, oversight loops, analytics frameworks, applications, and MCPs. Those peripheral layers are updated more often and therefore fail more often, while a good database platform is unlikely to fail; the design goal is that a failed management-layer update does not stop users from reaching the database (PlanetScale talk).

The second principle is redundancy. The classic replicated-database diagram also applies to application infrastructure, though redundancy is usually easier for application servers because they are stateless workloads, where autoscaling tools such as Cloudflare Workers, Vercel functions, and AWS Lambda can help (PlanetScale talk).

- "Move fast and break things" came from early Facebook culture; the talk proposes achieving speed and reliability together as AI agents accelerate releases.
- Demand for AI agents is driving rapid user growth—2x, 10x or 100x—that infrastructure often cannot keep up with, with three to five nines of availability as the target.
- Insulation: isolate components so a failure in one layer (governance, oversight, analytics, MCPs, apps) does not take down the data plane or block users.
- Redundancy: replicate critical components; stateless application workloads are easier to autoscale (e.g. Cloudflare Workers, Vercel functions, AWS Lambda) than databases.
- The talk covers three questions: building systems that don't fail at any user count, scaling those principles to millions of users, and using AI agents to assist with the process.