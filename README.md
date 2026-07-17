# FORGE Lite

[![Validate](https://github.com/JHY817/Forge-Lite/actions/workflows/validate.yml/badge.svg)](https://github.com/JHY817/Forge-Lite/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/JHY817/Forge-Lite?include_prereleases)](https://github.com/JHY817/Forge-Lite/releases)

> 把通用 Coding Agent 配置成会判断阶段、核对事实、审查方向并产出 PRD 的产品经理工作流 Agent。

FORGE Lite 是一套可配置的产品经理 Agent 工作流与评测框架。它不是独立运行的模型或应用；当它由能读取项目指令、文件和工具的宿主 Agent 加载后，才形成一个可运行的产品经理工作流 Agent 系统。

## 它解决什么

普通的“帮我写 PRD”很容易跳过需求收敛、现状核对和方向判断。FORGE Lite 要求 Agent 先回答：

- 现在处于哪个阶段？
- 哪些信息是事实，哪些只是推断？
- 需要激活哪些模块，哪些应跳过？
- 是否触碰对象模型、归属、权限、生命周期或状态机？
- 当前应自动执行、执行后通知，还是等待用户批准？
- 产物应通过、返工、回退还是沉淀？

```text
需求输入
→ 配置与阶段检查
→ 需求收敛
→ 事实补证
→ 方向门禁
→ 按风险选择 auto / notify / approve
→ 按需准备原型输入
→ PRD 生成
→ Rubric 审计、返工或回退
→ Eval 与经验沉淀
```

## 适合谁

适合：

- 希望 Agent 参与需求判断、方案设计、逆向工程或 PRD 交付的产品经理。
- 有自己的产品文档、代码库、业务 Rubric 或文档模板的团队。
- 使用能够读取项目级指令和本地文件的 Agent 环境。

不适合：

- 只想获得一份不需要事实核对的通用 PRD 模板。
- 期待开箱即用的业务知识库或自动代替产品经理做最终决策。
- 宿主工具无法读取项目指令、文件或执行必要工具。

## 快速开始

需要 Git、Bash 和 Python 3。克隆仓库后执行：

```bash
git clone https://github.com/JHY817/Forge-Lite.git
cd Forge-Lite
bash scripts/setup.sh
python3 scripts/validate-config.py
```

`setup.sh` 会生成本地 `config/` 和 `AGENTS.md`。初次校验预期会告诉你还需填写哪些内容；这是 onboarding，不是安装失败。

最少完成：

1. `config/product-context.md`：产品、用户、核心对象、流程和约束。
2. `config/knowledge-base.yaml`：至少一个可读的事实来源。

然后再次执行：

```bash
python3 scripts/validate-config.py
```

完整步骤见 [QUICKSTART.md](QUICKSTART.md)。

## 第一个任务

```text
请按 FORGE Lite 流程处理下面的需求。
先检查配置和当前阶段，不要直接写 PRD。
请说明需要激活的模块、需要补充的事实和本轮门禁。

需求：
我们希望把一个已有能力开放给新的用户角色。
```

配置完整时，Agent 应先输出类似下面的设计计划，而不是直接生成 PRD：

```text
当前阶段：需求理解 / 产品现状补证
必须模块：需求理解、产品现状、方向门禁
暂不激活：PRD 生成
需要证据：现有角色模型、权限和生命周期
本轮门禁：notify
```

如果配置仍是占位符，Agent 应停在配置引导，明确告诉用户要先补哪些内容。

## 核心能力

| 能力 | 作用 |
|---|---|
| 配置门禁 | 防止在产品背景仍是占位符时继续设计 |
| 需求理解 | 收敛真实问题、用户、场景和本期边界 |
| 产品现状 | 核对已有能力、历史决策和约束 |
| 逆向工程 | 在产品判断依赖代码时检查实现事实 |
| 数据与竞品 | 判断是否需要补充内外部证据 |
| 方向门禁 | 检查对象、归属、权限、生命周期和核心路径 |
| 原型准备 | 向设计或原型工具交付结构化输入并验收输出 |
| PRD 生成 | 把已确认方案转成可评审、可实现、可测试的规格 |
| Loop + Rubric | 判断通过、返工、回退、风险接受或沉淀 |
| Eval | 检查新规则是否真正改善 Agent 行为 |

## 配置与扩展

仓库不包含任何私有业务知识。使用者需在本地配置：

- 产品背景与核心对象
- 知识库和事实来源
- 按需使用的代码库
- 业务专属 Rubric
- 团队文档模板
- 私有经验沉淀

真实配置位于已忽略的 `config/`、`private/` 和 `learning/`，不应提交到公开仓库。详细说明见 [docs/configuration-guide.md](docs/configuration-guide.md)。

## 仓库导航

- [QUICKSTART.md](QUICKSTART.md)：10 分钟安装与首次任务。
- [PROJECT_INDEX.md](PROJECT_INDEX.md)：全部文件与规则归属。
- [docs/concepts.md](docs/concepts.md)：核心概念。
- [docs/collaboration-guide.md](docs/collaboration-guide.md)：人与 Agent 的协作方式。
- [examples/fictional-product/README.md](examples/fictional-product/README.md)：虚构产品示例。
- [evals/README.md](evals/README.md)：行为验证和回归方法。

## 当前边界

- 目前为中文优先的早期版本。
- 它不提供自己的模型、工具运行时或业务知识库。
- 实际能力取决于宿主 Agent 的文件、代码、网络和工具权限。
- 公开 Eval 只覆盖通用回归场景，团队仍需要自己的私有案例。

## 开发与发布检查

```bash
python3 scripts/validate-framework.py
bash scripts/smoke-test-install.sh
bash scripts/check-release.sh
```

贡献说明见 [CONTRIBUTING.md](CONTRIBUTING.md)，安全问题见 [SECURITY.md](SECURITY.md)。

## License

[MIT License](LICENSE)
