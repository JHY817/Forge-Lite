# 规则唯一来源

| 规则类型 | 唯一完整定义位置 | 其他位置允许内容 |
|---|---|---|
| 项目角色、硬约束、路由 | `AGENTS.md`（由模板生成） | 不适用 |
| 运行状态与迁移 | `workflows/runtime-state.md` | 仅引用触发点 |
| 上下文与事实分级 | `workflows/context-and-evidence.md` | 模块只写特殊输入 |
| 用户门禁与受控并行 | `workflows/approval-and-parallelism.md` | 只标注本阶段门禁 |
| 端到端、单模块、审计编排 | `workflows/` 对应流程 | Agent 模板只负责路由 |
| 模块内部执行 | `modules/` 对应模块 | 流程不复制执行细节 |
| 阶段和产物质量 | `rubrics/` | 模块只引用，不复制判定表 |
| 当前任务事实 | 使用者项目中的 `current-state.md` | 历史文档不能覆盖 |
| Agent 行为验证 | `evals/` | 经验记录不能冒充评测 |

完整规则只保留一处。其他文件可以解释如何使用，但不能形成第二套达标条件。冲突时先修正唯一来源，不由 Agent 临场调和。
