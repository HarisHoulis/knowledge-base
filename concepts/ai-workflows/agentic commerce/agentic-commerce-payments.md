---
domain: ai-workflows
subdomain: agentic commerce
concept: agentic-commerce-payments
title: How AI Agents Pay: Checkout via Agent Commerce Protocol and MCP Apps
sources:
  - title: "How AI Agents Pay: Checkout in ChatGPT and Google AI Mode — Sam Parsons, PayPal"
    url: "https://www.youtube.com/watch?v=c5U-XbbEN-g"
    author: "AI Engineer"
    date: "2026-10-06T01:30:12+00:00"
---

# How AI Agents Pay: Checkout via Agent Commerce Protocol and MCP Apps

Sam Parsons, a senior staff engineer at PayPal, describes how agent commerce works from PayPal Corporate Payments (formerly Braintree), which processes payments for large merchants. The central takeaway is that PayPal Enterprise Payments is building bridges so merchants can accept payments from many agentic surfaces, a field he says is evolving rapidly. He outlines three paths: OpenAI's Agent Commerce Protocol in ChatGPT, Google's Universal Commerce Protocol—which he says is almost identical in specification—and a human-in-the-loop path using only MCP applications with external payment (Parsons, "How AI Agents Pay").

In the ChatGPT/ACP flow, the user searches and a merchant's MCP app displays products inside the chat; the merchant controls the UI and appearance because the MCP app embeds HTML and JavaScript and can run in agents like ChatGPT and Claude as a connector. When the user chooses to buy, the MCP app contacts its host, ChatGPT, to purchase using the Agent Commerce Protocol. The user enters or uses saved card details, payment data is tokenized through PayPal systems, and the merchant ultimately makes the withdrawal. Sellers provide an MCP app experience and receive tokens from PayPal Corporate Payments that look like standard tokens they already process (Parsons, "How AI Agents Pay").

Backend billing, refunds, chargebacks, and compliance remain the same and are supported through PayPal Corporate Payments. In the demo, the seller drives the product interface, while the ChatGPT instant payment checkout interface is provided by ChatGPT and is currently being improved; the user enters card details—only a test card in the demo—which are tokenized via PayPal (Parsons, "How AI Agents Pay").

- PayPal Corporate Payments (formerly Braintree) has created an integration with OpenAI's Agent Commerce Protocol so merchants can accept instant payments inside ChatGPT.
- Merchants use MCP apps to embed seller-controlled UI inside agents; checkout is handled by ChatGPT's instant payment interface, and payment data is tokenized through PayPal.
- Backend billing, refunds, chargebacks, and compliance remain supported through PayPal Corporate Payments, making the agent payment flow similar to standard token processing for sellers.
- Google's Universal Commerce Protocol is described as very similar to OpenAI's Agent Commerce Protocol, and another path supports agent payments with human involvement using MCP applications and external payment.