---
domain: android-kotlin
subdomain: android-ui
concept: actionbarsherlock-v4
title: ActionBarSherlock v4: Native-Style Action Bar for Older Android
sources:
  - title: "ActionBarSherlock - A Love Story (Part 3)"
    url: "https://jakewharton.com/actionbarsherlock-a-love-story-part-3/"
---

# ActionBarSherlock v4: Native-Style Action Bar for Older Android

The post announces ActionBarSherlock v4 and says 3.x users will get a two-month deprecation window from v4's release. The author describes v4 as the first version he thinks he will be truly proud of (ActionBarSherlock - A Love Story (Part 3)).

A major change is that v4 stops shuffling between native and custom implementations. Google's support library makes no attempt to use native implementations even if they exist because it is easier and more stable to keep functionality in the library, and the Android 4.0 action bar was designed to accommodate every conceivable screen size. Changes to Android 4.0's `MenuItem` interface made this shift a need rather than a choice. Support library classes are no longer in the core library; an optional plugin `.jar` will be provided with modified ActionBarSherlock support and minimal unrelated changes. The post warns that users of `FragmentMapActivity` or fragments in `SherlockPreferenceActivity` will have to change their implementation or create their own base classes (ActionBarSherlock - A Love Story (Part 3)).

Extending from a custom base activity is no longer required, though still recommended. Static attachment of the action bar is possible, allowing alternate base activities such as those from RoboGuice. Interaction logic is placed in a single class also used by base activities, so either approach affords the full API. Theming fully mirrors the native action bar with proper styles for the action bar, action mode, and sub-components, replacing v3.x's `ab`-prefixed attributes. It includes the Ice Cream Sandwich action bar features: split action bar, action modes, action providers, condensed tab navigation, and more (ActionBarSherlock - A Love Story (Part 3)).

A v4 beta was to be announced the next day with more technical detail. Bugs were tracked under GitHub milestone 4.0.0, and there was no timeline yet for final release; one or two release candidates were planned, with work on real implementations to find problems (ActionBarSherlock - A Love Story (Part 3)).

- v4 abandons switching between native and custom action bar implementations in favor of a custom-only approach for stability and consistency.
- Support library classes are removed from the core; an optional plugin jar adds ActionBarSherlock support with minimal changes.
- Custom base activities are no longer required: static attachment allows third-party base activities like RoboGuice while still exposing the full API.
- Theming mirrors the native action bar with proper action bar, action mode, and action view styles, plus ICS features such as split action bar and action providers.
- v3 gets a two-month deprecation window after v4's release; v4 beta details were to follow, with final release timeline unset.