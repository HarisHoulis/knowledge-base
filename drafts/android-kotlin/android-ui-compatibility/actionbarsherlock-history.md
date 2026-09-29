---
domain: android-kotlin
subdomain: android-ui-compatibility
concept: actionbarsherlock-history
title: ActionBarSherlock: A Love Story (Part 2) — Origins and Evolution
sources:
  - title: "ActionBarSherlock - A Love Story (Part 2)"
    url: "https://jakewharton.com/actionbarsherlock-a-love-story-part-2/"
    author: "Jake Wharton"
---

# ActionBarSherlock: A Love Story (Part 2) — Origins and Evolution

ActionBarSherlock began from a personal need: after migrating work servers to VMware/vSphere in January 2011, Jake Wharton wanted an Android app to view VM information and perform quick vMotions. Finding only two inferior, closed-source Android Market apps, he started writing his own. Porting the Java SDK to Android took about a month and led to a custom SOAP client with aggressive caching and lazy loading; he then needed an application shell [1].

At the time he thought GreenDroid was the best library for common UI patterns, but the Honeycomb SDK landed that same week and he wanted one APK for phones and tablets. Pre-Android Compatibility Library, he proxied the action bar APIs of GreenDroid and Honeycomb. Version 1 was completed in one day, proxied only needed methods, and required two static inner classes for pre- and post-Honeycomb handling; a naming conflict over getActionBar() led him to Hameno’s GreenDroid fork with getGDActionBar(), and he added a compatibility mention to the README. Version 2 came the next day as a complete rewrite, dropping GreenDroid and adding Android-ActionBar support [1].

Version 2.1.0, released two weeks later, added the compatibility dependency, Maven build/release, list navigation, menu inflation, and Fragment support. The custom fluent API was limiting, so he rewrote the library around interfaces for individual action bar features, reaching feature-complete “lost” 3.0 code on May 12, 2011. An epiphany followed: instead of a custom action bar API, why not provide the full API through getSupportActionBar() exactly like the compatibility library? After adapting the code and working with Johan Nilsson to expand Android-ActionBar, version 3.0.0 was released on June 5, 2011, internalizing Android-ActionBar sources to mirror the native API on Android 1.6+. Releases on 3.x continued steadily to 3.5.0. The original vSphere app was never completed, partly because ActionBarSherlock’s popularity overwhelmed his free time and his SOAP client remained unstable [1].

- ActionBarSherlock originated from the author’s personal need for a vSphere client app after finding no suitable open-source Android Market alternatives.
- Version 1 was completed in one day as a proxy over GreenDroid and Honeycomb action bar APIs; version 2 was a complete rewrite the next day and added Android-ActionBar support.
- Version 2.1.0 added the Android Compatibility Library dependency, Maven build/release, list navigation, menu inflation, and Fragment support.
- The “lost” 3.0 was interface-based and feature-complete on May 12, 2011; an epiphany led to mirroring the full native action bar API via getSupportActionBar(), released as 3.0.0 on June 5, 2011.
- The original vSphere app was never completed; community interest in ActionBarSherlock overwhelmed the author’s free time, and he had never written an app using his own libraries.