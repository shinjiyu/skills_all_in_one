# 07｜文档处理实战：Word/Excel/PDF 的最小可用 Skill 设计

关键词：cursor, claude code, skills, skill

Git 链接：
- 仓库：[shinjiyu/skills_all_in_one](https://github.com/shinjiyu/skills_all_in_one)
- 本文：[docs/wechat-series/07-doc-processing-case/README.md](https://github.com/shinjiyu/skills_all_in_one/blob/main/docs/wechat-series/07-doc-processing-case/README.md)

“文档处理”是最适合 Skills 的场景之一：需求高频、步骤可复现、输出结构可固定。真正的关键不在于“能不能提取文本”，而在于：**怎么把处理结果组织成可交付的报告**。

## 1）最小可用能力：先别追求万能

一个“最小可用”的文档处理 Skill，建议只覆盖 3 件事：

- **识别**：文件类型/页数/表格数量等元信息
- **提取**：按规则提取文本或表格（例如只提取标题与摘要）
- **输出**：固定模板输出（摘要 + 关键发现 + 风险点）

不要一上来就做“全文理解 + 自动改写 + 自动生成 PPT”，那会让边界失控。

## 2）本仓库的参考项目

直接看 `examples/05-document-processor/`：它展示了文档处理 Skill 的项目组织方式——脚本负责解析，Skill 负责流程与交付。

同时在 `docs/references.md` 里也给出了一些常用库方向（如 Word/Excel/PDF 处理）。

## 3）把结果写成“可读交付物”的模板

公众号/团队交付最常用的结构是：

- **文件概览**：类型、大小、页数/工作表
- **提取摘要**：3–5 句
- **关键信息**：用列表列出（标题、日期、结论、关键数字）
- **异常与建议**：缺页/乱码/无法解析的提示与下一步

这个结构一旦固定，后续任何文档处理都能稳定复用。

## 4）判断题（欢迎评论区回复“对/错”）

**判断题：** 文档处理 Skill 最难的部分通常是“解析文档”，而不是“把结果组织成稳定可读的交付物”。（对 / 错？）

