---
domain: ai-workflows
subdomain: cloud-cost-management
concept: default-hard-budget-caps
title: We're going to need default hard budget caps on pretty much everything
sources:
  - title: "We're going to need default hard budget caps on pretty much everything"
    url: "https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/"
    author: "Simon Willison"
    date: "2026-10-03"
  - title: "New AWS experience helps builders get started and ship faster"
    url: "https://aws.amazon.com/about-aws/whats-new/2026/09/New-AWS-Builder-Experience/"
    author: "AWS"
    date: "2026-09-16"
  - title: "Create a spend limit in AWS Settings"
    url: "https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html"
    author: "AWS"
  - title: "New early anomalies and spend caps on Google Cloud budgets"
    url: "https://cloud.google.com/blog/topics/cost-management/new-early-anomalies-and-spend-caps-on-google-cloud-budgets"
    author: "Google Cloud"
    date: "2026-07"
---

# We're going to need default hard budget caps on pretty much everything

Simon Willison argues that pay-by-usage services and APIs need a default feature that cuts off usage once a spending threshold is reached: "after $X/month, cut this thing off and return errors" (simonwillison.net). He stresses these must be **hard** limits — soft caps that merely send a warning email are insufficient, because nobody wants to wake up to a midnight budget warning and discover their rogue service consumed hundreds or thousands more dollars overnight.

The driver is coding agents and "personal agents (coding agents wrapped in a less threatening UI)", which greatly reduce the friction of spinning up code that can do useful things — sometimes expensive things, such as calls to paid APIs, hosted web applications, or systems that bill for additional storage and compute. Lowered friction means more uncapped, runaway services.

Willison anticipates the objection that businesses don't want their hosted applications throwing errors because a budget was exceeded, and counters that most businesses and individuals would prefer errors to a surprise $10,000+ bill. Hard caps should therefore be the default, with an opt-in escape hatch — a prominent checkbox reading: "Remove the budget cap. My application will not be shut down if I exceed the configured budget limit, and I will be responsible for subsequent charges."

He most wants this from AWS, citing people who refuse AWS for personal projects out of justified fear of bankruptcy and others who were seriously burned. AWS launched spend limits in its new builder experience on 16th September 2026 — a monthly spend limit that pauses a project for the month when reached — and Google Cloud launched "Spend Caps" in July, letting users "set a monthly financial cap on specific services within a project". Willison hopes agents will bias toward recommending providers with hard budget caps and warn inexperienced builders against uncapped services.

- Hard budget caps (cut off and return errors at $X/month) should be the default for pay-by-usage services; soft warning-only caps are insufficient.
- Coding agents and personal agents lower the friction of spinning up cost-incurring services, making runaway spend more likely.
- Errors from hitting a cap are preferable to a surprise bill of $10,000+; removing the cap should be an explicit, prominent opt-in.
- AWS launched a monthly spend limit that pauses projects when reached (16 Sept 2026), and Google Cloud launched Spend Caps in July.
- Agents should bias toward providers with hard budget caps and warn new builders away from uncapped services.