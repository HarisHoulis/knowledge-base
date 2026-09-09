---
domain: android-kotlin
subdomain: image-loading
concept: picasso-image-loading
title: Enhance Your Application Using Picasso
sources:
  - title: "Enhance Your Application Using Picasso"
    url: "https://developer.squareup.com/blog/enhance-your-application-using-picasso"
    author: "D. Koutsogiorgas, Jake Wharton"
---

# Enhance Your Application Using Picasso

Square introduced and open sourced Picasso, an image downloading and caching library for Android designed to be fast and simple to use, often requiring only one line of code. The library automatically handles caching, recycling, and displaying bitmaps into target views, making it suitable for both single images and adapter-based list loading.

- Picasso provides a fluent API that can load and display an image with a single line of code.
- It automatically handles memory and disk caching, bitmap recycling, and displaying the final image.
- Images can be transformed, e.g., via resize and centerCrop, with the result stored in memory for reuse.
- Transformation work happens on a background thread to avoid blocking the UI.
- For development, Picasso can display colored markers indicating the image source (memory, disk, or network).