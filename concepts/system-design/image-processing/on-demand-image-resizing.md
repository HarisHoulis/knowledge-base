---
domain: system-design
subdomain: image-processing
concept: on-demand-image-resizing
title: Dynamic Images with Thumbor
sources:
  - title: "Dynamic Images with Thumbor"
    url: "https://developer.squareup.com/blog/dynamic-images-with-thumbor"
    author: "Jake Wharton"
---

# Dynamic Images with Thumbor

Square uses a large number of user-generated images displayed across many mediums, including dashboard, market pages, Register client, email receipts, and Wallet. To handle this efficiently, they leverage Thumbor, an open-source on-demand image service that performs server-side cropping, resizing, and compositing. By requesting images at exact sizes, clients avoid downloading large files and scaling them locally, which reduces bandwidth, memory consumption, and disk usage. Thumbor URLs define the desired transformations, and options like domain whitelisting and authentication can secure the service from abuse. To simplify complex URL construction, Square developed Pollexor, a Java/Android URL builder, and ThumborURL for iOS clients.

- Thumbor enables server-side image resizing and transformation via specially constructed URLs.
- Requesting images at exact target sizes reduces bandwidth, memory consumption, and disk usage across clients.
- Security options such as domain whitelisting and authentication prevent unauthorized or abusive use of the image service.
- Square built Pollexor (Java/Android) and ThumborURL (iOS) libraries to make crafting Thumbor URLs more declarative and manageable.