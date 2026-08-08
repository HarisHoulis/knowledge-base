---
domain: android-kotlin
subdomain: date-time
concept: days-between-instants
title: Kotlin Development - Instants and LocalDates, Aargh!
sources:
  - title: "Kotlin Development - Instants and LocalDates, Aargh!"
    url: "https://www.youtube.com/watch?v=qiHaPl_aaxM"
    author: "Pairing with Duncan"
    date: "2022-02-19T15:59:01+00:00"
---

# Kotlin Development - Instants and LocalDates, Aargh!

In this episode, Duncan tackles a common date-time pitfall in Kotlin: calculating the number of days between two Instant values. He explains that an Instant represents a universal moment in time, independent of time zone. To determine how many days have passed, you must know the time zone because the concept of a 'day' (midnight-to-midnight) is zone-dependent. For example, the same two instants can be zero days apart in one zone and one day apart in another due to offset differences (Duncan, 2022).

Duncan proposes a solution: convert each Instant to a LocalDate using the target time zone, then retrieve the epochDay (the number of days since the epoch) for each and subtract them. This approach effectively counts the number of midnights crossed between the two instants in that zone. He tests this logic with a set of unit tests, including same-instant comparisons, same-day boundaries, and cross-day boundaries. He also checks the effect of daylight saving time by comparing January (GMT) and June (BST) scenarios in London, verifying that the same instants produce different day counts depending on the zone's offset (Duncan, 2022).

The emphasis of the episode is on trying to break the proposed logic rather than just confirming it. Duncan deliberately attempts to prove his own solution wrong across multiple edge cases, including reversing time order (expecting negative day counts) and shifting the time zone from UTC to GMT. The tests pass, giving confidence that the epoch-day-difference method is a robust way to calculate days between instants in Kotlin (Duncan, 2022).

- Instants are time-zone agnostic; converting to LocalDate requires a time zone to interpret calendar days.
- The number of days between two instants equals the difference in their LocalDate epochDay values in the same zone.
- Daylight saving time shifts, like London's January vs June, change the day count for the same instants.
- Edge cases include same instant, start-to-end of same day, and reversed order (negative days).
- Testing aims to falsify the approach rather than just confirm it.