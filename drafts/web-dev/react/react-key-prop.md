---
domain: web-dev
subdomain: react
concept: react-key-prop
title: Understanding React's key prop
sources:
  - title: "Understanding React's key prop"
    url: "https://kentcdodds.com/blog/understanding-reacts-key-prop"
    date: "2019-11-11"
---

# Understanding React's key prop

React's `key` prop controls component instances, not just list rendering warnings. Each component instance has its own state, and React normally reuses the same element types across renders even if props change (source). The `key` prop is the exception: returning the same element type with a different key forces React to unmount the previous instance and mount a new one, removing all prior state and reinitializing the component (source).

For a component, this means React runs cleanup on effects, then state initializers and effect callbacks for the new instance. The article notes that effect cleanup happens after the new component is mounted but before the next effect callback runs (source). A counter example logs the initializer and effect callback on mount, skips them on normal re-renders, and runs them again when the parent changes the counter key (source).

The same principle applies to native form elements. In the contact form example, an uncontrolled `<input>` with `defaultValue={defaultValuesByTopic[topic]}` does not reset when the topic changes unless it has `key={topic}` (source). Adding the key makes React treat each topic as a new input instance, so the default subject updates and focus/value state can reset too (source).

Thus the `key` prop is a useful mechanism for controlling React component and element instances, in addition to its required role when rendering arrays (source).

- Changing a component's `key` forces React to unmount the old instance and mount a new one, destroying and reinitializing its state.
- React otherwise reuses the same element types across renders even when props change; `key` is the exception that resets instance identity.
- Using `key` on an uncontrolled input can reset its default value and focus when related state changes.
- The `key` prop applies to both custom components and native DOM elements.
- Effect cleanup runs after the new component mounts but before the next effect callback.