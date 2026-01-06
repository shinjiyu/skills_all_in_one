# 03｜SKILL.md 规范一把梭：位置、YAML、触发词与冲突

关键词：cursor, claude code, skills, skill

Git 链接：
- 仓库：[shinjiyu/skills_all_in_one](https://github.com/shinjiyu/skills_all_in_one)
- 本文：[docs/wechat-series/03-skillmd-spec/README.md](https://github.com/shinjiyu/skills_all_in_one/blob/main/docs/wechat-series/03-skillmd-spec/README.md)

你会遇到的第一类“看似玄学”的问题，90% 都不是模型的问题，而是规范问题：**放错位置、少了字段、触发词写得太像**。

## 1）位置：放错就等于不存在

可被识别的位置只有两类：

- **项目级**：`.claude/skills/<skill-name>/SKILL.md`
- **个人级**：`~/.claude/skills/<skill-name>/SKILL.md`

本仓库采用项目级 Skills：`.claude/skills/` 下已有 `resource-search`、`resource-briefing`、`daily-report`。

## 2）YAML 头：最小必须字段

`SKILL.md` 必须以 YAML frontmatter 开头，至少包含：

- `name`：唯一标识
- `description`：触发与选择的关键

很多“没触发”的根因，是第一行不是 `---`、或 `description` 太模糊。

## 3）description：写给“触发器”的，不是写给人看的

一个好用的 `description`，通常包含三件事：

- **能力**：做什么（例如“生成资源简报”）
- **边界**：用在什么场景（例如“周报/月报/指定时间段”）
- **触发词**：用户会怎么说（例如“生成本周简报”“周期简报”“从…到…”）

如果你的多个 Skills 都写成“helps with resources”，它们就会互相抢。

## 4）冲突：不是 Bug，是设计信号

当你发现 Claude 触发了“错误的 Skill”，大概率意味着：

- 多个 Skills 的 `description` 太相似
- 你的请求表达过于宽泛（比如只说“帮我整理一下”）

解决方式不是“加更多内容”，而是让边界更清晰：**每个 Skill 负责一件事**。

## 5）判断题（欢迎评论区回复“对/错”）

**判断题：** `description` 写得越泛用越好，因为这样更容易触发。（对 / 错？）

