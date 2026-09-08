---
domain: android-kotlin
subdomain: picasso-palette-integration
concept: picasso-palette-transformation
title: Coercing Picasso To Play With Palette
sources:
  - title: "Coercing Picasso To Play With Palette"
    url: "https://jakewharton.com/coercing-picasso-to-play-with-palette/"
    author: "Jake Wharton"
---

# Coercing Picasso To Play With Palette

Jake Wharton explores how to integrate Android's Palette library with Picasso before official API support. He rejects Downloader/RequestHandler hooks because they require duplicating logic across image sources, sometimes receive InputStreams, and operate on raw bitmaps before transformations. Instead, he selects Transformation as the ideal hook because it runs after internal transformations like fit/resize/centerCrop and receives a Bitmap on Picasso's background thread (source).

- Palette support can be added to Picasso via a Transformation rather than waiting for official API changes.
- Downloader/RequestHandler are unsuitable because of source duplication, decoding responsibilities, and pre-transformation bitmaps.
- A stateful Transformation instance can be pooled to carry Palette metadata back to the caller after image loading.
- For memory-cached images, a Bitmap-keyed WeakHashMap provides a clean cache without duplicating Picasso's LruCache.
- URL-based caching for Palette is problematic because Picasso's LruCache lacks purge callbacks for reference counting.