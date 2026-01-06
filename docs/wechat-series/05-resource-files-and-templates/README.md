# 05｜资源文件的价值：让输出“长得一样”，让参数“可配置”

关键词：cursor, claude code, skills, skill

Git 链接：
- 仓库：[shinjiyu/skills_all_in_one](https://github.com/shinjiyu/skills_all_in_one)
- 本文：[docs/wechat-series/05-resource-files-and-templates/README.md](https://github.com/shinjiyu/skills_all_in_one/blob/main/docs/wechat-series/05-resource-files-and-templates/README.md)

当你想把 Skills 用到“可对外发布”的场景（例如公众号周报、日报、清单），最关键的不是写更长的说明，而是：**把稳定内容做成资源文件**，把变化部分当参数。

## 1）为什么要用资源文件

两个直接收益：

- **输出一致**：固定模板让文章结构不会乱
- **改动可控**：改模板就是改模板，不会误伤逻辑

从维护角度看，资源文件就是“内容层”，Skill 指令是“规则层”，脚本是“执行层”。三者分开，才好迭代。

## 2）本仓库已经准备了哪些资源

你可以在 `examples/resources/` 看到一些通用资源：

- `report_template.md`：报告模板
- `email_template.md`：邮件模板
- `config.json` / `settings.yaml`：配置示例
- `sample_data.csv` / `reference_data.json`：示例数据

这意味着你做一个“周报 Skill”，不需要从 0 写模板，直接复用并按字段填充即可。

## 3）公众号写作的一个实用拆分

以“资源简报”为例，可以拆成：

- **模板固定**：标题、栏目、推荐格式、结尾互动题
- **变量填充**：时间段、统计数字、重点条目、趋势摘要

当你把模板固定，写作就变成“填空题”，而不是“自由作文”。

## 4）判断题（欢迎评论区回复“对/错”）

**判断题：** 把输出结构抽成模板（资源文件），通常能显著提高 Skills 在“对外发布内容”场景下的稳定性。（对 / 错？）

