# FORGE Lite

> 可配置的 AI 产品经理工作流 Agent 框架。  
> A configurable AI product-management workflow agent framework.

FORGE Lite 是一套面向产品经理的通用 Agent 工作流框架。

它的目标不是“帮你快速套一个 PRD 模板”，而是让 AI 按产品工作的真实链路推进：

```text
需求输入
→ 问题收敛
→ 事实补证
→ 方案判断
→ 用户确认
→ 原型准备
→ PRD 生成
→ 审计返工
→ 经验沉淀
```

这套框架不绑定任何公司、任何产品、任何代码库。使用者需要自己配置产品背景、知识库、代码库和业务 Rubric。

## 这是什么

FORGE Lite 是一个“产品经理数字化分身”的通用骨架。

它帮助 Agent 判断：

- 现在任务处在哪个阶段。
- 是否应该先收敛需求，而不是直接写 PRD。
- 是否需要查产品现状、代码逻辑、数据或竞品。
- 是否触碰对象模型、权限、生命周期、状态机等方向问题。
- 是否应该进入方案设计。
- 是否需要先准备原型设计输入。
- PRD 是否可以生成。
- 产物是否需要审计、返工、回退或沉淀。

## 这不是什么

FORGE Lite 不是：

- 固定 PRD 模板。
- 某个公司的内部工作流。
- 某个产品的脱敏版规范。
- 可以直接替代产品经理判断的自动化机器。
- 内置业务知识库的完整 Agent。

## 核心流程

```text
需求输入
→ 判断任务类型和阶段
→ 检查已有事实和上下文
→ 判断需要激活哪些模块
→ 输出设计计划并让人确认
→ 按需做现状理解 / 逆向工程 / 数据判断 / 竞品分析
→ 进入方案设计
→ 方向确认
→ 按需进入原型准备
→ 生成 PRD
→ 审计、返工、回退或沉淀
```

## 核心模块

| 模块 | 作用 |
|---|---|
| 需求理解 | 收敛真实问题、目标用户、关键场景和本期边界 |
| 产品现状理解 | 查清已有产品行为、文档、历史决策和约束 |
| 逆向工程 | 当产品逻辑依赖代码时，检查实现事实 |
| 数据分析判断 | 判断是否需要补数据，以及数据能支持什么结论 |
| 竞品分析 | 针对具体产品问题做外部参照 |
| 方案设计 | 形成推荐方向、取舍、风险和待确认点 |
| 原型设计准备 | 为设计或原型工具准备结构化输入 |
| PRD 生成 | 把已确认方案转成可交付的产品需求 |
| 审计与沉淀 | 检查产物质量，决定返工、回退或沉淀经验 |

## 使用前需要配置什么

FORGE Lite 默认不包含任何私有业务信息。你需要自己配置：

- 产品背景
- 用户角色
- 核心对象
- 关键业务流程
- 知识库位置
- 代码库位置
- 团队自己的功能逻辑 Rubric
- PRD 模板偏好
- 本地经验沉淀目录

配置示例在：

```text
config.example/
```

## 目录说明

```text
forge-lite/
├── README.md                    # 项目介绍
├── AGENTS.template.md            # Agent 指令模板
├── config.example/               # 配置示例
├── workflows/                    # 工作流
├── modules/                      # 能力模块
├── rubrics/                      # 通用检查标准
├── templates/                    # 文档模板
├── examples/                     # 虚构示例
└── docs/                         # 使用说明和开源注意事项
```

## 快速开始

如果你刚 clone 这个项目，先看：

```text
QUICKSTART.md
```

最短路径：

1. 运行 `bash scripts/setup.sh`，生成本地 `config/`。
2. 脚本会同时生成本地 `AGENTS.md`。
3. 填写 `config/product-context.md`。
4. 填写 `config/knowledge-base.yaml`。
5. 按需填写 `config/codebase.yaml`。
6. 按需填写 `config/rubric.yaml`。
7. 按需填写 `config/templates.yaml`，替换为你的团队 PRD 模板。
8. 让 Agent 先输出设计计划，不要直接写 PRD。

发布前本地检查：

```bash
bash scripts/check-release.sh
```

不同任务入口：

- 从需求到 PRD：`workflows/end-to-end-prd.md`
- 单点分析任务：`workflows/single-module-task.md`
- 审 PRD 或方案：`workflows/review-and-retrospective.md`

## 开源边界

这个仓库可以公开：

- 通用架构
- 通用流程
- 通用模块
- 通用 Rubric
- 通用模板
- 虚构示例

这个仓库不应该公开：

- 真实业务知识库
- 内部代码库路径
- 具体功能逻辑
- 真实 PRD
- 真实客户案例
- 私有经验沉淀
- 公司专属设计规范

## 当前状态

这是早期草案。当前正文以中文为主，方便先把方法论讲清楚。后续如果真的发布到 GitHub，可以逐步补英文版 README 和英文文档。

## License

本项目使用 MIT License。

如果你在自己的项目里复用或修改，请保留 `LICENSE` 中的版权和许可声明。
