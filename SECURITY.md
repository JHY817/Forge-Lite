# 安全说明

## 如何报告敏感信息

如果你发现仓库里误提交了密钥、私有公司信息、内部路径或其他敏感内容，请优先使用 [GitHub Private Vulnerability Reporting](https://github.com/JHY817/Forge-Lite/security/advisories/new) 向维护者私密报告。

如果私密报告功能不可用，请只在公开 Issue 中说明“需要私密联系维护者”，不要附上敏感细节。

## 不要提交什么

请不要提交：

- API key
- token
- cookie
- 私有仓库 URL
- 内部截图
- 真实客户数据
- 真实 PRD
- 公司专属知识库

## 维护者处理建议

如果敏感信息已经进入仓库历史，在公开发布前应尽量从历史记录中移除。

如果仓库已经公开，应尽快：

1. 删除敏感内容。
2. 轮换相关密钥。
3. 检查是否有 fork 或 release 包含敏感内容。
4. 在必要时发布安全说明。
