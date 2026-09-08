---
domain: ai-workflows
subdomain: agent-output-persistence
concept: personal-software-factory
title: Introducing Kody: Your Personal Software Factory
sources:
  - title: "Introducing Kody: Your Personal Software Factory"
    url: "https://www.youtube.com/watch?v=QA0xYMAMjEg"
    author: "Kent C. Dodds"
    date: "2026-09-08"
---

# Introducing Kody: Your Personal Software Factory

Kent C. Dodds introduces Kody, a platform that preserves AI agent work by turning successful responses into persistent, runnable code packages. He criticizes the ephemeral nature of typical agent conversations, where users repeatedly ask the same question across chats, devices, and agents, paying for the same inference each time without retaining the outcome (Dodds, 2026). Kody acts as a 'mini GitHub and npm' where packages are real code that users own, can run, fork, and ship. It removes the model from the loop for repeated tasks, making them faster, cheaper, and more reliable, and continues running in the cloud even when the user's device is off (Dodds, 2026). Kody integrates with existing agents, ensuring outputs are portable across them. It also handles secrets in a vault so agents remain blind to sensitive keys, and provides package locking for security. The pitch positions Kody not as another AI agent, but as the infrastructure that gives agents a durable 'home' for the artifacts they create (Dodds, 2026).

- Agent conversation outputs are ephemeral; users re-ask and re-pay for recurring tasks.
- Kody saves agent-generated solutions as owned, reusable code packages.
- Packages run deterministically on schedules or triggers without model inference, improving cost and reliability.
- Work created in one agent follows the user to any other agent.
- Kody provides a secret vault and package locking to manage access and prevent rogue agent actions.