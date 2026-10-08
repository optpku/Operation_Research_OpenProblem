# Markov Decision Processes with an Input Discount Factor

**Proposed by:** Yinyu Ye

Can discounted Markov decision processes with an input discount factor be solved exactly with only logarithmic discount-gap dependence in the arithmetic-operation count?

## Statement

Consider a finite stochastic discounted MDP with $`N`$ states, $`M`$ actions, rational rewards and probabilities, and a common rational input discount $`0<\gamma<1`$. Seek an exact optimal policy with iterations or arithmetic operations bounded by

```math
\mathrm{poly}\!\left(N,M,\log\frac1{1-\gamma}\right).
```

This is different from polynomial time in the complete input bit length. That length also includes rewards, probabilities, and the rational representation of $`\gamma`$; $`\log(1/(1-\gamma))`$ does not describe all those data.

The intended algorithm class and dependencies on reward/probability magnitudes must be specified. The stronger discount-independent operation target is discussed in [Strongly Polynomial Algorithms for MDPs](strongly-polynomial-mdp.md).

## Background

Bit complexity, exact arithmetic-operation counts, and sampling complexity describe different computational models. Distinguishing them identifies what remains beyond ordinary LP solvability.

## Known results

Bellman inequalities give a polynomial-size LP, so polynomial solvability in full input bit length is already available through general LP algorithms [3]. Fixed-discount guarantees [1] do not directly provide the displayed input-discount bound.

Sidford et al. [2] treat approximate policies under a generative model. Its sample-complexity guarantee does not establish the exact arithmetic bound above.

## References

1. Y. Ye. *The simplex and policy-iteration methods are strongly polynomial for the Markov decision problem with a fixed discount rate*. MOR 36(4), 593–603, 2011. [Publication](https://pubsonline.informs.org/doi/abs/10.1287/moor.1110.0516).
2. A. Sidford, M. Wang, X. Wu, L. F. Yang, Y. Ye. *Near-Optimal Time and Sample Complexities for Solving Markov Decision Processes with a Generative Model*. NeurIPS 2018. [arXiv:1806.01492](https://arxiv.org/abs/1806.01492).
3. L. G. Khachiyan. *A polynomial algorithm in linear programming*. Soviet Mathematics Doklady 20, 191–194, 1979.
