---
domain: android-kotlin
subdomain: testing
concept: idling-resource-deprecation
title: Deprecating idling resource libraries
sources:
  - title: "Deprecating idling resource libraries"
    url: "https://jakewharton.com/deprecating-idling-resource-libraries/"
    author: "Jake Wharton"
---

# Deprecating idling resource libraries

Jake Wharton announces the deprecation of two idling resource libraries for Android testing: RxIdler and okhttp-idling-resource. These libraries were created to monitor RxJava schedulers and OkHttp's dispatcher, allowing Espresso tests to wait for the app to become idle before proceeding. The author explains that while idling resources increased test stability, they expose application internals to the testing framework in a way no real user interacts with, violating the principles of the robot pattern and high-level test descriptions (Jake Wharton, https://jakewharton.com/deprecating-idling-resource-libraries/).

Instead, tests should wait on UI conditions that signal readiness, just as a real user would. For example, a user waits for the 'continue' button to turn green rather than for OkHttp's dispatcher to report idle. This approach makes failures more representative of real-world behavior. The author notes that Google has also shifted away from idling resources, providing alternatives in Compose testing and official documentation. For View-based layouts, he suggests writing a custom ViewAction that loops, checking the condition and yielding to the main thread until the condition is met (Jake Wharton, https://jakewharton.com/deprecating-idling-resource-libraries/).

The deprecated libraries remain stable and reliable; no changes are required for existing users. Deprecation is intended as guidance for new users to avoid this pattern and for existing users to migrate at their own pace to superior solutions based on UI condition waits.

- Idling resources couple tests to internal implementation details, unlike real user behavior.
- Tests should wait on observable UI conditions, such as a button becoming enabled.
- Google's official documentation now recommends alternatives to idling resources, especially in Compose.
- For View-based tests, a custom ViewAction can loop until a condition is met.
- RxIdler and okhttp-idling-resource are still stable but should not be adopted for new projects.