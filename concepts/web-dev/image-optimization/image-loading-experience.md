---
domain: web-dev
subdomain: image-optimization
concept: image-loading-experience
title: Building an awesome image loading experience
sources:
  - title: "Building an awesome image loading experience"
    url: "https://kentcdodds.com/blog/building-an-awesome-image-loading-experience"
    author: "Kent C. Dodds"
    date: "2021-10-19"
---

# Building an awesome image loading experience

For placeholders, Dodds compares Unsplash's multi-layered approach—solid color, blurhash canvas, then full image—and chooses a simpler server-rendered base64 data URL of a low-resolution, blurred Cloudinary version (Kent C. Dodds, 2021). To further improve the visual while loading, he applies a `backdrop-blur` filter over the placeholder, which removes pixelation and gives a pleasing blur (Kent C. Dodds, 2021). Finally, he fades in the real image on load using a small React `BlurrableImage` component that listens for the `load` event and toggles visibility (Kent C. Dodds, 2021).

- Reserve image space with aspect-ratio CSS to avoid cumulative layout shift.
- Combine `srcset`/`sizes` with a CDN like Cloudinary to deliver context-appropriate image sizes.
- Use a server-rendered, base64-encoded blurred thumbnail as the placeholder for instant feedback.
- Add `backdrop-filter: blur` over the placeholder to smooth pixelation and fades in the real image when loaded.