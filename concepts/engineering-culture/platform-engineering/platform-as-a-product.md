---
domain: engineering-culture
subdomain: platform-engineering
concept: platform-as-a-product
title: Platform Engineering for Developers, Architects & the Rest of Us
sources:
  - title: "Platform Engineering for Developers, Architects & the Rest of Us"
    url: "https://www.youtube.com/watch?v=ROBX-P7q1d8"
    author: "GOTO Conferences"
    date: "2026-08-26T12:00:33+00:00"
---

# Platform Engineering for Developers, Architects & the Rest of Us

In this GOTO 2025 talk, Daniel Bryant argues that platform engineering must have a product focus, treating developers as customers rather than merely re-branding DevOps [1]. He emphasizes that a platform should be built as a product to reduce developers' cognitive load, recalling how simpler platforms like Heroku and Cloud Foundry made it easy to "code, ship, and run," while the rise of microservices dramatically increased the learning burden [1]. Bryant also highlights that platform architecture and software architecture are symbiotic; he shares a personal mistake where a distributed system worked perfectly on his local machine but failed in the AWS cloud, illustrating the need to design software with platform constraints in mind [1]. Finally, he asserts that good APIs, abstractions, and automation are the ultimate prize of platform engineering, not merely swapping tools [1]. He traces the evolution of developer workflows and introduces the concept of a developer control plane as a way to help developers focus on delivery while the platform handles underlying complexity [1].

- Platform engineering should treat developers as customers and build the platform as a product, not just a DevOps rebranding.
- Platform architecture and software architecture are symbiotic; local designs may break in production cloud environments.
- The real value of platform engineering comes from well-designed APIs, abstractions, and automation.
- Reducing developer cognitive load is central, enabling developers to code, ship, and run without needing to manage every infrastructure detail.
- Platform engineering involves balancing build vs. buy and creating a developer control plane to streamline delivery.