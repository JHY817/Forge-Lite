# 运行状态协议

> 定义阶段状态、合法迁移、回退失效和跨任务恢复规则。模块执行细节仍由对应模块负责。

## 阶段状态

| 状态 | 含义 | 可进入下一阶段 |
|---|---|---|
| `not_started` | 尚未开始 | 否 |
| `in_progress` | 正在执行 | 否 |
| `agent_review_failed` | Agent 审计未通过 | 否 |
| `agent_review_passed` | Agent 审计通过，尚未完成必要门禁 | 取决于门禁 |
| `waiting_user_confirmation` | 等待必须的用户确认 | 否 |
| `confirmed` | 必要用户确认已完成 | 是 |
| `blocked` | 缺少不可替代的事实、权限或外部条件 | 否 |
| `superseded` | 因回退或新结论失效 | 否 |
| `completed` | 阶段和交接均已完成 | 是 |

“基本完成”“原则可行”“大致确认”不是合法状态。

## 合法迁移

```text
not_started → in_progress
in_progress → agent_review_failed / agent_review_passed / blocked
agent_review_failed → in_progress / blocked
agent_review_passed → completed / waiting_user_confirmation
waiting_user_confirmation → confirmed / in_progress / blocked
confirmed → completed
blocked → in_progress
任意已产出状态 → superseded
```

不得把用户未回复视为确认。

## 阶段迁移记录

```text
stage:
from_status:
to_status:
trigger:
rubric_result:
evidence:
invalidated_artifacts:
next_action:
gate: auto / notify / approve
updated_at:
```

记录可直接写入当前状态文件，不要求每一步单独建文档。

## 回退与下游失效

以下变化会使相关下游产物失效：

- 核心问题或本期范围变化；
- 对象模型、归属、权限或生命周期变化；
- 核心用户路径变化；
- 决定方案的关键事实被推翻；
- 已确认方向被否决；
- PRD 细化暴露方向结构不可持续。

回退时必须指定根因阶段、目标阶段、仍有效事实、失效产物和下一步。方向、范围或关键事实变化后，下游必须全量重审，不能只复查旧问题。

## 强制更新当前状态的事件

- 范围或方向确认；
- 阶段 Rubric 通过或失败；
- 用户确认方案或接受风险；
- 主产物被替换；
- 阶段回退；
- 产物失效；
- 任务阻塞、中断或完成。

历史项目没有状态文件时先形成状态草案；如果主产物冲突，标记 `blocked` 或 `waiting_user_confirmation`，不能自行选择最方便的一版。
