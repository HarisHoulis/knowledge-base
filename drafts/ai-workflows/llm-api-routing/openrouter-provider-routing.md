---
domain: ai-workflows
subdomain: llm-api-routing
concept: openrouter-provider-routing
title: So you want to use OpenRouter?
sources:
  - title: "So you want to use OpenRouter?"
    url: "https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/"
    author: "Simon Willison"
    date: "2026-09-11"
  - title: "So you want to use OpenRouter?"
    url: "https://mmoustafa.com/blog/so-you-want-to-use-openrouter/"
    author: "Mohamed Moustafa"
  - title: "Hacker News discussion"
    url: "https://news.ycombinator.com/item?id=49621546"
---

# So you want to use OpenRouter?

Simon Willison highlights a post by Mohamed Moustafa warning that using OpenRouter can produce inconsistent behavior, because the same OpenRouter endpoint may be backed by different providers running different serving software, optimizations, and settings. The result is that identical model requests can behave differently depending on which provider handles them.

Specific divergences cited include providers that lack vision capability even for vision models, and differences in how the reasoning effort option is processed (Simon Willison, "So you want to use OpenRouter?").

The practical mitigation is to control routing explicitly: OpenRouter's `provider.only` option allows restricting requests to specific providers. To find out which providers are available, the `/endpoints` method returns the list of available providers for a given model ID.

- The same OpenRouter endpoint can behave differently across requests because different providers use different serving software, optimizations, and settings.
- Behavioral gaps include providers lacking vision capability for vision models and inconsistent handling of the reasoning effort option.
- OpenRouter's `provider.only` option lets you constrain routing to specific providers.
- The `/endpoints` method lists the available providers for a specific model ID.