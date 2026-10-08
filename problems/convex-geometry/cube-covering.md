# Covering a Unit Cube by Smaller Cubes

**Proposed by:** Włodzimierz Kuperberg and Yinyu Ye

How many cubes of edge length strictly less than one are needed to cover a unit cube when rotations are allowed?

## Statement

For an integer $`n\ge2`$, let $`C=[0,1]^n`$ and define

```math
q(n)=\min\{m:C\subseteq\bigcup_{i=1}^m(a_i+R_i[0,\ell_i]^n),\quad 0<\ell_i<1,\ R_i\in O(n)\}.
```

The covering cubes may have different edge lengths, independent translations and rotations, and may extend outside $`C`$. Determine $`q(n)`$ for general $`n`$.

## Background

Free orientations can cover corners and boundary regions differently from coordinate-aligned subdivisions. The difficulty is to control the entire target boundary and to exclude all arrangements with fewer cubes.

## Known results

The problem chapter [1] records $`q(2)=3`$ and $`q(n)\le n+1`$. The stricter axis-parallel or homothetic model requires $`2^n`$ cubes, which is not a lower bound for freely rotated coverings.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.6. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
