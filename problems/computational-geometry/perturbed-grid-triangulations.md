# Triangulations of Perturbed Square Grids

**Proposed by:** Peter Brass and Yinyu Ye

Does every tetrahedralization of a small three-dimensional perturbation of an $`n`$-point planar square grid have $`O(n^{3/2})`$ cells?

## Statement

Let $`n=m^2`$ and let $`G_m=\{(i,j,0):1\le i,j\le m\}\subset\mathbb R^3`$. Perturb the points slightly to obtain $`P`$ with no four points coplanar.

For every tetrahedralization $`\mathcal T`$ of the convex hull with vertex set $`P`$ and no added Steiner points, is there a uniform bound

```math
|\mathcal T|\le Cn^{3/2}=Cm^3.
```

The bound concerns every tetrahedralization. The allowed displacement relative to the grid spacing and $`m`$, and the dependence of $`C`$ on that displacement, remain to be fixed.

## Background

Three-dimensional tetrahedralizations of the same point set can vary greatly in size. A near-planar grid combines regular placement with three-dimensional nondegeneracy, testing whether that structure prevents quadratic worst-case size.

## Known results

Edelsbrunner, Preparata, and West [2] give small-tetrahedralization constructions, and Avis and ElGindy [3] study size variation. Existence of one small tetrahedralization does not bound all of them.

The problem chapter [1] also mentions an $`O(n^{5/3})`$ result for grid cubes, a different point configuration.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.3. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
2. H. Edelsbrunner, F. P. Preparata, D. B. West. *Tetrahedrizing point sets in three dimensions*. J. Symbolic Comput. 10, 335–347, 1990.
3. D. Avis, H. ElGindy. *Triangulating point sets in space*. Discrete Comput. Geom. 2, 99–111, 1987.
