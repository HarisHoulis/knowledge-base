---
domain: engineering-culture
subdomain: software-strategy
concept: shannons-demon-volatility
title: Reject Change, Sometimes: Shannon's Demon and Volatility Strategy
sources:
  - title: "Reject Change, Sometimes: Shannon's Demon and Volatility Strategy"
    url: "https://newsletter.kentbeck.com/p/reject-change-sometimes"
---

# Reject Change, Sometimes: Shannon's Demon and Volatility Strategy

Kent Beck uses a parable of three traders to build intuition about volatility. Prudence keeps all coins in a strongbox (no risk, no gain); Reckless bets everything on a coin flipper that doubles or halves the stake; SD (Shannon's Demon) splits coins half in the box and half in the flipper, rebalancing every day. Over time Prudence stays flat, Reckless oscillates around flat, but SD's stack grows—same investments, different outcomes. Beck walks through a win-then-loss and loss-then-win sequence to show that rebalancing banks winnings and shrinks losses, giving up upside while avoiding downside.

He maps this to software product development. Extract is the domain most like the balanced flipper: you make a change, maybe gain customers or revenue, maybe lose some. There the SD strategy fits—protect the revenue stream, take some growth bets, lower costs, keep changes reversible. But the calculus changes when the payoff is asymmetric: with a flipper paying triple on a win and losing only a third on a loss, going all in beats rebalancing, so Explore is pure Reckless. Beck stresses the interesting question isn't expected value but *how* to play.

Expand needs a richer model with three outcomes per turn: overcome the next growth bottleneck, die (losing everything and all future gains), or switch to Extract. There the value-creating strategy is engineering and operational investment to reduce the probability of death or increase the chance of clearing the next hurdle—performance tuning, securing resources, backup and recovery. During Expand, demand is pulling; pushing increases risk, so reducing friction sustains growth. Beck includes a small JavaScript simulator to build intuition, crediting Kunal Bhalla for the Shannon's Demon reference.

- Rebalancing between a safe asset and a volatile one (Shannon's Demon) can grow wealth even when the volatile bet is fair, by banking wins and shrinking losses
- Extract-phase product work resembles the balanced flipper: protect revenue, take some growth bets, keep changes reversible
- With strongly asymmetric payoffs (e.g. +300%/-33%), going all in on the risky bet beats rebalancing—Explore is deliberately reckless
- Expand adds a death outcome that erases all future gains, so value comes from engineering/operational investment that reduces death probability or raises the odds of clearing the next bottleneck
- The key question isn't whether a bet has positive expected value but how to play it