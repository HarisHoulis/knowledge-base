---
domain: web-dev
subdomain: react-typescript
concept: custom-hook-tuple-typing
title: Wrapping React.useState with TypeScript
sources:
  - title: "Wrapping React.useState with TypeScript"
    url: "https://kentcdodds.com/blog/wrapping-react-use-state-with-type-script"
    date: "2021-01-19"
---

# Wrapping React.useState with TypeScript

The article explores a common TypeScript issue when wrapping React's useState in a custom hook, using a useDarkMode hook as the example. The initial implementation returns [mode, setMode] directly, but TypeScript infers this as an array whose elements are either string or React.Dispatch, causing the setter to be considered possibly not callable. This conflicts with how React's own useState is typed as a tuple [S, Dispatch<SetStateAction<S>>], which allows destructuring to preserve each element's type (Kent C. Dodds, 2021).

The author presents three fixes: annotating the full return type, using an intermediate typed variable, or using a `const` assertion (`as const`) on the returned array. The `as const` approach is highlighted as the cleanest because it tells TypeScript the values are constant and preserves the precise tuple shape without verbose annotations. Furthermore, the state type can be narrowed from string to the union `'dark' | 'light'`, making the hook safer by limiting acceptable values for the setter. Type aliases for both the state and dispatch function help keep prop types readable when passing values through multiple components (Kent C. Dodds, 2021).

- Returning an array from a custom hook without a tuple type makes TypeScript infer a union array, causing errors when calling the setter.
- React's useState uses an explicit tuple type, so custom wrappers must recreate that shape for destructuring to work correctly.
- The `as const` assertion is the simplest way to preserve the tuple type for a returned array.
- Using a union type like `'dark' | 'light'` for state makes invalid setter calls a compile-time error.
- Type aliases for state and dispatch functions improve prop typing across component hierarchies.