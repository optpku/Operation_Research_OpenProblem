# A Multicolored Carathéodory Conjecture

## Problem

Can an origin-containing transversal also have distinct row labels within every color class?

## Statement

For each integer $`r\ge2`$, does there exist $`N_0(r)`$ such that the following holds for every $`N\ge N_0(r)`$?

Let $`P_{ij}\in\mathbb R^N`$ for $`1\le i\le r`$ and $`1\le j\le N+1`$, with

```math
0\in\mathrm{conv}\{P_{1j},\ldots,P_{rj}\}.
```

Partition the column indices as $`C_1\uplus\cdots\uplus C_m=\{1,\ldots,N+1\}`$ with $`|C_\ell|\le r-1`$. Must there be row labels $`k_j\in\{1,\ldots,r\}`$ satisfying

```math
0\in\mathrm{conv}\{P_{k_1,1},\ldots,P_{k_{N+1},N+1}\},
```

and $`k_a\ne k_b`$ whenever distinct columns $`a,b`$ belong to the same color class?

Both the convex-hull and label constraints are required. A counterexample at one fixed $`N`$ does not refute a statement for all sufficiently large $`N`$.

## Background

The colorful Carathéodory theorem supplies origin-containing transversals without this additional label constraint. The conjecture combines convex selection with a coupled combinatorial assignment condition.

## Known results

Blagojević, Matschke, and Ziegler [3] prove related colored Tverberg results for prime parameters. Jojić, Panina, and Živaljević [4] treat prime powers and associated color models. Their hypotheses must be compared with the exact threshold and color constraints above.

The problem chapter [1] highlights $`r=4,N=9`$, but that instance is not the full asymptotic conjecture.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.9. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
2. I. Bárány. *Quadratically many colorful simplices*. SIAM J. Discrete Math. 24, 191–198, 2010.
3. P. V. M. Blagojević, B. Matschke, G. M. Ziegler. *Optimal bounds for the colored Tverberg problem*. JEMS 17, 739–754, 2015. [arXiv:0910.4987](https://arxiv.org/abs/0910.4987).
4. D. Jojić, G. Panina, R. T. Živaljević. *Optimal colored Tverberg theorems for prime powers*. [arXiv:2005.11913v3](https://arxiv.org/abs/2005.11913v3).
