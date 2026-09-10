---
domain: system-design
subdomain: authentication-architecture
concept: server-driven-authentication
title: Airbnb Cuts Authentication Code by 60% with Server Driven Architecture
sources:
  - title: "Airbnb Cuts Authentication Code by 60% with Server Driven Architecture"
    url: "https://www.infoq.com/news/2026/09/airbnb-server-driven-login/"
    author: "Leela Kumili"
    date: "2026-09-04"
---

# Airbnb Cuts Authentication Code by 60% with Server Driven Architecture

Airbnb redesigned its authentication architecture around server driven flows and policy based challenge selection. Rather than hardcoding authentication logic and challenge sequences in each client, the Flexible Authentication system lets the server dictate the flow and decide which challenge to present (Leela Kumili, InfoQ).

The reported results of the redesign are substantial: authentication related code dropped by 60%, the web client bundle shrank by 100 KB, successful authentication improved by 2.6%, duplicate account creation fell by 27%, and OTP costs were lowered by 11% (Leela Kumili, InfoQ).

The combination of a smaller client footprint and server-owned policy suggests the gains came from centralizing authentication decisions server-side while keeping clients thin. The improvements in duplicate account creation and OTP cost point to better challenge selection rather than merely cleaner code.

- Server driven flows plus policy based challenge selection form the core of Airbnb's Flexible Authentication redesign.
- Authentication related code was reduced by 60% and the web client bundle shrank by 100 KB.
- Successful authentication improved by 2.6% while duplicate account creation dropped 27%.
- OTP costs decreased by 11%.