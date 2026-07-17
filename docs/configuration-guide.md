# 配置说明

FORGE Lite 是通用框架，本身不包含任何真实产品知识。  
要让它真正可用，需要把你自己的产品上下文配置进去。

## 1. 复制配置示例

把：

```text
config.example/
```

复制成：

```text
config/
```

`config/` 默认会被 `.gitignore` 忽略，不建议提交到 GitHub。

推荐直接运行：

```bash
bash scripts/setup.sh
python3 scripts/validate-config.py
```

初次校验会列出尚未替换的占位符。必需配置未通过前，Agent 应保持在配置引导阶段。

## 2. 配置产品背景

编辑：

```text
config/product-context.md
```

建议填写：

- 产品名称
- 产品类型
- 目标用户
- 主要用户角色
- 核心对象
- 关键业务流程
- 重要生命周期
- 当前产品原则
- 明确不做什么

## 3. 配置知识库

编辑：

```text
config/knowledge-base.yaml
```

可以配置：

- 产品帮助文档
- 内部需求文档
- 设计规范
- 公开文档
- 历史方案

注意：

- 公开仓库里只放示例。
- 真实路径不要提交。
- 不能访问的知识源要明确标记，不能靠猜。

## 4. 配置代码库

编辑：

```text
config/codebase.yaml
```

可以配置：

- 前端仓库
- 后端仓库
- 服务仓库
- 文档仓库

FORGE Lite 的原则是：

- 代码事实和产品决策分开。
- 能查代码就不要猜现状。
- 不做大范围无目标扫仓。
- 不把真实代码库路径提交到公开仓库。

## 5. 配置 Rubric

编辑：

```text
config/rubric.yaml
```

公开仓库里的 Rubric 只保留通用检查项。  
具体业务 Rubric 应该放在私有配置里。

例如：

- 通用对象模型检查可以公开。
- 某个产品的具体权限规则不要公开。
- 某次真实返工沉淀出来的业务细则不要公开。

## 6. 配置文档模板

编辑：

```text
config/templates.yaml
```

可以配置：

- 设计计划模板
- 当前状态模板
- 方案设计模板
- 原型设计 Brief 模板
- PRD 模板

如果团队已经有自己的 PRD 模板，可以把 `prd.path` 指向你的私有模板。

## 7. 配置本地经验沉淀

如果你希望记录长期经验，可以创建：

```text
learning/
```

建议：

- `learning/` 不提交到 GitHub。
- 经验沉淀写入前先确认。
- 能通用化的经验，后续再考虑抽象进公开 Rubric。

## 8. 推荐配置顺序

```text
product-context.md
→ knowledge-base.yaml
→ codebase.yaml
→ rubric.yaml
→ templates.yaml
→ 本地模板
→ 本地经验沉淀
```

先让 Agent 知道“这是个什么产品”，再让它知道“去哪里查事实”。

## 9. 配置通过标准

- `product-context.md` 不再包含 `<...>` 占位符。
- `knowledge-base.yaml` 至少有一个非占位的知识源。
- 需要逆向工程时，`codebase.yaml` 中目标仓库路径真实可读。
- 私有 Rubric 或模板尚未配置时，Agent 应显式标注并使用公开默认值，不伪造团队规则。
