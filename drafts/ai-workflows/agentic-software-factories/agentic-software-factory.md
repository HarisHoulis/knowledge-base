---
domain: ai-workflows
subdomain: agentic-software-factories
concept: agentic-software-factory
title: Inside OpenAI's agentic software factory
sources:
  - title: "Inside OpenAI's agentic software factory"
    url: "https://newsletter.pragmaticengineer.com/p/openai-software-factory"
    author: "Gergely Orosz"
    date: "2026-09-15"
---

# Inside OpenAI's agentic software factory

Based on a visit and interviews with seven OpenAI engineering leaders, Codex has gone from a nice-to-have tool to the backbone of nearly everything at the company since around January. Non-engineering orgs — finance, recruitment, legal — went from roughly 0% to 90% Codex usage in a four-month period, and almost all employees now use Codex and ChatGPT Work weekly, without any mandate from above (Orosz, Pragmatic Engineer, 2026). Adoption was driven partly by the /goal setting for long-running agent tasks, which pushed usage from 60% to 90% between April and May, and partly by an "awareness overhang": many uses are discovered by word-of-mouth from teammates (Akshay Nathan, quoted by Orosz, 2026). Role-specific plugins let teams adapt the agent to their work, since "you can't just give everyone an empty box" (Andrew Ambrosino), and domain experts are now embedded in engineering teams to supply taste the models lack in areas like slide decks, spreadsheets and reports (Orosz, 2026).

The article reports that IDE usage has declined since January, validating OpenAI's bet not to fork VS Code for the Codex app, which was seen as a possible "misfit" between terminal (CLI) and feature-rich IDE (Ambrosino, quoted by Orosz, 2026). Agent-driven output is straining developer infrastructure: PRs per engineer are growing "like a hockey stick," with roughly 10x load increases on some systems in about six months — growth that takes most companies two or three years (Venkat Venkataramani, quoted by Orosz, 2026). Every month brings a new set of scaling bottlenecks as model capabilities unlock. In response, OpenAI is rethinking core primitives: agentic code reviews that examine changes through multiple lenses (e.g. cloud infrastructure and security), and agents that handhold a change to production while watching monitoring graphs or building their own dashboards (Venkataramani, quoted by Orosz, 2026).

Native mobile deployment is described as an increasingly painful bottleneck, because every iOS and Android update must pass Apple's and Google's manual review processes, which take hours or days. Sulman Choudhry compares this to Facebook's 2010s push from monthly to weekly releases, and argues the goal should be shipping native mobile as fast as the web, something OpenAI is "nowhere close" to (Choudhry, quoted by Orosz, 2026).

The article frames OpenAI's setup as a "software factory" — AI agents and humans producing software together, analogous to a physical factory — built around Codex with several automated, agentic feedback loops, such as a Perf Factory that monitors production and kicks off Codex agents to automatically fix performance issues (Orosz, 2026). The reported consequences for the profession: engineering specializations are disappearing, judgment and agency matter more, and previously "impossible" rewrites and migrations now take only one or two engineers (Orosz, 2026). OpenAI's dependence is such that during even a minor outage, internal messages reach the Codex and Work teams at the same time as, or before, automated alerts (Orosz, 2026).

- Codex and ChatGPT Work spread from engineering to all OpenAI orgs without a mandate: non-engineering teams went from ~0% to 90% usage in four months, and almost all employees use them weekly.
- Long-running agent threads and the /goal setting drove the biggest usage jump (60% to 90% between April and May); long threads reduce human parallel work because agents spawn sub-agents themselves.
- Agent-driven throughput is breaking dev infrastructure: PRs per engineer are growing hockey-stick style, with ~10x load increases on some systems in ~6 months, forcing a rethink of PRs, code review, and CI/CD.
- Native mobile release approval by Apple and Google is a sharp bottleneck — code generation is fast, but getting code onto phones still takes hours or days, and OpenAI is "nowhere close" to web-speed shipping.
- The engineering job is shifting: specializations are fading, judgment and agency matter more, and one or two engineers can now accomplish rewrites and migrations previously considered impossible.