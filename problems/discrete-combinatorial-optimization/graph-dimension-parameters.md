# Euclidean, Gram, and Positive Semidefinite Corank Graph Parameters

**Proposed by:** Monique Laurent, Yinyu Ye, and Antonios Varvitsiotis

## Problem

Do Euclidean dimension, Gram dimension, and positive semidefinite corank satisfy the proposed universal equalities for graphs?

## Statement

For a finite simple graph $`G=(V,E)`$, let $`ed(G)`$ be the least dimension in which every realizable set of edge-distance data can be realized. Let $`gd(G)`$ be the least $`k`$ such that every partial Gram matrix specified on diagonal and edge positions and admitting a positive semidefinite completion has a completion of rank at most $`k`$.

Let $`\mathcal C(G)`$ consist of positive semidefinite matrices with zeros at nonedge positions. Define $`\nu^{=}(G)`$ as the largest corank of $`M\in\mathcal C(G)`$ satisfying the Strong Arnold Property: a symmetric matrix $`X`$ with $`MX=0`$ and $`X_{ij}=0`$ at diagonal and edge positions must satisfy $`X=0`$.

Let $`\nabla G`$ be obtained by adding a vertex adjacent to every vertex of $`G`$. Determine whether each inequality holds for all graphs:

```math
ed(\nabla G)\le ed(G)+1,\qquad gd(G)\le\nu^{=}(G).
```

Use consistent conventions for dimension zero, edgeless graphs, and the empty graph; the reverse inequalities depend on those conventions. The two targets are independent.

## Background

Edge distances and partial inner products impose different low-dimensional realization constraints. Comparing them with semidefinite corank connects graph structure, geometry, and low-rank matrix completion.

## Known results

Laurent and Varvitsiotis [3] establish $`ed(\nabla G)=gd(G)`$ and discusses one-sided bounds and low-dimensional characterizations. Together with the reverse inequalities recorded in [4], the proposed inequalities would yield equalities under consistent definitions. Low-dimensional cases alone do not establish the universal statements.

## References

1. M. Belk, R. Connelly. *Realizability of graphs*. Discrete Comput. Geom. 37, 125–137, 2007.
2. H. van der Holst. *Two tree-width-like graph invariants*. Combinatorica 23(4), 633–651, 2003.
3. M. Laurent, A. Varvitsiotis. *A new graph parameter related to bounded rank positive semidefinite matrix completions*. [arXiv:1204.0734](https://arxiv.org/abs/1204.0734); [preprint text](https://arxiv.org/html/1204.0734v1).
4. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
