# Strategy Iteration Complexity for Deterministic Turn-Based Zero-Sum Games

## Problem

Is simple strategy iteration polynomial, or strongly polynomial, for deterministic turn-based zero-sum discounted games?

## Statement

Let $`S=S_{\min}\uplus S_{\max}`$ be a finite state set. Each action has a rational immediate cost, a deterministic successor, and a common discount $`0<\gamma<1`$. The minimizing and maximizing players optimize the discounted total cost.

Consider a method alternating the leader's local strategy improvement, analogous to one simplex pivot, with the follower's exact best response. Ask whether:

1. Total operations are polynomial in the complete input encoding length.
2. A strongly polynomial bound exists in state and action counts, independent of discount and numerical magnitudes.

The leader, improving-state/action selection, tie rules, and follower-response algorithm must be specified. Count both outer improvement rounds and the total cost of computing follower responses.

## Background

A second player makes improvement depend on an adversarial best response. Deterministic successors retain combinatorial structure, but single-player progress arguments need not survive this interaction.

## Known results

Hansen, Miltersen, and Zwick [1] analyze strategy iteration for fixed-discount stochastic games. Post and Ye [2] treat a specific simplex rule for deterministic single-player MDPs.

Neither the single-player theorem nor a lower bound for synchronous Howard updates directly settles the local two-player method described here.

## References

1. T. D. Hansen, P. B. Miltersen, U. Zwick. *Strategy iteration is strongly polynomial for 2-player turn-based stochastic games with a constant discount factor*. JACM 60(1), 2013. [arXiv:1008.0530](https://arxiv.org/abs/1008.0530).
2. I. Post, Y. Ye. *The simplex method is strongly polynomial for deterministic Markov decision processes*. MOR 40(4), 859–868, 2015. [arXiv:1208.5083v2](https://arxiv.org/abs/1208.5083v2).
3. Y. Ye. *The simplex and policy-iteration methods are strongly polynomial for the Markov decision problem with a fixed discount rate*. MOR 36(4), 593–603, 2011. [Publication](https://pubsonline.informs.org/doi/abs/10.1287/moor.1110.0516).
