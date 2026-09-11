---
domain: android-kotlin
subdomain: android-library-maintenance
concept: dropping-legacy-android-support
title: Dropping Android 1.6 Support in ActionBarSherlock 4.0
sources:
  - title: "ActionBarSherlock - A Love Story (Part 1)"
    url: "https://jakewharton.com/actionbarsherlock-a-love-story-part-1/"
    author: "Jake Wharton"
---

# Dropping Android 1.6 Support in ActionBarSherlock 4.0

In this post Jake Wharton announces that ActionBarSherlock 4.0 will drop support for Android 1.6 (API level 4). After nearly 9 months and 22 releases across 3 major versions, the upcoming 4.0 is described as the first "true" release, bringing full Ice Cream Sandwich action bar functionality to all relevant APIs (source).

The original justification for supporting 1.6 was that the library was tightly integrated with the official Android compatibility library, which itself supported 1.6. ABS 4.0 takes a different direction: the core library will have zero dependencies, and the action bar is simplified to stand alone. Since the library no longer depends on the compat lib, Wharton's reason to force 1.6 support is gone (source).

Wharton also cites technical obstacles specific to 1.6. Its classloader is "over-eager": it checks every method call in loaded classes, forcing workarounds using concise static inner-classes, and it cannot call superclass implementations of methods you have implicitly overridden. These problems recur heavily in the ICS action bar for things like accessibility and configuration changes. API 7 (Android 2.1) becomes the new minimum target of the library (source).

He acknowledges some users will be angered, noting one implementer still supports 1.5 for a niche market of Motorola i1 owners. Having developed and maintained the library for 9 months in his spare time for free, Wharton invites those who need 1.6 support to fork it, implement it themselves, and send a pull request, or to sponsor the effort (source).

- ActionBarSherlock 4.0 drops Android 1.6 (API level 4), setting API 7 (Android 2.1) as the new minimum.
- The decision follows ABS 4.0 moving to a zero-dependency core library, severing the tight integration with the compat lib that justified 1.6 support.
- Android 1.6's classloader forces awkward static inner-class workarounds and blocks calls to superclass implementations of overridden methods.
- The maintainer, who built the library for free in his spare time, asks those needing 1.6 support to fork, send a pull request, or sponsor the work.