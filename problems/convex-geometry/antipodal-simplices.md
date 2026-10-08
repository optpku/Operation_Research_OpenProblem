# Antipodal Segments and Simplices

**Proposed by:** Imre Bárány, Yinyu Ye, Endre Makai, Jr., Horst Martini, and Valeriu Soltan

Is the size of a pairwise antipodal family of segments or $`k`$-simplices in $`\mathbb R^d`$ at most $`2^{d-k}`$?

## Statement

Let $`S_k`$ be a finite family of nondegenerate $`k`$-simplices in $`\mathbb R^d`$, and let $`P=\mathrm{conv}(\bigcup_{s\in S_k}s)`$. For every distinct pair $`s_i,s_j`$, assume there are distinct parallel supporting hyperplanes $`H_i,H_j`$ of $`P`$ such that $`s_i\subset H_i`$ and $`s_j\subset H_j`$. The hyperplanes may depend on the pair.

Determine whether both assertions hold:

1. For segments ($`k=1`$), $`|S_1|\le2^{d-1}`$.
2. For $`1\le k\le d-2`$, $`|S_k|\le2^{d-k}`$.

Containment in a supporting hyperplane does not require equality with the supporting face.

## Background

The Danzer–Grünbaum theorem bounds an antipodal point set by $`2^d`$. Replacing points with positive-dimensional objects asks whether the bound decreases systematically with the dimension of each object. Pair-dependent supporting directions make a direct coordinatewise argument difficult.

## Known results

The problem chapter [1] records at most four antipodal segments in dimension three and at most two objects when $`k=d-1`$. Parallel edges or simplices in parallel faces of a parallelotope attain the conjectured sizes, showing sharpness if the bounds hold.

Makai–Martini [3] discusses related antipodality questions. Bounds on the number of strictly antipodal point pairs concern a different quantity.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.1. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
2. L. Danzer, B. Grünbaum. *Über zwei Probleme bezüglich konvexer Körper von P. Erdős und V. L. Klee*. Math. Z. 79, 95–99, 1962.
3. E. Makai, Jr., H. Martini. *On the number of antipodal or strictly antipodal pairs of points in finite subsets of Rᵈ*. [Related paper in the author archive](https://users.renyi.hu/~makai/antipod2.pdf).
4. B. Grünbaum. *Convex Polytopes*. Wiley-Interscience, 1967.
