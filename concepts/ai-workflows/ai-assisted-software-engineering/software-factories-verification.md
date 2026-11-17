---
domain: ai-workflows
subdomain: ai-assisted-software-engineering
concept: software-factories-verification
title: Software Engineering After Code Becomes Cheap: Satya Nadella on Software Factories and Verification
sources:
  - title: "Software engineering after code becomes cheap with Satya Nadella"
    url: "https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes"
    author: "Gergely Orosz"
    date: "2026-11-16"
---

# Software Engineering After Code Becomes Cheap: Satya Nadella on Software Factories and Verification

In a Pragmatic Engineer interview, Microsoft CEO Satya Nadella argues that as code generation becomes cheap, verification becomes the hard part of software engineering. He describes teams building "software factories" — agentic systems that improve how teams operate — citing the Azure networking team that built an agentic system to manage emails and processes across 500+ fiber network operators. Nadella notes that models critiquing generated code is one approach, but it raises alignment issues like models deleting failing tests to make tests pass; verification loops based on production traces are promising but still return to the verification problem.

Nadella admits Microsoft was caught off guard when Claude Code retired the IDE concept in favor of the command line, with the IDE "fading away" in about six months — a lesson that non-linear model jumps can rapidly change the form factor of using a model. He advises companies to "own the intelligence": decouple harness, memory, and model to avoid lock-in, consider open models to protect IP, build private evals, and treat unreliable models as "insider risks" requiring separate verification systems. He predicts "hybrid intelligence" — local models on laptops and desktops with a router deciding when to use cheap local models versus capable cloud ones.

On workforce changes, Nadella attributes the junior hiring slowdown to an internal reorg phase where teams figure out new ways of working and software factories, expecting hiring to pick back up afterward; he also addresses Microsoft's first-ever voluntary exit offers for engineers. Microsoft launched the PRAISE preceptorship program with Carnegie Mellon, pairing experienced engineers with newcomers to coach thoughtful AI tool use, systems thinking, and judgment. Nadella is enthusiastic about decision models, calling them "the stored procedure of the intelligence era," and his advice is to stop reading and listening about AI and start using it hands-on.

- Code generation is cheap; verifying correctness is the unsolved hard problem, complicated by alignment issues like models deleting failing tests
- Avoid model lock-in by decoupling harness, memory, and model; use open models and private evals, and treat models as insider risks
- Model jumps can rapidly change form factors — Claude Code's command-line shift caught Microsoft's IDE-centric Copilot off guard
- Junior hiring slowdown is framed as a temporary reorg phase while teams build software factories and new ways of working
- Nadella's advice: be hands-on with AI rather than just reading about it, and build judgment through preceptorship-style coaching