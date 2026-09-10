---
domain: android-kotlin
subdomain: android-animation
concept: pre-honeycomb-animation-proxy
title: Advanced Pre-Honeycomb Animation with NineOldAndroids
sources:
  - title: "Advanced Pre-Honeycomb Animation with NineOldAndroids"
    url: "https://jakewharton.com/advanced-pre-honeycomb-animation/"
    author: "Jake Wharton"
---

# Advanced Pre-Honeycomb Animation with NineOldAndroids

Android 3.0 introduced an animation framework with View methods for translation, scale, rotation, and alpha. The NineOldAndroids library backports this API to older platforms, but originally it could only modify values for which methods already existed on the running platform, so the new Honeycomb View properties could not be animated on pre-3.0 devices. The author sought a reliable solution, but neither StackOverflow answers nor advice from Chet Haase produced a stable implementation; the usual recommendation was to use the built-in view animation.

The key insight came from examining how view animations are processed. An animation receives a Transformation object and a time interval, and it adjusts that object to reflect the associated view's state. Because Transformation exposes alpha and a canvas matrix, it can achieve all of the transformations introduced natively in Honeycomb. The author implemented a custom Animation subclass that sets setDuration(0) and setFillAfter(true), calls view.setAnimation(this), and acts as a proxy to alpha and the Transformation object. It exposes getter and setter methods for the Honeycomb properties, stores values in instance variables, and calls view.invalidate() on each change so the transformation is reapplied.

To make this seamless with NineOldAndroids, the integration adds a check in ObjectAnimator initialization. If the animation uses a named property rather than a Property, runs on pre-3.0 Android, targets a View, and the named property is one introduced in Honeycomb, a proxy Property is used. PROXY_PROPERTIES maps those property names to special Property classes that automatically use the proxy animation class, overriding the string equivalent so reflection is not attempted. This allows Honeycomb-style multi-property animation by changing imports to NineOldAndroids, as in an AnimatorSet using ObjectAnimator.ofFloat for rotationX, rotationY, rotation, translationX, translationY, scaleX, scaleY, and alpha.

- NineOldAndroids backports the Honeycomb animation API but originally could not animate Honeycomb-introduced View properties on pre-3.0 platforms.
- View animation's Transformation object provides alpha and a canvas matrix, which is enough to implement translation, scale, rotation, and alpha transformations.
- A custom Animation proxy sets setDuration(0) and setFillAfter(true), attaches itself to the View, and applies stored property values whenever the view is invalidated.
- ObjectAnimator automatically selects a proxy Property when a named property targets a View on pre-3.0 and the property is one introduced in Honeycomb, avoiding reflection.
- The example AnimatorSet uses ObjectAnimator.ofFloat to animate rotationX, rotationY, rotation, translationX, translationY, scaleX, scaleY, and alpha together.