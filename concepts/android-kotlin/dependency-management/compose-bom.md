---
domain: android-kotlin
subdomain: dependency-management
concept: compose-bom
title: Let's defuse the Compose BOM
sources:
  - title: "Let's defuse the Compose BOM"
    url: "https://jakewharton.com/defuse-the-compose-bom/"
    author: "Jake Wharton"
---

# Let's defuse the Compose BOM

The Compose BOM (bill of materials) is commonly used to manage Compose library versions, but it is largely redundant for Gradle users. AndroidX libraries automatically bundle peer dependency constraints in Gradle module metadata, ensuring all artifacts in a library group resolve to the same version without manual intervention. Additionally, the Compose BOM only defines four distinct versions across five library groups, making it unnecessary when using version catalogs. The BOM adds indirection, masks real library versions with an opaque date-based number, and is inconsistently released. For new projects, it is better to directly declare the few Compose group versions, and existing projects can safely remove the BOM.

- Gradle module metadata in AndroidX libraries automatically aligns versions within each library group, eliminating the need for a BOM.
- The Compose BOM covers about 15 libraries but only uses four distinct versions across five groups.
- Version catalogs allow defining Compose versions centrally without relying on the BOM.
- The BOM's single date-based version hides the actual library versions, making it harder to track fixes.
- Gradual adoption of AndroidX betas partially overrides the BOM, reducing its effectiveness.