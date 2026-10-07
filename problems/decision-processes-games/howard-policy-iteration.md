# Howard's Policy Iteration Complexity for Deterministic MDPs

**Proposed by:** Yinyu Ye

## Problem

Is synchronous Howard policy iteration strongly polynomial for deterministic discounted Markov decision processes with an input discount factor?

## Statement

Consider $`N`$ states and $`M`$ actions, rational costs $`c(s,a)`$, deterministic successors $`f(s,a)`$, and a common rational discount $`0<\gamma<1`$. For a policy $`\pi`$, solve

```math
v^\pi(s)=c(s,\pi(s))+\gamma v^\pi(f(s,\pi(s))).
```

Then simultaneously choose actions minimizing $`c(s,a)+\gamma v^\pi(f(s,a))`$ at every state. Is the number of improving rounds bounded by a fixed polynomial in $`N,M`$, independent of $`\gamma`$ and numerical magnitudes?

Retain the current action when it is still minimizing, and use a fixed rule for other ties. A simplex rule that changes only one state per round is a different algorithm.

## Background

Deterministic transitions simplify the model but do not make synchronous policy updates equivalent to single-action simplex pivots. Input discounts near one separate fixed-discount guarantees from numerical-data-independent bounds.

## Known results

Ye [1] gives fixed-discount guarantees. Post and Ye [2] give a discount-independent strongly polynomial bound for a specific simplex rule on deterministic MDPs.

Zhong and Ye [4], in a preprint submitted in September 2026, claim exponentially many Howard improvements on deterministic MDPs, even with two actions per state. The claim has not been independently verified here. It concerns Howard's algorithm, not the existence of a different strongly polynomial algorithm.

## References

1. Y. Ye. *The simplex and policy-iteration methods are strongly polynomial for the Markov decision problem with a fixed discount rate*. MOR 36(4), 593–603, 2011. [Publication](https://pubsonline.informs.org/doi/abs/10.1287/moor.1110.0516).
2. I. Post, Y. Ye. *The simplex method is strongly polynomial for deterministic Markov decision processes*. MOR 40(4), 859–868, 2015. [arXiv:1208.5083v2](https://arxiv.org/abs/1208.5083v2).
3. T. D. Hansen, P. B. Miltersen, U. Zwick. *Strategy iteration is strongly polynomial for 2-player turn-based stochastic games with a constant discount factor*. JACM 60(1), 2013. [arXiv:1008.0530](https://arxiv.org/abs/1008.0530).
4. H. Zhong, Y. Ye. *Policy Iteration Is Not Strongly Polynomial for Deterministic Markov Decision Processes: The Price of Algorithmic Anarchy*. [arXiv:2609.40147v1](https://arxiv.org/abs/2609.40147v1), submitted 2026-09-30.
