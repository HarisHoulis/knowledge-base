---
domain: system-design
subdomain: server-side-redirects
concept: custom-short-link-redirector
title: Custom short-link redirector
sources:
  - title: "Custom short-link redirector"
    url: "https://jakewharton.com/custom-short-link-redirector/"
---

# Custom short-link redirector

The article describes the author's migration from Bitly to Netlify for hosting a custom short-link redirector. The author had used Bitly for years with a custom domain (jakes.link), but Bitly's announcement that free users would see ad-backed preview pages made the service untenable. The paid plan supporting custom domains costs $350/year, which is excessive for the few links the author creates per year. The author chose Netlify because it already hosts his site and supports server-side redirects via a `_redirects` file, providing a free, data-driven alternative.

- Bitly's path customization is a global namespace, and free custom domains now show ads before redirecting; paid plans are expensive.
- Netlify's `_redirects` file enables a simple, free server-side redirector that can handle custom domains.
- Migration involves three steps: create a git repo with a `_redirects` file, deploy it on Netlify, and add a custom domain alias.
- The solution is data-driven (redirects are in a git repo) and controllable, though it sacrifices built-in analytics and a user-friendly link creation experience.