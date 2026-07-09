# 快速上手

目标：让你 clone 这个仓库后，在 10 分钟内完成基础配置，并让 Agent 能按 FORGE Lite 流程开始工作。

## 1. 复制配置文件

在仓库根目录执行：

```bash
bash scripts/setup.sh
```

它会把：

```text
config.example/
```

复制为：

```text
config/
```

同时它会把：

```text
AGENTS.template.md
```

复制为本地使用的：

```text
AGENTS.md
```

如果你不想运行脚本，也可以手动复制。

## 2. 填写产品背景

编辑：

```text
config/product-context.md
```

至少填写：

- 产品名称
- 产品类型
- 目标用户
- 核心对象
- 关键流程
- 已知约束

如果这一步不填，Agent 很容易给出泛泛建议。

## 3. 配置知识库

编辑：

```text
config/knowledge-base.yaml
```

把你的产品文档、帮助文档、设计文档、历史 PRD 等来源填进去。

可以先只配置一个本地文档目录。

## 4. 配置代码库

编辑：

```text
config/codebase.yaml
```

如果你的任务需要逆向工程，就配置相关代码库。

如果暂时不需要代码分析，可以先保留占位，并在使用时告诉 Agent 跳过逆向工程。

## 5. 配置业务 Rubric

编辑：

```text
config/rubric.yaml
```

公开仓库只提供通用 Rubric。  
你的业务专属检查项应该放到私有文件里，再在这里配置路径。

## 6. 配置 PRD 等文档模板

编辑：

```text
config/templates.yaml
```

默认会使用仓库里的通用模板：

```text
templates/prd.md
```

如果你有自己的团队 PRD 模板，可以把 `config/templates.yaml` 里的 `prd.path` 改成你的模板路径。

## 7. 复制 Agent 指令模板

如果你已经运行过 `bash scripts/setup.sh`，这一步已经自动完成。

如果你要手动部署，把：

```text
AGENTS.template.md
```

复制到你的 Agent 工作区，并改名为：

```text
AGENTS.md
```

然后按你的工具要求加载它。

## 8. 让 Agent 跑第一个任务

你可以这样对 Agent 说：

```text
请按 FORGE Lite 流程处理这个需求。
先不要直接写 PRD，先判断任务阶段、需要哪些模块、需要补哪些事实，然后输出设计计划让我确认。

需求：
我们希望把一个已有能力开放给新的用户角色，看看应该怎么设计。
```

Agent 应该先输出设计计划，而不是直接生成 PRD。

## 9. 判断是否跑通

如果流程跑通，Agent 至少应该做到：

- 识别这是产品设计任务。
- 不直接写 PRD。
- 先判断任务阶段。
- 输出需要激活的模块。
- 说明是否需要方向门禁。
- 明确需要哪些产品事实、代码事实或用户确认。

如果 Agent 直接开始写 PRD，说明指令没有正确加载，或项目上下文不足。

## 10. 发布前检查

如果你准备把仓库推到 GitHub，先运行：

```bash
bash scripts/check-release.sh
```

它会检查：

- GitHub 必备文件是否存在。
- 核心流程文件是否存在。
- 是否还有 `.DS_Store`。

然后再按 `RELEASE_CHECKLIST.md` 做人工复查。
