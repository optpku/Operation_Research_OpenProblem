# OpenProblems

A collection of 16 mathematical problems in geometry, combinatorial optimization, and decision processes. Each problem includes a precise statement, background, related results, and references.

## Problems

| ID | Problem | Area | Status |
| --- | --- | --- | --- |
| [OP-001](problems/antipodal-simplices.md) | Antipodal Segments and Simplices | Convex geometry | Unconfirmed |
| [OP-002](problems/symmetric-body-points.md) | Points in a Centrally Symmetric Convex Body | Convex geometry | Unconfirmed |
| [OP-003](problems/convex-set-faces.md) | Faces of a Compact Convex Set | Convex geometry | Unconfirmed |
| [OP-004](problems/plank-ball-volume.md) | Planks Covering the Unit Ball | Convex geometry | Solution claimed |
| [OP-005](problems/non-euclidean-simplex-intersection.md) | Simplex–Ball Intersection in Spherical and Hyperbolic Space | Convex geometry | Needs clarification |
| [OP-006](problems/cube-covering.md) | Covering a Unit Cube by Smaller Cubes | Convex geometry | Unconfirmed |
| [OP-007](problems/boolean-quadric-volume.md) | Volume of the Boolean Quadric Polytope | Discrete and combinatorial optimization | Partial results |
| [OP-008](problems/perturbed-grid-triangulations.md) | Triangulations of Perturbed Square Grids | Computational geometry | Needs clarification |
| [OP-009](problems/simplex-euler-incenter.md) | Incenter on the Euler Line of an n-Simplex | Convex geometry | Needs clarification |
| [OP-010](problems/graph-dimension-parameters.md) | Euclidean, Gram, and Positive Semidefinite Corank Graph Parameters | Discrete and combinatorial optimization | Unconfirmed |
| [OP-011](problems/multicolored-caratheodory.md) | A Multicolored Carathéodory Conjecture | Discrete and combinatorial optimization | Related results |
| [OP-012](problems/howard-policy-iteration.md) | Howard's Policy Iteration Complexity for Deterministic MDPs | Decision processes and games | Solution claimed |
| [OP-013](problems/deterministic-game-strategy-iteration.md) | Strategy Iteration Complexity for Deterministic Turn-Based Zero-Sum Games | Decision processes and games | Needs clarification |
| [OP-014](problems/game-interior-point.md) | Interior-Point Algorithms for Discounted Markov Games | Decision processes and games | Needs clarification |
| [OP-015](problems/strongly-polynomial-mdp.md) | Strongly Polynomial Algorithm for General Discounted MDPs | Decision processes and games | Unconfirmed |
| [OP-016](problems/variable-discount-mdp.md) | Markov Decision Processes with an Input Discount Factor | Decision processes and games | Needs clarification |

## Files

- `problems/`: problem text and `catalog.json` for titles, areas, and status.
- `templates/problem.md`: template for a new problem.
- `site/` and `build.py`: website styles, search, and page generation.
- `docs/`: the published website.

## Build locally

```bash
python3 -m pip install -r requirements.txt
python3 build.py
python3 -m http.server 8098 --directory docs
```

Open `http://localhost:8098`. After editing a problem, rebuild the site and commit both the problem text and generated pages. To publish the website, enable GitHub Pages with GitHub Actions as the source in the repository settings. The workflow publishes `docs/` when changes are pushed to `main`.
