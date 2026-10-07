# Planks Covering the Unit Ball

## Problem

How much of the unit ball can be covered by planks whose total width is less than its diameter?

## Statement

Let $`d\ge2`$ and $`B^d=\{x\in\mathbb R^d:\|x\|_2\le1\}`$. Fix positive widths $`w_1,\ldots,w_m`$ with $`W=\sum_iw_i<2`$. A plank of width $`w_i`$ has the form $`P_i=\{x:a_i\le u_i^Tx\le a_i+w_i\}`$, where $`\|u_i\|_2=1`$.

Determine the maximum over all orientations and translations:

```math
\max_{P_1,\ldots,P_m}\mathrm{vol}_d\!\left(B^d\cap\bigcup_{i=1}^mP_i\right).
```

The conjectured optimum is attained by parallel planks with disjoint interiors whose union is a single plank of width $`W`$ centered at the ball's center. The proposed value is $`\mathrm{vol}_d(B^d\cap\{|x_1|\le W/2\})`$.

## Background

The classical plank theorem concerns complete coverings. Here the width budget is too small for complete coverage, and the objective is covered volume. Different orientations affect both coverage and overlap.

## Known results

Bezdek [2] discusses two-plank, three-dimensional, and some three-plank cases. A lower bound on the width needed for complete coverage does not determine the maximum partial volume.

Bakaev and Polyanskii [3], in a preprint submitted in July 2026, claim a complete affirmative solution for Euclidean balls. The claim has not been independently verified here.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.2. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
2. K. Bezdek. *Tarski's plank problem revisited*. Geometry: Intuitive, Discrete, and Convex, 2013; see also *Classical Topics in Discrete Geometry*, 2010.
3. E. Bakaev, A. Polyanskii. *Optimal partial plank coverings*. [arXiv:2607.27483v1](https://arxiv.org/abs/2607.27483v1), submitted 2026-07-29.
