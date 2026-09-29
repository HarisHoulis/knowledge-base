---
domain: android-kotlin
subdomain: android-ui-libraries
concept: actionbarsherlock-beta
title: Something Beta This Way Comes!
sources:
  - title: "Something Beta This Way Comes!"
    url: "https://jakewharton.com/something-beta-this-way-comes/"
    author: "Jake Wharton"
---

# Something Beta This Way Comes!

The ActionBarSherlock 4.0 beta release outlines implementation details for the Android action bar compatibility library. It provides six base activities: SherlockActivity, SherlockPreferenceActivity, SherlockListActivity, and SherlockExpandableListActivity in the core library, plus a modified FragmentActivity and a separate SherlockMapActivity plugin. All classes now live under com.actionbarsherlock.*, and developers are warned to avoid com.actionbarsherlock.internal.* and to check imports before reporting bugs. [source]

Default options menu methods are final in the base activities to prevent erroneous use. SherlockPreferenceActivity does not support fragments or loaders as v3.x did, and PreferenceFragment porting is a future possibility without an ETA. Issues related to the compat-lib plugin should be filed on b.android.com rather than the library's tracker. [source]

The beta has known bugs and missing features. Users are encouraged to check the bug tracker, samples, and the 4.0-wip branch, build plugins themselves if needed, and test the beta thoroughly before the final release. Theme.Sherlock must be used; only a dark theme is available for testing, with light and light/dark action bar themes planned for the release candidate. Bug reports should be filed on GitHub with detailed descriptions, code, and images; pull requests are welcome. [source]

- ActionBarSherlock 4.0 beta includes six base activities: four core Sherlock activities, a modified FragmentActivity, and a separate SherlockMapActivity plugin.
- All classes moved to com.actionbarsherlock.*; avoid com.actionbarsherlock.internal.* and verify imports.
- Default options menu methods are final in base activities; SherlockPreferenceActivity lacks fragment and loader support, with no ETA for PreferenceFragment.
- Use Theme.Sherlock; only a dark theme is available for testing, with light and light/dark action bar themes planned for the release candidate.
- Test betas thoroughly, check samples and the 4.0-wip branch, and report bugs on GitHub with detailed descriptions, code, and images; pull requests are welcome.