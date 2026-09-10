---
domain: android-kotlin
subdomain: android-ui
concept: actionbarsherlock
title: Using ActionBarSherlock as a Base for Android Apps
sources:
  - title: "Using ActionBarSherlock As A Base"
    url: "https://developer.squareup.com/blog/using-actionbarsherlock-as-a-base"
    author: "Jake Wharton"
---

# Using ActionBarSherlock as a Base for Android Apps

ActionBarSherlock is an open source Android library that brings the full action bar design pattern to older platform versions under a unified API and theme. It delegates to the built-in platform action bar where appropriate and uses a compatibility implementation otherwise, so developers can call getSupportActionBar() instead of getActionBar() while keeping the same API.

The article compares three approaches: custom layouts, Google's ActionBarCompat sample, and ActionBarSherlock. Custom layouts offer maximum flexibility but require the largest developer-time investment and do not use the built-in platform action bar unless extra work is done. ActionBarCompat is described as a rudimentary sample that covers only a limited subset of action bar features and is not intended as a full library.

ActionBarSherlock is presented as providing the full feature set of the latest built-in action bar back to Android 2.1 and newer, including list navigation, stacked tab navigation, custom action item views, action item submenus, and action modes. Theming mirrors the built-in action bar by creating a style with duplicate attributes, one with the android: prefix and one without.

By combining ActionBarSherlock with Google's support library, the article says developers can provide the Honeycomb-introduced action bar, fragments, and loaders to 99% of devices with access to Google Play Store without writing version-specific code. Square used ActionBarSherlock in the Pay with Square app, later enabling advanced features such as action providers, expandable action items, and dynamic theming with little additional work because the API matched the native action bar.

- ActionBarSherlock provides the full latest platform action bar feature set to Android 2.1+ under the same API, exposed via getSupportActionBar().
- Custom action bar layouts offer maximum flexibility but require the most developer time and forgo built-in platform action bar improvements.
- Google's ActionBarCompat is only a rudimentary sample covering a limited subset of action bar features, not a full library.
- Theming ActionBarSherlock mirrors built-in action bar theming by duplicating attributes with and without the android: prefix.
- Combining ActionBarSherlock with the support library delivers action bar, fragments, and loaders to 99% of Play Store devices without version-specific code.