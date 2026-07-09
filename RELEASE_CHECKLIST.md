# 发布前检查清单

在把仓库切换为 public 前，按这份清单检查。

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

## 3. 使用链路检查

- [ ] 用户能从 `README.md` 找到 `QUICKSTART.md`。
- [ ] 用户能运行 `scripts/setup.sh` 初始化 `config/`。
- [ ] 用户能运行 `scripts/check-release.sh` 做发布前检查。
- [ ] 用户知道要填写产品背景、知识库、代码库和 Rubric。
- [ ] 用户知道如何复制 `AGENTS.template.md`。
- [ ] 用户知道第一个测试任务怎么问。

## 4. 内容边界

- [ ] 示例是虚构产品或公开产品。
- [ ] Rubric 是通用检查项，不包含业务专属答案。
- [ ] 模板是通用模板，不包含具体公司流程。
- [ ] 没有把私有经验沉淀放入公开仓库。

## 5. GitHub 设置

- [ ] 先创建 private repo。
- [ ] push 后在 GitHub 页面复查。
- [ ] 设置仓库 description。
- [ ] 添加 topics。
- [ ] 确认无敏感内容后再切换 public。
