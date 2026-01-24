# Skills 资源库更新日报

**日期**：2026-01-22  
**生成时间**：本次更新自动生成

## 更新统计
- 新增资源：8
- 修改资源：0
- 删除资源：0

## 详细更新列表

### 博客文章
- [新增] **Spring AI Agentic Patterns (Part 1): Agent Skills - Modular, Reusable Capabilities**
  - 链接：https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills
  - 说明：Spring AI 在 Java 生态落地 Agent Skills（SKILL.md + 渐进式加载 + scripts/references/assets），并说明发现→激活→执行流程与安全注意事项

- [新增] **How to Write and Implement Agent Skills（DigitalOcean）**
  - 链接：https://www.digitalocean.com/community/tutorials/how-to-implement-agent-skills
  - 说明：从零实现 Skill（以 PDF 解析为例），解释 SKILL.md frontmatter、目录结构与集成方式

- [新增] **Using Agent Skills to add alt texts to my blog post images**
  - 链接：https://www.jannemattila.com/appdev/2026/01/12/using-agent-skills.html
  - 说明：真实案例：使用 `.github/skills/.../SKILL.md` 让代理批量生成并写回图片 alt 文本

- [新增] **Writing OpenCode Agent Skills: A Practical Guide with Examples**
  - 链接：https://jpcaparas.medium.com/writing-opencode-agent-skills-a-practical-guide-with-examples-870ff24eec66
  - 说明：以 OpenCode 为例讲 Skills 写作方法与跨工具可移植性（Agent Skills open standard）

- [新增] **Codex changelog**
  - 链接：https://developers.openai.com/codex/changelog/
  - 说明：Codex 对 Skills/规范实现的持续更新记录（含 2026-01 多项变更）

- [新增] **Skills vs. Commands [vs. Rules]（Cursor 社区讨论）**
  - 链接：https://forum.cursor.com/t/skills-vs-commands-vs-rules/148875
  - 说明：梳理 Rules / Commands / Skills / Subagents 的定位差异，适合作为团队共识材料

- [新增] **SKILL.md is created when creating new cursor rules（Cursor 已知问题）**
  - 链接：https://forum.cursor.com/t/skill-md-is-created-when-creating-new-cursor-rules/148833
  - 说明：稳定版创建 Project Rule 误生成 `.cursor/skills/SKILL.md` 的问题说明与临时规避方案

### GitHub 仓库
- [新增] **meetrais/claude-agent-skills**
  - 链接：https://github.com/meetrais/claude-agent-skills
  - 说明：Claude Skills 示例仓库：默认文档类 skills + 自定义 skills 框架（含 SKILL.md + scripts 组织方式）

## 更新摘要
本次主要补齐了 2026-01 的 Skills 生态资料（实现教程、真实案例、规则/技能定位讨论、Codex 变更日志），并更新了资源清单文件。

## 待办事项
- [ ] 如需在 GitHub Pages 的“日报界面”展示更新日报，请确保运行 `python3 scripts/generate_github_pages.py` 后 commit + push
- [ ] 如需自动化：可将“生成日报 + 生成 docs 同步”纳入日常脚本/CI

