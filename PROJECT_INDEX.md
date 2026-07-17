# 项目目录索引

这个文件帮你快速理解每个目录是干什么的。

## 先看这里

- `README.md`：项目介绍，说明 FORGE Lite 是什么、怎么用。
- `QUICKSTART.md`：clone 后快速配置和跑通第一个任务。
- `AGENTS.template.md`：Agent 指令模板，以后可以复制到具体项目里使用。
- `RELEASE_CHECKLIST.md`：发布到 GitHub 前的检查清单。

## 配置示例

- `config.example/product-context.example.md`：产品背景配置模板。
- `config.example/knowledge-base.example.yaml`：知识库配置示例。
- `config.example/codebase.example.yaml`：代码库配置示例。
- `config.example/rubric.example.yaml`：私有 Rubric 扩展配置示例。

真实配置以后应该放在 `config/` 里，并且不要提交到 GitHub。

## 工作流

- `workflows/end-to-end-prd.md`：从需求到 PRD 的完整流程。
- `workflows/single-module-task.md`：只做一个模块任务时使用。
- `workflows/review-and-retrospective.md`：审计、返工、复盘时使用。
- `workflows/runtime-state.md`：阶段状态、迁移、回退失效和恢复。
- `workflows/context-and-evidence.md`：阶段上下文、事实分级和信息对齐。
- `workflows/approval-and-parallelism.md`：auto / notify / approve 和受控并行。

## 能力模块

- `modules/demand-understanding.md`：需求理解。
- `modules/product-current-state.md`：产品现状理解。
- `modules/reverse-engineering.md`：逆向工程。
- `modules/data-analysis-decision.md`：数据分析判断。
- `modules/competitor-analysis.md`：竞品分析。
- `modules/solution-design.md`：方案设计。
- `modules/prototype-preparation.md`：原型设计准备。
- `modules/prd-generation.md`：PRD 生成。
- `modules/review-and-learning.md`：审计与经验沉淀。

## 通用 Rubric

- `rubrics/direction-gate.md`：方向门禁检查。
- `rubrics/product-logic-generic.md`：通用产品逻辑检查。
- `rubrics/prd-quality.md`：PRD 质量检查。
- `rubrics/writing-quality.md`：表达质量检查。
- `rubrics/issue-severity.md`：P0/P1/P2、停止条件和复审范围。
- `rubrics/reverse-engineering-quality.md`：逆向事实强度和证据质量。
- `rubrics/prototype-output-quality.md`：通用原型输出保真、状态和 QA 验收。

## 模板

- `templates/design-plan.md`：设计计划模板。
- `templates/current-state.md`：当前状态模板。
- `templates/reverse-engineering-summary.md`：逆向工程总结模板。
- `templates/solution-design.md`：方案设计模板。
- `templates/product-design-brief.md`：原型设计 Brief 模板。
- `templates/prd.md`：PRD 模板。
- `templates/stage-handoff.md`：阶段交接模板。

## 文档

- `docs/concepts.md`：核心概念说明。
- `docs/configuration-guide.md`：配置说明。
- `docs/collaboration-guide.md`：协作方式说明。
- `docs/open-source-checklist.md`：第一次 GitHub 开源注意事项。
- `docs/faq.md`：常见问题。
- `docs/rule-ownership.md`：规则唯一来源和去重边界。

## Eval

- `evals/README.md`：评测目的和执行原则。
- `evals/scoring.md`：通用评分标准。
- `evals/cases/template.md`：评测案例模板。
- `evals/cases/generic-regression-cases.md`：不含真实业务信息的通用回归案例。
- `evals/records.md`：append-only 评测记录。

## GitHub 开源文件

- `LICENSE`：MIT 开源协议。
- `CONTRIBUTING.md`：贡献说明。
- `SECURITY.md`：安全和敏感信息报告说明。
- `CODE_OF_CONDUCT.md`：行为准则。
- `.github/ISSUE_TEMPLATE/`：Issue 模板。
- `.github/pull_request_template.md`：PR 模板。

## 脚本

- `scripts/setup.sh`：生成本地配置和 `AGENTS.md`。
- `scripts/validate-config.py`：检查首次使用必需配置和按需配置。
- `scripts/validate-framework.py`：检查框架结构和规则链。
- `scripts/smoke-test-install.sh`：在干净临时目录演练首次安装和重复安装。
- `scripts/check-release.sh`：发布前检查敏感边界、安装链路和框架结构。

## 示例

- `examples/fictional-product/README.md`：虚构产品 TaskBoard 示例。

## 为什么文件名使用英文

英文文件名更容易被跨平台工具和自动化脚本稳定识别。当前正文中文优先，英文版作为后续扩展，不影响中文使用链路。
