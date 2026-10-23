---
domain: ai-workflows
subdomain: agent-authentication
concept: agent-signup-protocol
title: Letting AI Agents Sign Up for Your App Safely
sources:
  - title: "How to Let AI Agents Sign Up for Your App Safely — Isabelle Williams, WorkOS"
    url: "https://www.youtube.com/watch?v=uTrY8slys0w"
    author: "AI Engineer"
    date: "2026-10-23"
---

# Letting AI Agents Sign Up for Your App Safely

Isabelle Williams (WorkOS) argues that the next user of many applications will be an AI agent, not a human, and that product teams need to design onboarding flows for agents. Using her Cursor-built travel app Waypoint as an example, she frames three questions: how to let agents into the app, how to connect agent activity to real users, and how to limit and revoke an agent's access, especially for corporate travel where compliance and financial risk matter. She notes that agents will delegate research and getting-started work, so the human's 'epiphany moment' may happen through the agent rather than directly.

The proposed mechanism is a file called `off.md` (as transcribed), an open Markdown protocol shipped with the application that describes how agents can register accounts, gain access, and call the API. Crucially, the file describes access and operations, but the application itself still performs authorization via its API. The protocol has two modes: an anonymous mode where agents can perform limited actions to prove product value without signing up, and an authenticated mode where the agent acts on behalf of a real user with expanded permissions.

The anonymous-to-claimed flow works like this: the agent performs anonymous actions through the API and receives an access token plus a claim token. The agent then gives the user a link and a one-time code; the user registers, logs in, and enters the code to claim the agent's prior actions and transfer them to their account. Finally, the app's authorization server uses OAuth to issue an access token on behalf of that user to the agent, which then calls the API. Williams flags that this manual flow (links, registration, code entry, email confirmation) is exactly where product-driven growth loses users.

She then asks why, if the agent provider already knows who the user is (as with Claude Code or Muse, which verify identity via email), it can't simply tell the application who the user is and skip manual intervention. She begins describing this as also possible via the protocol's auth mode, though the transcript cuts off mid-explanation.

- Agents are becoming first-class users, so apps need agent-oriented onboarding and signup flows.
- An `off.md` Markdown file lets agents learn how to register, gain access, and call your API, while the app retains authorization control.
- Two modes: anonymous limited actions for trial, and user-linked access with expanded permissions.
- A claim-token plus one-time-code flow lets a human claim and transfer an agent's anonymous actions to their account, followed by OAuth tokens for the agent.
- Manual claim flows (links, codes, email confirmation) are friction points; provider-asserted identity could remove them.