# Points in a Centrally Symmetric Convex Body

**Proposed by:** Zsolt Langi and Yinyu Ye

Does every centrally symmetric convex body in dimension $`n\ge3`$ contain $`2n`$ points at pairwise distance at least $`\sqrt2`$ in its own norm?

## Statement

Let $`C\subset\mathbb R^n`$ be compact and convex, with nonempty interior and $`C=-C`$. Define

```math
\|x\|_C=\inf\{t>0:x\in tC\}.
```

For every $`n\ge3`$ and every integer $`n+2\le k\le2n`$, must there exist $`p_1,\ldots,p_k\in C`$ such that

```math
\|p_i-p_j\|_C\ge\sqrt2\qquad(1\le i<j\le k)?
```

It is enough to prove the case $`k=2n`$, since smaller configurations can be obtained by taking subsets. The distance is measured in the norm induced by $`C`$, not necessarily in the Euclidean norm.

## Background

The question compares finite packing in Euclidean and general normed spaces. Central symmetry defines a norm, but provides much less structure than the rotational symmetry of a Euclidean ball.

## Known results

For the Euclidean unit ball, $`\{\pm e_1,\ldots,\pm e_n\}`$ gives $`2n`$ points with the required separation. Rankin [1] studies the corresponding spherical-code problem.

Doyle, Lagarias, and Randall [2] give the related planar self-packing result with four separated points. The question here concerns arbitrary centrally symmetric bodies in dimensions at least three.

## References

1. R. A. Rankin. *The closest packing of spherical caps in n dimensions*. Proc. Glasgow Math. Assoc. 2, 139–144, 1955. [Publication](https://doi.org/10.1017/S2040618500033219).
2. P. G. Doyle, J. C. Lagarias, D. Randall. *Self-packing of centrally symmetric convex bodies in R²*. Discrete & Computational Geometry 8, 171–189, 1992. [DOI](https://doi.org/10.1007/BF02293042); [author bibliography](https://websites.umich.edu/~lagarias/PUBLICATIONS/tilings.html).
3. J. Aczél. *Solution to Problem 35* (in Hungarian). Mat. Lapok 3, 94–95, 1952.
