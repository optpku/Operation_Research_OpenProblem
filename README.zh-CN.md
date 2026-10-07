# 运筹优化开放问题库

[English](README.md) | 简体中文

[![许可证：Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

本项目旨在整理运筹优化各细分领域具有代表性的前沿开放问题，帮助研究者快速了解值得关注和进一步探索的研究方向。目前已收集整理 **16 个问题，并通过专家评审**。每个问题提供明确的问题表述、背景、已有结果和参考来源。

问题库既服务于后续科研探索，也可作为 **AI 科研智能体的真实研究问题来源与评测对象**。项目的长期目标是从问题集合发展为可持续维护的开放研究社区，通过领域负责人与社区协作，持续完善问题、记录进展和组织讨论。

## 研究领域与问题列表

问题按具体研究领域分类。当前覆盖 4 个领域，后续将根据收录的问题拓展运筹优化的其他主要研究方向。

| 研究领域 | 问题数量 | 领域负责人 |
| --- | ---: | --- |
| [凸几何](problems/convex-geometry/) | 7 | 待指定 |
| [离散与组合优化](problems/discrete-combinatorial-optimization/) | 3 | 待指定 |
| [计算几何](problems/computational-geometry/) | 1 | 待指定 |
| [决策过程与博弈](problems/decision-processes-games/) | 5 | 待指定 |

### 凸几何

| ID | 问题 | 研究状态 |
| --- | --- | --- |
| OP-001 | [对踵线段与单纯形](problems/convex-geometry/antipodal-simplices.md) | 未核实 |
| OP-002 | [中心对称凸体中的点](problems/convex-geometry/symmetric-body-points.md) | 未核实 |
| OP-003 | [紧凸集的面](problems/convex-geometry/convex-set-faces.md) | 未核实 |
| OP-004 | [覆盖单位球的板条](problems/convex-geometry/plank-ball-volume.md) | 已有解答声称 |
| OP-005 | [球面与双曲空间中的单纯形和球的相交问题](problems/convex-geometry/non-euclidean-simplex-intersection.md) | 待澄清 |
| OP-006 | [用较小的立方体覆盖单位立方体](problems/convex-geometry/cube-covering.md) | 未核实 |
| OP-009 | [n 维单纯形的内心与欧拉线](problems/convex-geometry/simplex-euler-incenter.md) | 待澄清 |

### 离散与组合优化

| ID | 问题 | 研究状态 |
| --- | --- | --- |
| OP-007 | [布尔二次多面体的体积](problems/discrete-combinatorial-optimization/boolean-quadric-volume.md) | 部分结果 |
| OP-010 | [图的欧氏维数、Gram 维数与半正定余秩](problems/discrete-combinatorial-optimization/graph-dimension-parameters.md) | 未核实 |
| OP-011 | [多色 Carathéodory 猜想](problems/discrete-combinatorial-optimization/multicolored-caratheodory.md) | 相关结果 |

### 计算几何

| ID | 问题 | 研究状态 |
| --- | --- | --- |
| OP-008 | [扰动方格点集的三角剖分](problems/computational-geometry/perturbed-grid-triangulations.md) | 待澄清 |

### 决策过程与博弈

| ID | 问题 | 研究状态 |
| --- | --- | --- |
| OP-012 | [确定性马尔可夫决策过程的 Howard 策略迭代复杂度](problems/decision-processes-games/howard-policy-iteration.md) | 已有解答声称 |
| OP-013 | [确定性轮流行动零和博弈的策略迭代复杂度](problems/decision-processes-games/deterministic-game-strategy-iteration.md) | 待澄清 |
| OP-014 | [折扣马尔可夫博弈的内点算法](problems/decision-processes-games/game-interior-point.md) | 待澄清 |
| OP-015 | [一般折扣马尔可夫决策过程的强多项式算法](problems/decision-processes-games/strongly-polynomial-mdp.md) | 未核实 |
| OP-016 | [折扣因子作为输入的马尔可夫决策过程](problems/decision-processes-games/variable-discount-mdp.md) | 待澄清 |

**评审状态与研究状态分别记录。** 专家评审是收录与整理的审核机制；研究状态用于跟踪后续进展。`Unconfirmed` 表示当前开放性尚待进一步核实，`Needs clarification` 表示表述或适用范围需澄清，`Partial results` 表示已有部分结果，`Related results` 表示已有相关结果，`Solution claimed` 表示已有解答声称、待核验。最新情况以具体问题的正文和参考文献为准。

## 领域负责人机制

每个研究领域设置领域负责人，负责该领域问题的整理、审核与持续维护：

- 维护领域分类、问题列表与元数据，审核并完善社区提交的新问题。
- 跟踪相关研究进展，记录阶段性结果与问题状态变化，注明来源和更新时间。
- 邀请领域专家参与讨论与评审，推动问题表述和背景资料的迭代完善。

领域定义及负责人 GitHub 用户名统一维护于 [`problems/areas.json`](problems/areas.json)。当前负责人尚待指定；问题提出者与领域负责人是不同角色。

## 社区参与与后续建设

目前通过 GitHub Issues 和 Pull Requests 开展协作，逐步形成“提交—讨论—评审—收录—持续更新”的维护流程。

1. **提交题目：** 使用 [问题模板](templates/problem.md)，补充问题表述、背景、已有结果和原始来源，通过 Issue 提议或 PR 提交至对应领域目录。同步在 `problems/catalog.json` 登记唯一 ID、slug、领域、摘要、评审状态、研究状态和更新时间；新提交的问题应标为 `Pending review`，通过评审后再更新。
2. **更新进展：** 提供可核验的论文或证明来源，说明覆盖的假设与范围、仍未解决的部分；通过 PR 更新问题正文、研究状态和日期。解答声称经核验后再更新为已解决，并保留历史记录。
3. **反馈讨论：** 在 Issue 中注明问题 ID，提出表述修正、文献补充、反例或研究思路。领域负责人协调社区反馈并邀请专家评审。

欢迎贡献新领域的问题、认领领域维护工作，以及参与研究进展跟踪。对于 AI 科研智能体评测，应固定仓库版本、明确待解决目标，并记录所用来源、输出结果与专家评价，便于复现与比较。

## 仓库结构

```text
problems/
  areas.json                          # 领域定义与负责人
  catalog.json                        # 问题元数据
  convex-geometry/                     # 凸几何
  discrete-combinatorial-optimization/ # 离散与组合优化
  computational-geometry/              # 计算几何
  decision-processes-games/            # 决策过程与博弈
templates/problem.md                  # 新问题模板
site/                                 # 网站样式与交互脚本
build.py                              # 静态网站生成器
tests/                                # 构建回归测试
docs/                                 # 生成的网站与第三方 KaTeX 资源
```

问题源文件位于 `problems/<area_slug>/<slug>.md`。网站按领域分组，支持全文搜索与领域、研究状态筛选；问题 ID 和已有网站地址保持稳定。

## 许可证

本项目采用 [Apache License 2.0](LICENSE)。第三方组件保留各自许可证，例如 [KaTeX 的 MIT 许可证](docs/vendor/katex/LICENSE)。参考文献及外部链接所指向的论文遵循其各自授权。
