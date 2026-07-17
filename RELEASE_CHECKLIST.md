# 对外分享与发布检查清单

在仓库转为 Public、发布 Release 或对外大范围分享前，按这份清单检查。

## 1. 基础文件

- [ ] `README.md` 已说明项目定位和使用方式。
- [ ] `QUICKSTART.md` 已说明 clone 后如何配置并跑通第一个任务。
- [ ] `LICENSE` 已存在。
- [ ] `.gitignore` 已包含 `config/`、`private/`、`learning/`、`.env`。
- [ ] `CONTRIBUTING.md` 已说明贡献边界。
- [ ] `SECURITY.md` 已说明敏感信息处理方式。
- [ ] `CODE_OF_CONDUCT.md` 已存在。

## 2. 隐私检查

- [ ] 没有真实公司名。
- [ ] 没有真实产品名。
- [ ] 没有客户名或客户材料。
- [ ] 没有真实 PRD。
- [ ] 没有内部截图。
- [ ] 没有本机绝对路径。
- [ ] 没有私有代码库地址。
- [ ] 没有 token、cookie、password、secret、api_key。
- [ ] 没有内部 KMS、飞书/协作文档地址或可定位私有资源的文档 token。
- [ ] 已检查 Git 历史，不只是当前工作树。
- [ ] 如果历史中曾存在敏感内容，已明确决定是否清理历史、轮换权限或接受风险。

## 3. 使用链路检查

- [ ] 用户能从 `README.md` 找到 `QUICKSTART.md`。
- [ ] 用户能运行 `scripts/setup.sh` 初始化 `config/`。
- [ ] 用户能运行 `scripts/check-release.sh` 做发布前检查。
- [ ] 用户知道要填写产品背景、知识库、代码库和 Rubric。
- [ ] 用户知道如何复制 `AGENTS.template.md`。
- [ ] 用户知道第一个测试任务怎么问。
- [ ] `python3 scripts/validate-framework.py` 通过。
- [ ] `python3 scripts/validate-config.py` 在占位配置下输出 `CONFIG_STATUS=needs_configuration`，`--strict` 模式返回非零退出。
- [ ] `bash scripts/smoke-test-install.sh` 通过。
- [ ] GitHub Actions 在 `main` 和 Pull Request 上通过。
- [ ] 用户知道如何记录当前状态、阶段交接和 Eval 结果。

## 4. 内容边界

- [ ] 示例是虚构产品或公开产品。
- [ ] Rubric 是通用检查项，不包含业务专属答案。
- [ ] 模板是通用模板，不包含具体公司流程。
- [ ] 没有把私有经验沉淀放入公开仓库。
- [ ] Eval 案例只使用虚构或公开场景，不包含真实业务失败材料。
- [ ] 原型输出 Rubric 不绑定私有设计工具、公司设计系统或内部截图。

## 5. GitHub 设置

- [ ] 如果仓库还未公开，先在 private 状态完成检查。
- [ ] Push 后在 GitHub 页面复查 README 渲染和链接。
- [ ] 设置仓库 description。
- [ ] 添加 topics。
- [ ] 已启用 Private Vulnerability Reporting，或在 `SECURITY.md` 提供等价私密渠道。
- [ ] 已创建稳定 Tag 和 Release，并说明当前限制。
- [ ] 确认无敏感内容后再切换 public。
