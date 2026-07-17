# 10 分钟快速上手

目标：从全新 Clone 到让宿主 Agent 按 FORGE Lite 流程处理第一个产品任务。

## 1. 准备环境

需要：

- Git
- Bash
- Python 3.10 或更高版本
- 能够读取项目级指令和本地文件的 Agent 环境

FORGE Lite 本身不安装模型，也不提供独立的 Agent 运行时。

## 2. Clone 与初始化

```bash
git clone https://github.com/JHY817/Forge-Lite.git
cd Forge-Lite
bash scripts/setup.sh
```

安装脚本会：

- 把 `config.example/` 复制为已忽略的本地 `config/`。
- 把 `AGENTS.template.md` 复制为已忽略的本地 `AGENTS.md`。
- 保留已经存在的配置，重复执行不会覆盖。

## 3. 检查配置状态

```bash
python3 scripts/validate-config.py
```

刚安装时，校验器会返回“需要配置”并列出占位项。这说明配置门禁正常工作。

默认命令会输出 `CONFIG_STATUS=needs_configuration` 但保持正常退出，便于 Agent 继续向用户说明下一步。CI 或自动化脚本可使用 `python3 scripts/validate-config.py --strict` 把配置未完成视为非零退出。

## 4. 填写必需配置

先完成 `config/product-context.md`：

- 产品名称和类型
- 目标用户和核心任务
- 核心对象和角色
- 关键流程和生命周期
- 已知约束和非目标

再完成 `config/knowledge-base.yaml`，至少提供一个 Agent 能够读取的事实来源。

## 5. 按需配置

- `config/codebase.yaml`：只有任务需要代码逆向时才必须。
- `config/rubric.yaml`：放置你的私有产品逻辑和表达规范。
- `config/templates.yaml`：可以继续使用默认模板，也可指向团队私有模板。

再次检查：

```bash
python3 scripts/validate-config.py
```

必需配置通过后，产品设计任务才可以继续。

## 6. 让宿主 Agent 加载指令

默认安装生成 `AGENTS.md`。如果你的 Agent 工具使用不同的项目指令文件名，请按工具要求复制或引用 `AGENTS.md`，不要维护两套不同规则。

## 7. 执行第一个任务

```text
请按 FORGE Lite 流程处理下面的需求。
先检查配置和当前阶段，不要直接写 PRD。

需求：
我们希望把一个已有能力开放给新的用户角色，请判断需要核对哪些现状，以及是否应该进入 PRD。
```

## 8. 判断是否跑通

配置不完整时，Agent 应：

- 明确进入配置引导。
- 指出哪些必需文件还是占位符。
- 不把占位符当成产品事实。
- 不直接进入方案或 PRD。

配置完整时，Agent 应：

- 识别任务类型和当前阶段。
- 说明需要激活和跳过的模块。
- 区分产品事实、用户陈述、推断和待确认项。
- 检查是否命中方向门禁。
- 输出设计计划和 auto / notify / approve 判断。
- 在方向未确认前不生成 PRD。

## 9. 本地自检

```bash
python3 scripts/validate-framework.py
bash scripts/smoke-test-install.sh
bash scripts/check-release.sh
```

如果你要替换模板或扩展 Rubric，先阅读 [docs/configuration-guide.md](docs/configuration-guide.md) 和 [docs/rule-ownership.md](docs/rule-ownership.md)。
