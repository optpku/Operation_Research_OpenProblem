# Faces of a Compact Convex Set

## Problem

Can every point of a compact convex set be represented using faces with prescribed individual dimension bounds?

## Statement

Let $`K\subset\mathbb R^n`$ be a nonempty compact convex set. Let positive integers $`n_1,\ldots,n_s`$ satisfy $`\sum_{i=1}^s n_i=n+1`$. For every $`z\in K`$, do there exist nonempty faces $`F_1,\ldots,F_s`$ such that

```math
z\in\mathrm{conv}(F_1\cup\cdots\cup F_s),\qquad \dim F_i\le n_i-1\quad(1\le i\le s)?
```

A face has the usual convex-analysis meaning: if the relative interior of a segment in $`K`$ meets $`F`$, both endpoints lie in $`F`$. The improper face $`K`$ is allowed; faces need not be exposed. Dimension means affine dimension, and $`K`$ need not be full-dimensional.

## Background

Extreme-point representations use zero-dimensional faces. This problem allows higher-dimensional faces but assigns a separate dimension budget to each, connecting convex representations with the face structure of the set.

## Known results

The problem chapter [1] states the polytopal case. If $`s=1`$, take $`F_1=K`$. If every $`n_i=1`$, the question reduces to representation by extreme points. Mixed dimension budgets for general compact convex sets are the remaining target.

Soltan's slides [2] discuss related face-representation results.

## References

1. K. Bezdek, A. Deza, Y. Ye. *Selected Open Problems in Discrete Geometry and Optimization*, 2013, §1.10, Conjecture 2. [Chapter](https://www.cas.mcmaster.ca/~deza/fic2013b.pdf).
2. V. Soltan. *Carathéodory-type Results for Faces of Convex Sets*. Talk on joint work with Jim Lawrence. [Fields Institute slides](https://www.fields.utoronto.ca/talk-media/1/85/64/slides.pdf).
