---
domain: system-design
subdomain: event-driven architecture
concept: event-terminology-disambiguation
title: Every Event, Everywhere, All at Once: Disambiguating What “Event” Means
sources:
  - title: "Every Event, Everywhere, All at Once • Jacqui Read • GOTO 2025"
    url: "https://www.youtube.com/watch?v=1dIjb9A4uow"
    author: "GOTO Conferences (Jacqui Read)"
    date: "2026-08-25"
---

# Every Event, Everywhere, All at Once: Disambiguating What “Event” Means

Jacqui Read's GOTO talk is framed as a disambiguation of the word "event," motivated by the confusion caused by the many different types of events in computing (Read, GOTO 2025). She starts from definitions: a colloquial "occurrence, something that happens" carries too little information, and a "pre-arranged social activity" describes what is really a calendar event — something tied to time and date that may be in the past, the future, or the present (Read, GOTO 2025).

For computing, she offers a deliberately broad umbrella definition: an event is "an end result, an outcome" — something that has already happened. The key property is tense and immutability: it is not happening and not going to happen, the outcome is known and will not change (Read, GOTO 2025). This generality is required to cover all the different event types used in computing (Read, GOTO 2025).

The talk then traces events back historically, citing JDK 1.1 from 1997 and its PreferenceChangeEvent and PropertyChangeEvent, which were largely about changing things via the UI (Read, GOTO 2025). Inspecting PreferenceChangeEvent shows it models a preference being added, removed, or changed — an early example of an event that bundles multiple meanings into one type (Read, GOTO 2025).

Read notes that events today can also model more than one thing, and that this often causes problems: consumers who only care about, say, whether something was added or removed must consume every event and determine its type, wasting effort or acting unnecessarily (Read, GOTO 2025). Structurally, the historical example already resembles modern events — the event acts as a wrapper carrying the information, here a key (identifier) and a string holding the new value, and it could equally have carried the old value (Read, GOTO 2025).

- Computing events are best defined broadly as something that has already happened — an outcome that is known and unchangeable — as opposed to calendar events, which are tied to a time and date and can be past, present, or future.
- The multiplicity of event types and terminology is itself a source of confusion, which motivates the disambiguation framing.
- Events have a long history in computing: JDK 1.1 (1997) included PreferenceChangeEvent and PropertyChangeEvent, mostly for changing things through the UI.
- Early events already showed today's pattern of bundling multiple meanings (add/remove/change) into one type, forcing consumers to inspect every event to find what they need.
- An event functions as a wrapper for information — in the JDK example, a key identifier plus the new value (and potentially the old value).