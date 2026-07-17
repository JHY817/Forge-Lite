# 贡献说明

感谢你关注 FORGE Lite。

## 欢迎贡献什么

适合贡献：

- 通用工作流改进。
- 通用模块定义。
- 通用产品管理 Rubric。
- 模板改进。
- 虚构示例。
- 文档修正。

不适合贡献：

- 公司专属产品知识。
- 内部工作流。
- 真实客户案例。
- 真实 PRD。
- 私有代码库路径。
- 密钥、token 或其他凭据。

## Pull Request 建议

提交 PR 时请注意：

1. 示例必须是虚构的，或基于公开产品。
2. 区分通用框架改进和具体业务观点。
3. 说明为什么这个改动具有通用价值。
4. 不要为了流程而增加流程；只有能减少真实歧义或风险时，才增加规则。

## 本地验证

提交 Pull Request 前运行：

```bash
python3 scripts/validate-framework.py
bash scripts/smoke-test-install.sh
bash scripts/check-release.sh
```

如果修改了流程、Rubric 或 Agent 路由，请同时补充 `evals/cases/` 或说明已用哪个现有案例验证。

## 语言

中文内容可以接受。  
英文翻译也欢迎，但不要为了英文牺牲表达准确性。
