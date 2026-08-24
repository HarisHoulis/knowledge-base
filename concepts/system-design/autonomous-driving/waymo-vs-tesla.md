---
domain: system-design
subdomain: autonomous-driving
concept: waymo-vs-tesla
title: Waymo vs Tesla: Two Ways to Build Self-Driving Cars
sources:
  - title: "Waymo vs Tesla: Two Ways to Build Self-Driving Cars"
    url: "https://blog.bytebytego.com/p/waymo-vs-tesla-two-ways-to-build"
    author: "ByteByteGo"
    date: "Mon, 17 Aug 2026 15:30:56 GMT"
---

# Waymo vs Tesla: Two Ways to Build Self-Driving Cars

Waymo and Tesla represent two divergent architectures for self-driving cars. Waymo's sixth-generation system uses a multi-modal sensing suite—13 cameras, four lidar units, six radar units, and external audio receivers—to achieve 500-meter coverage and redundancy in adverse conditions [1][2]. Tesla relies primarily on cameras with a pure vision approach, using neural networks for semantic segmentation, object detection, and monocular depth estimation, ultimately building a birds-eye-view representation through 48 networks taking nearly 70,000 GPU hours to train [6][9]. This difference extends to representation: Waymo maintains compact structured representations (explicit object lists and roadgraph elements) for verifiability and simulation efficiency, while Tesla's learned representation captures nuance but is less inspectable [3][6].

- Waymo uses cameras, lidar, radar, and audio receivers; Tesla uses cameras only for its main FSD approach.
- Waymo builds explicit, structured representations of the world; Tesla uses end-to-end learned representations from per-camera networks.
- Waymo predicts multiple possible futures for each road user and validates trajectories via a separate onboard layer; Tesla's supervised FSD relies on an attentive driver, with a smaller driverless service under remote supervision.
- Safety reporting differs: Waymo reports rider-only miles with no human in driver's seat, showing 94% reduction in serious injury crashes; Tesla compares supervised FSD vs manual driving, reporting 7x fewer collisions.
- Both systems depend on machine learning but differ in how much is fixed in advance and how safety evidence is collected.