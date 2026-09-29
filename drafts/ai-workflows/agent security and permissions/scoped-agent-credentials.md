---
domain: ai-workflows
subdomain: agent security and permissions
concept: scoped-agent-credentials
title: Make your agent safe and autonomous
sources:
  - title: "Make your agent safe and autonomous"
    url: "https://www.youtube.com/watch?v=_EJTrJFLa3g"
    author: "Kent C. Dodds"
    date: "2026-09-15T14:00:17+00:00"
---

# Make your agent safe and autonomous

The talk explains that AI agents often receive broad tokens capable of many actions, which can lead to unintended consequences such as sending an email without review or even dropping a production database. The core problem is over-scoping: the agent's credentials allow more than the user actually wants it to do (source: Kent C. Dodds, "Make your agent safe and autonomous").

Using Gmail as an example, the speaker notes that Gmail lacks a drafts-only scope, so an agent allowed to draft emails may also be able to send them. Some plugins add instructions like "do not send email," but those are not as reliable as deterministic enforcement. The proposed solution is to use Cody, which holds secrets, locks them to a particular package or repository, and prevents the agent from updating that code without explicit user permission (source: Kent C. Dodds, "Make your agent safe and autonomous").

By creating a package that only exposes safe operations—such as creating a draft but not sending an email—you can deterministically prevent unsafe actions. The speaker also notes that Cody centralizes integrations, so protections do not need to be reimplemented in every agent or code editor. This pattern can prevent severe mistakes like an overscoped token dropping a production database (source: Kent C. Dodds, "Make your agent safe and autonomous").

- Agents with broad, overscoped tokens can perform destructive or unwanted actions such as sending email or dropping a production database.
- Gmail does not offer a drafts-only scope, so allowing an agent to draft may also allow it to send.
- Cody can store secrets, bind them to specific packages or repositories, and require user permission before the agent can change that code.
- A package that exposes only safe operations (e.g., create draft) and blocks unsafe ones (e.g., send email) provides deterministic protection.
- Centralizing integrations in Cody avoids having to set up the same protections separately across multiple agents and code editors.