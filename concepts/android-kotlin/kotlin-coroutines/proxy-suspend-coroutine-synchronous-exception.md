---
domain: android-kotlin
subdomain: kotlin-coroutines
concept: proxy-suspend-coroutine-synchronous-exception
title: Exceptions and proxies and coroutines, oh my!
sources:
  - title: "Exceptions and proxies and coroutines, oh my!"
    url: "https://jakewharton.com/exceptions-and-proxies-and-coroutines-oh-my/"
    author: "Jake Wharton"
---

# Exceptions and proxies and coroutines, oh my!

In this article, Jake Wharton explores a subtle interaction between Java's `Proxy` and Kotlin coroutines in Retrofit. Checked exceptions are enforced only by the Java compiler; at runtime, throwing a checked exception from a method on a `Proxy` instance can cause an `UndeclaredThrowableException` if the method does not declare it. Because Kotlin suspend functions do not require checked exception declarations, this became a practical issue when Retrofit added coroutine support via interface proxies. ([jakewharton.com](https://jakewharton.com/exceptions-and-proxies-and-coroutines-oh-my/))

The article explains that a Kotlin `suspend` function compiles to a method returning `Object` and taking an extra `Continuation` parameter, allowing a synchronous result or the `COROUTINE_SUSPENDED` marker. Retrofit uses `suspendCoroutine` to adapt its callback API; this API wraps the real continuation to intercept synchronous invocations and protect the call stack. A race condition caused by thread preemption between creating the continuation wrapper and calling `getResult()` can make a callback invoke the continuation synchronously, causing a checked exception to propagate synchronously and trigger the `UndeclaredThrowableException`.

The fix in Retrofit 2.6.1 catches the checked exception at the Java boundary and calls a Kotlin helper that performs `yield()` before rethrowing it, ensuring the exception is delivered to the continuation asynchronously rather than as a synchronous checked exception. This workaround is recommended for any library that exposes suspend functions through a Java `Proxy`. ([jakewharton.com](https://jakewharton.com/exceptions-and-proxies-and-coroutines-oh-my/))

- Checked exceptions disappear in bytecode, but Java `Proxy` instances enforce a form of them by wrapping undeclared checked exceptions in `UndeclaredThrowableException`.
- Kotlin's `suspend` functions compile to methods returning `Object` with a `Continuation` parameter, so they can return a result synchronously or suspend.
- `suspendCoroutine` protects the stack by intercepting synchronous continuation invocations; a preemption race can break this protection and cause checked exceptions to appear synchronously.
- Retrofit 2.6.1 fixes the issue by catching exceptions at the Java layer and using `yield()` before throwing to force asynchronous continuation delivery.