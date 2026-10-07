# Interior-Point Algorithms for Discounted Markov Games

## Problem

Can a leader-based interior-point algorithm solve discounted Markov games with only logarithmic dependence on the inverse discount gap?

## Statement

Consider a finite turn-based two-player zero-sum Markov game with rational costs and transition probabilities. States belong to the minimizing or maximizing player. Let $`N,M`$ be the state and action counts, and let the common rational discount satisfy $`0<\gamma<1`$.

Seek an exact algorithm based on the leader's interior-point method with iterations or arithmetic operations bounded by

```math
\mathrm{poly}\!\left(N,M,\log\frac1{1-\gamma}\right)
```

rather than a polynomial in $`1/(1-\gamma)`$.

The leader/follower model, interior-point subproblems, output values or strategies, and dependencies on other numerical data must be specified. An approximate method or fixed-discount guarantee alone does not establish this exact-operation bound.

## Background

Single-player MDPs admit linear-programming formulations, while two-player games add minimax and best-response structure. The question is whether an interior-point analysis can retain favorable discount dependence in that setting.

## Known results

Ye [1] gives a single-player MDP interior-point result with logarithmic discount-gap dependence. Hansen et al. [2] concerns game strategy iteration, not the proposed interior-point method. Zhong and Ye [3] treat related robust MDPs with fixed discount; this does not establish the stated general-game bound.

## References

1. Y. Ye. *A new complexity result on solving the Markov decision problem*. MOR 30(3), 733–749, 2005. [Publication](https://pubsonline.informs.org/doi/10.1287/moor.1050.0149).
2. T. D. Hansen, P. B. Miltersen, U. Zwick. *Strategy iteration is strongly polynomial for 2-player turn-based stochastic games with a constant discount factor*. JACM 60(1), 2013. [arXiv:1008.0530](https://arxiv.org/abs/1008.0530).
3. H. Zhong, Y. Ye. *Linear Programming Representations and Strongly Polynomial Algorithms for Robust Markov Decision Processes*. [arXiv:2610.02131v1](https://arxiv.org/abs/2610.02131v1), 2026.
