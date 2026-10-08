# Volume of the Boolean Quadric Polytope

**Proposed by:** Jon Lee and Yinyu Ye

Find an exact volume formula, or improved bounds, for the Boolean quadric polytope of the complete graph.

## Statement

For $`n\ge2`$, set $`d=n(n+1)/2`$ and define

```math
P_n=\mathrm{conv}\{(x,y)\in\mathbb R^d:x\in\{0,1\}^n,\ y_{ij}=x_ix_j\ (1\le i<j\le n)\}.
```

Determine $`\mathrm{vol}_d(P_n)`$, or proved bounds $`a_n,b_n`$ with $`0<a_n\le\mathrm{vol}_d(P_n)\le b_n`$. The volume is ordinary $`d`$-dimensional Lebesgue volume in these coordinates, not volume multiplied by $`d!`$.

The graph is $`K_n`$; the formula or bounds should hold for all $`n`$.

## Background

The Boolean quadric polytope linearizes binary quadratic products. Comparing its volume with relaxation volumes measures the extra geometric region introduced by relaxation.

## Known results

The standard relaxation $`Q_n`$ is defined, for every $`i<j`$, by

```math
y_{ij}\ge0,\quad y_{ij}\le x_i,\quad y_{ij}\le x_j,\quad x_i+x_j\le1+y_{ij}
```

Ko, Lee, and Steingrímsson [1] give the relaxation-volume formula

```math
\mathrm{vol}_d(Q_n)=\frac{2^{2n-d}n!}{(2n)!}.
```

Since $`P_n\subseteq Q_n`$, this supplies an upper bound.

Lee and Skipper [2] study sparse-graph relaxation volumes. Lee [3] claims exact volume computation for series-parallel graphs. General $`K_n`$ with $`n\ge4`$ is not series-parallel, so that result does not cover the general complete-graph problem.

## References

1. C.-W. Ko, J. Lee, E. Steingrímsson. *The volume of relaxed Boolean-quadric and cut polytopes*. Discrete Mathematics 163, 293–298, 1997. [Publication](https://www.sciencedirect.com/science/article/pii/0012365X9500343U).
2. J. Lee, D. Skipper. *Volume computation for sparse boolean quadric relaxations*. [arXiv:1703.02444v4](https://arxiv.org/abs/1703.02444v4).
3. J. Lee. *Exact volume computation for Boolean quadric polytopes of series-parallel graphs*. [arXiv:2610.00734v1](https://arxiv.org/abs/2610.00734v1), submitted 2026-09-30.
4. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.7. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
