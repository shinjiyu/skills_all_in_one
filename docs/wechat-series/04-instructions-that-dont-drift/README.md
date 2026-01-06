# 04｜指令怎么写才不飘：输入边界、步骤分解、输出模板

关键词：cursor, claude code, skills, skill

Git 链接：
- 仓库：[shinjiyu/skills_all_in_one](https://github.com/shinjiyu/skills_all_in_one)
- 本文：[docs/wechat-series/04-instructions-that-dont-drift/README.md](https://github.com/shinjiyu/skills_all_in_one/blob/main/docs/wechat-series/04-instructions-that-dont-drift/README.md)

“同一句话每次输出都不一样”并不神秘。绝大多数时候是因为你只写了目标，没有写清楚：**输入边界**、**执行步骤**、**输出模板**。

## 1）先定输入边界：缺什么就问什么

以“生成周期简报”为例，最常缺的输入只有两个：

- **时间段**：周报/月报/自定义起止日期
- **输出语言/风格**：中文（默认）/英文，是否对外发布

如果用户没有提供时间段，你可以选择：

- 先追问（更严谨）
- 给默认值并在正文标明（更省沟通成本）

## 2）步骤要能被检查：数据从哪来、怎么筛

写步骤时建议把“数据源”写死：

- 读取 `community-resources/` 资源文件
- 参考 `community-resources/CHANGELOG.md` 的更新记录
- 必要时对比目录变化（新增/修改/删除）

这样做的好处是：当结果有争议时，你能明确“是数据源变了还是规则变了”，而不是陷入争论。

## 3）输出模板：字段不可缺省

公众号文章最常见的“翻车点”是输出风格不稳定。解决方式是用模板锁住关键字段，例如：

- 时间段
- 更新统计（按分类）
- 重点推荐（3–5 条，每条包含：标题/链接/一句推荐理由）
- 趋势总结（3–5 句）

当字段不可缺省，输出就不会变成散文。

## 4）用仓库现成 Skill 对照理解

你可以直接看 `.claude/skills/resource-briefing/SKILL.md`：它的目标很清晰，但真正让它稳定的是“数据来源 + 输出结构”。

## 5）判断题（欢迎评论区回复“对/错”）

**判断题：** 为了输出更稳定，Skill 指令里用固定模板约束“字段不可缺省”，通常比“让模型自由发挥”更可靠。（对 / 错？）

