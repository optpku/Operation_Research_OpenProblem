# Open Problems in Operations Research and Optimization

English | [简体中文](README.zh-CN.md)

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

This project aims to curate representative frontier open problems across operations research and optimization, helping researchers identify directions worth investigating. The collection currently contains **16 problems that have undergone expert review**. Each entry provides a precise statement, background, known results, and references.

The library supports further research and provides **real research problems for AI research agents to explore and for evaluating their research capabilities**. Our long-term goal is to develop the collection into a research community sustained by area maintainers and community contributors who refine problem statements, record progress, and organize discussions.

## Research Areas and Problems

Problems are organized by research area. The collection currently covers four areas and will expand to other major areas of operations research and optimization as new problems are contributed.

| Research area | Problems | Area maintainers |
| --- | ---: | --- |
| [Convex geometry](problems/convex-geometry/) | 7 | To be appointed |
| [Discrete and combinatorial optimization](problems/discrete-combinatorial-optimization/) | 3 | To be appointed |
| [Computational geometry](problems/computational-geometry/) | 1 | To be appointed |
| [Decision processes and games](problems/decision-processes-games/) | 5 | To be appointed |

### Convex geometry

| ID | Problem | Research status |
| --- | --- | --- |
| OP-001 | [Antipodal Segments and Simplices](problems/convex-geometry/antipodal-simplices.md) | Unconfirmed |
| OP-002 | [Points in a Centrally Symmetric Convex Body](problems/convex-geometry/symmetric-body-points.md) | Unconfirmed |
| OP-003 | [Faces of a Compact Convex Set](problems/convex-geometry/convex-set-faces.md) | Unconfirmed |
| OP-004 | [Planks Covering the Unit Ball](problems/convex-geometry/plank-ball-volume.md) | Solution claimed |
| OP-005 | [Simplex–Ball Intersection in Spherical and Hyperbolic Space](problems/convex-geometry/non-euclidean-simplex-intersection.md) | Needs clarification |
| OP-006 | [Covering a Unit Cube by Smaller Cubes](problems/convex-geometry/cube-covering.md) | Unconfirmed |
| OP-009 | [Incenter on the Euler Line of an n-Simplex](problems/convex-geometry/simplex-euler-incenter.md) | Needs clarification |

### Discrete and combinatorial optimization

| ID | Problem | Research status |
| --- | --- | --- |
| OP-007 | [Volume of the Boolean Quadric Polytope](problems/discrete-combinatorial-optimization/boolean-quadric-volume.md) | Partial results |
| OP-010 | [Euclidean, Gram, and Positive Semidefinite Corank Graph Parameters](problems/discrete-combinatorial-optimization/graph-dimension-parameters.md) | Unconfirmed |
| OP-011 | [A Multicolored Carathéodory Conjecture](problems/discrete-combinatorial-optimization/multicolored-caratheodory.md) | Related results |

### Computational geometry

| ID | Problem | Research status |
| --- | --- | --- |
| OP-008 | [Triangulations of Perturbed Square Grids](problems/computational-geometry/perturbed-grid-triangulations.md) | Needs clarification |

### Decision processes and games

| ID | Problem | Research status |
| --- | --- | --- |
| OP-012 | [Howard's Policy Iteration Complexity for Deterministic MDPs](problems/decision-processes-games/howard-policy-iteration.md) | Solution claimed |
| OP-013 | [Strategy Iteration Complexity for Deterministic Turn-Based Zero-Sum Games](problems/decision-processes-games/deterministic-game-strategy-iteration.md) | Needs clarification |
| OP-014 | [Interior-Point Algorithms for Discounted Markov Games](problems/decision-processes-games/game-interior-point.md) | Needs clarification |
| OP-015 | [Strongly Polynomial Algorithm for General Discounted MDPs](problems/decision-processes-games/strongly-polynomial-mdp.md) | Unconfirmed |
| OP-016 | [Markov Decision Processes with an Input Discount Factor](problems/decision-processes-games/variable-discount-mdp.md) | Needs clarification |

**Review status and research status are recorded separately.** Expert review is part of the process for curating and accepting problems; research status tracks subsequent developments. `Unconfirmed` means the current open status needs further verification; `Needs clarification` indicates that the statement or scope needs clarification; `Partial results` records partial progress; `Related results` indicates relevant existing results; and `Solution claimed` identifies a claimed solution awaiting verification. Consult each problem's text and references for details.

## Area Maintainers

Each research area has designated maintainers responsible for curating, reviewing, and maintaining its problems:

- Maintain area classifications, problem lists, and metadata, and review and refine new community submissions.
- Follow relevant research, record intermediate results and status changes, and keep sources and update dates current.
- Invite experts to join discussions and reviews, and improve problem statements and background material.

Area definitions and maintainers' GitHub usernames are recorded in [`problems/areas.json`](problems/areas.json). Maintainers are currently to be appointed. Problem proposers and area maintainers are distinct roles.

## Community Contributions and Future Development

Collaboration currently takes place through GitHub Issues and pull requests. We aim to establish an ongoing process of submission, discussion, review, acceptance, and updates.

1. **Submit a problem:** Use the [problem template](templates/problem.md) to provide the statement, background, known results, and original sources. Propose the problem in an issue or submit a pull request to the appropriate area directory. Add a corresponding entry to `problems/catalog.json` with a unique ID, slug, area, summary, review status, research status, and update date. Mark new submissions as `Pending review` and update that status after review.
2. **Report progress:** Provide verifiable papers or proofs, explain their assumptions and scope, and identify what remains unresolved. Submit a pull request updating the problem text, research status, and date. Mark a claimed solution as resolved after verification, and preserve the history of updates.
3. **Discuss and give feedback:** Include the problem ID in an issue when proposing corrections, references, counterexamples, or research ideas. Area maintainers coordinate feedback and invite expert review.

Contributions of problems from new areas, volunteers for area maintenance, and updates on research progress are welcome. When evaluating AI research agents, fix the repository version, specify the research target, and record the sources used, outputs, and expert assessments to support reproducibility and comparison.

## Repository Structure

```text
problems/
  areas.json                          # Area definitions and maintainers
  catalog.json                        # Problem metadata
  convex-geometry/                     # Convex geometry
  discrete-combinatorial-optimization/ # Discrete and combinatorial optimization
  computational-geometry/              # Computational geometry
  decision-processes-games/            # Decision processes and games
templates/problem.md                  # New problem template
site/                                 # Website styles and interaction scripts
build.py                              # Static website generator
tests/                                # Build regression tests
docs/                                 # Generated website and third-party KaTeX assets
```

Problem sources are stored at `problems/<area_slug>/<slug>.md`. The website groups problems by area and supports full-text search and filtering by area and research status. Problem IDs and existing website URLs remain stable.

## License

This project is licensed under the [Apache License 2.0](LICENSE). Third-party components retain their own licenses, including [KaTeX's MIT license](docs/vendor/katex/LICENSE). Referenced papers and other materials linked from the library are subject to their respective licenses.
