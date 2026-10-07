# Strongly Polynomial Algorithm for General Discounted MDPs

## Problem

Is there a strongly polynomial exact algorithm for general discounted Markov decision processes when the discount factor is part of the input?

## Statement

Let $`S`$ be a finite state set with nonempty finite action sets $`A_s`$. Input data are rational rewards $`r(s,a)`$, rational transition probabilities $`p(t\mid s,a)\ge0`$ with $`\sum_{t\in S}p(t\mid s,a)=1`$, and a common rational discount $`0<\gamma<1`$. Set $`N=|S|`$ and $`M=\sum_s|A_s|`$.

Output a deterministic stationary policy $`\pi`$ optimal for every initial state, maximizing

```math
v^\pi(s)=\mathbb E_s^\pi\!\left[\sum_{t=0}^{\infty}\gamma^t r(s_t,\pi(s_t))\right].
```

The number of arithmetic operations must be bounded by a fixed polynomial in $`N,M`$, independent of numerical magnitudes and $`\gamma`$. Intermediate rational numbers must have encoding lengths polynomial in the input length.

The target covers arbitrary stochastic transitions and input discounts. A lower bound for one policy-iteration algorithm does not rule out another algorithm.

## Background

Ordinary polynomial-time solvability follows from linear programming. Strong polynomiality additionally separates the number of arithmetic operations from the numerical encoding length.

## Known results

Ye [1] gives fixed-discount simplex and policy-iteration results. Post and Ye [2] prove a discount-independent strongly polynomial bound for a particular simplex rule on deterministic MDPs.

For general transitions, Bellman inequalities $`v(s)\ge r(s,a)+\gamma\sum_t p(t\mid s,a)v(t)`$ form an LP. This gives polynomial bit complexity, not a strongly polynomial operation bound.

The robust-MDP result [4] assumes fixed discount. The claimed Howard lower bound [5] concerns a specific algorithm, not this existence question.

## References

1. Y. Ye. *The simplex and policy-iteration methods are strongly polynomial for the Markov decision problem with a fixed discount rate*. Mathematics of Operations Research 36(4), 593–603, 2011. [Publication](https://pubsonline.informs.org/doi/abs/10.1287/moor.1110.0516).
2. I. Post, Y. Ye. *The simplex method is strongly polynomial for deterministic Markov decision processes*. Mathematics of Operations Research 40(4), 859–868, 2015. [arXiv:1208.5083v2](https://arxiv.org/abs/1208.5083v2).
3. T. D. Hansen, P. B. Miltersen, U. Zwick. *Strategy iteration is strongly polynomial for 2-player turn-based stochastic games with a constant discount factor*. JACM 60(1), 2013. [arXiv:1008.0530](https://arxiv.org/abs/1008.0530).
4. H. Zhong, Y. Ye. *Linear Programming Representations and Strongly Polynomial Algorithms for Robust Markov Decision Processes*. [arXiv:2610.02131v1](https://arxiv.org/abs/2610.02131v1), submitted 2026-10-01.
5. H. Zhong, Y. Ye. *Policy Iteration Is Not Strongly Polynomial for Deterministic Markov Decision Processes: The Price of Algorithmic Anarchy*. [arXiv:2609.40147v1](https://arxiv.org/abs/2609.40147v1), submitted 2026-09-30.
