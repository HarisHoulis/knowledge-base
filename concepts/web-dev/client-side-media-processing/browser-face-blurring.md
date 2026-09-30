---
domain: web-dev
subdomain: client-side-media-processing
concept: browser-face-blurring
title: Photo Scrubber — local face blur & metadata removal
sources:
  - title: "Photo Scrubber — local face blur & metadata removal"
    url: "https://simonwillison.net/2026/Sep/29/photo-scrubber/"
    author: "Simon Willison"
    date: "2026-09-29"
---

# Photo Scrubber — local face blur & metadata removal

Simon Willison built an experimental browser tool, Photo Scrubber, after taking a photograph of protesters and deciding he did not want to share images of strangers with identifiable faces. He had GPT-6 Astra build the tool, which detects faces in a photo and automatically blurs them out. The build is captured in a linked commit on his tools repository.

The implementation runs in the browser: it uses Google's MediaPipe C++ library compiled to WebAssembly via the @mediapipe/tasks-vision npm package, combined with the BlazeFace face detection model. The tool's title also indicates it performs local face blur and metadata removal, i.e. processing happens on the user's machine rather than a server.

The post is tagged photography and tools.

- Motivation: the author photographed protesters and did not want to publish identifiable faces of strangers.
- The tool was generated with GPT-6 Astra, with the build recorded in a public commit.
- Face detection uses Google's MediaPipe (C++ compiled to WebAssembly via @mediapipe/tasks-vision) and the BlazeFace model.
- It is described as a local tool for face blur and metadata removal.