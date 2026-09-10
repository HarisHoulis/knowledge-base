---
domain: web-dev
subdomain: react-state-management
concept: status-enum-over-booleans
title: Stop using isLoading booleans
sources:
  - title: "Stop using isLoading booleans"
    url: "https://kentcdodds.com/blog/stop-using-isloading-booleans"
    author: "Kent C. Dodds"
    date: "2020-03-02"
---

# Stop using isLoading booleans

The article argues against `isLoading` booleans and similar flags like `isRejected`, `isIdle`, or `isResolved`, because they cannot represent all possible states. Using a Geolocation API hook as an example, it shows how a boolean `isLoading` plus separate `position` and `error` fields can produce incorrect UI: after an error, the component may keep showing the last recorded position and never display the error, or the opposite can happen if the checks are swapped (Kent C. Dodds, 2020).

The article considers three fixes: require consumers to show both position and error, clear one when the other is set, or return an additional status property. It rejects the first because reusable APIs should make the right thing natural, and rejects clearing because some users may want to show the most recent position alongside an error. It therefore introduces a `status` enum with states `idle`, `pending`, `resolved`, and `rejected`, dispatching actions such as `started`, `success`, and `error` (Kent C. Dodds, 2020).

Consumers render based on `status`. Boolean conveniences can be derived from `status`, such as `isLoading = status === 'idle' || status === 'pending'`, but those booleans should not be stored in state to avoid impossible states. The article also demonstrates modeling the same logic with an XState state machine, where the status is built into the machine's finite state value and a terminal `rejectedNotSupported` state handles unsupported Geolocation (Kent C. Dodds, 2020).

The conclusion is to reduce reliance on booleans that cannot represent all actual states and instead use a state machine or an enum (Kent C. Dodds, 2020).

- `isLoading` booleans obscure real mutually exclusive states and can cause stale data or missed errors.
- A `status` enum (`idle`, `pending`, `resolved`, `rejected`) lets consumers know exactly which state is current.
- Derive boolean conveniences from `status`; do not store them in state, to avoid impossible states.
- State machines like XState encode finite states directly and can include terminal states such as unsupported geolocation.
- Prefer state machines or enums over booleans.