# Incenter on the Euler Line of an n-Simplex

**Proposed by:** Horst Martini and Yinyu Ye

## Problem

Characterize higher-dimensional simplices whose incenter lies on the line through the circumcenter and centroid.

## Statement

Let $`T=\mathrm{conv}\{v_0,\ldots,v_n\}\subset\mathbb R^n`$ be a nondegenerate simplex with $`n\ge3`$. Write $`C`$ for the circumcenter, $`G=(n+1)^{-1}\sum_iv_i`$ for the centroid, and $`I`$ for the incenter. If $`C\ne G`$, define

```math
L(T)=\{C+t(G-C):t\in\mathbb R\}.
```

Find necessary and sufficient geometric conditions for $`I\in L(T)`$ for general simplices.

If $`C=G`$, these centers do not determine a unique line. This case requires a separate convention and should be included in the characterization. General simplices need not be orthocentric.

## Background

The incenter is determined by distances to faces, the circumcenter by distances to vertices, and the centroid by vertex averaging. Their collinearity relates different aspects of simplex geometry.

## Known results

Edmonds, Hajja, and Martini [2] treat orthocentric simplices and relates the incenter-on-Euler-line property to biregularity: vertices split into two regular simplices with equal cross-group edge lengths. This is a special-class result, not a characterization of all simplices.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.8. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
2. A. E. Edmonds, M. Hajja, H. Martini. *Orthocentric Simplices and Biregularity*. Results Math. 52, 41–50, 2008. [Publication](https://link.springer.com/article/10.1007/s00025-008-0294-4).
