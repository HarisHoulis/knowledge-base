---
domain: android-kotlin
subdomain: android-build
concept: aapt2-keep-rule-accuracy
title: Increased Accuracy of aapt2 Keep Rules
sources:
  - title: "Increased accuracy of aapt2 "keep" rules"
    url: "https://jakewharton.com/increased-accuracy-of-aapt2-keep-rules/"
---

# Increased Accuracy of aapt2 Keep Rules

The aapt2 tool packages Android app resources and generates ProGuard/R8 keep rules so types referenced only in resources (e.g., views in layout XML, activities in the manifest) are not removed. Prior to Android Gradle plugin 3.3.0-alpha05, these rules used an argument wildcard, such as `<init>(...)`, which forced all constructors of a referenced class to be retained even if only one was actually used reflectively. For example, RecyclerView has three constructors, but layout inflation only invokes the two-argument Context + AttributeSet constructor; the wildcard kept the unused Context-only constructor as well.

Starting with Android Gradle plugin 3.3.0-alpha05, aapt2 generates more precise keep rules that specify the exact constructor needed, such as `<init>(android.content.Context, android.util.AttributeSet)` for RecyclerView. The article demonstrates that the Context-only constructor is no longer present in the release APK. The three-argument constructor remains because the two-argument constructor delegates to it, but if optimization is enabled and there are no other uses, it could be inlined—something the old wildcard rules prevented.

This change has the most impact on View subclasses, which commonly define multiple constructors, while Application/Activity classes usually have only one constructor and are less affected. By increasing specificity of keep rules, the final APK contains fewer needlessly retained methods, and optimization passes can have a greater effect. Any bugs with the new rules can be reported on the Android issue tracker.

- Old aapt2 keep rules used `<init>(...)`, retaining every constructor of resource-referenced classes.
- New rules (AGP 3.3.0-alpha05+) target only the exact constructor used by reflective resource lookup.
- Example: RecyclerView's Context-only constructor is no longer kept as an extra.
- This reduces APK method counts and enables better optimization, especially for View subclasses with multiple constructors.
- Bug reports should go to the Android issue tracker.