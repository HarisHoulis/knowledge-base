---
domain: web-dev
subdomain: http-caching
concept: vary-header-caching
title: Cloudflare Adds Vary Header Support, Enabling Content Negotiation Behind Its Cache
sources:
  - title: "We just shipped support for the ugliest part of HTTP: Vary (Hacker News)"
    url: "https://news.ycombinator.com/item?id=49823195"
  - title: "Simon Willison's comment on "We just shipped support for the ugliest part of HTTP: Vary""
    url: "https://news.ycombinator.com/item?id=49823195#49823961"
    author: "Simon Willison"
    date: "2026-09-23"
---

# Cloudflare Adds Vary Header Support, Enabling Content Negotiation Behind Its Cache

Simon Willison notes he has wanted Cloudflare support for the Vary header "for years" [1]. The classic motivating case is content negotiation: user agents that send "accept: text/html" receive HTML, while agents that don't receive JSON or another format [1].

That pattern was previously impossible to deploy behind Cloudflare caching because Cloudflare ignored the Vary header on anything other than images, so a cached JSON response risked being served to someone expecting HTML [1].

Independent of the new Cloudflare feature, Willison says he decided never to use that Accept-based pattern, preferring URLs that predictably return HTML or JSON — he adds a .json suffix to his apps to serve JSON instead [1].

- Cloudflare now supports the Vary header, a feature Willison had wanted for years.
- Previously Cloudflare ignored Vary on anything other than images, making Accept-header-based content negotiation unsafe behind its cache.
- The risk was caching a JSON variant and serving it to a client that expected HTML.
- Willison prefers explicit .json-suffixed URLs over content negotiation for predictable response formats.