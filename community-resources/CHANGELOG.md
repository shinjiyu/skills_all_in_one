# 更新日志

本文档记录社区资源库的所有更新。

格式：`[YYYY-MM-DD]` - 更新内容

---

## 2026-01-09

### 新增
- **AgentSkills.best 平台**：发现并添加专门的 Claude Agent Skills 市场平台
  - 链接：https://agentskills.best/zh
  - 类型：在线平台，提供技能库、教程、最佳实践
  - 支持中英文
- **技术博客文章**：添加 3 篇高质量技术分析文章
  - Skill Creator 指南（x-cmd）
  - Anthropic Claude Skills 案例解析（ApFramework，2025-12-20）
  - Claude Skills：简单却革命性的扩展机制（Build School Learn）

### 改进
- 持续监控和更新社区资源
- 完善博客文章分类结构

---

## 2026-01-10

### 新增
- **官方 Skills 公告与生态更新**：补充 2 篇 Claude 官方博客文章
  - Introducing Agent Skills（2025-10-16）：https://claude.com/blog/skills
  - Skills for organizations, partners, the ecosystem（2025-12-18）：https://claude.com/blog/organization-skills-and-directory
- **官方工程深度文章**：新增 Anthropic Engineering 文章，解释 Skills 的渐进式加载与 SKILL.md 机制（2025-10-16）
  - https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **官方 Cookbook 教程**：新增 Skills notebook 入门（2025-10-14）
  - https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction
- **开放标准/规范入口**：新增 Agent Skills open standard 站点与规范仓库
  - https://agentskills.io/
  - https://github.com/agentskills/agentskills
- **社区工具/分发渠道**：新增社区维护的 Skills/Plugins 市场
  - https://claude-plugins.dev/
- **GitHub 仓库**：新增 Skills 写作/维护辅助 Skill 仓库
  - https://github.com/metaskills/skill-builder
- **社区教程文章**：新增一篇从零入门 Skills / SKILL.md 的示例文章（2025-10-23）
  - https://jewelhuq.medium.com/claude-skills-a-beginner-friendly-guide-with-a-real-example-ab8a17081206
- **视频教程**：新增一个面向新手的 Claude Skills 视频教程（YouTube）
  - https://www.youtube.com/watch?v=ifsLyAC7wkM

### 改进
- **数据文件同步**：更新 `community-resources/data/resources.json`（版本 1.1.0），补齐资源条目并更新统计与最后更新时间（2026-01-10）

## 2026-01-06

### 新增
- **Cursor 动态上下文发现技术文章**：归档 Cursor 官方博客文章，并生成公众号文章
  - 博客文章：Cursor 动态上下文发现技术（Token 节省 46.9%）
  - 公众号文章：`community-resources/articles/cursor-dynamic-context-discovery.md`
- **官方文档链接**：添加 7 个官方文档链接到博客文章资源库
  - Claude 帮助中心：什么是技能？
  - Claude 帮助中心：如何创建自定义 Skills
  - Agent Skills 概述（Claude 中文社区）
  - Agent Skills 快速开始（Claude 中文社区）
  - Skills 架构设计（Claude 中文社区）
  - Agent Skills 学习及案例
  - SDK 中的代理技能
- **官方/权威文档补充**：补充 5 个更权威/更完整的参考入口
  - Claude 帮助中心（EN）：What are Skills?
  - Claude 帮助中心（EN）：Using Skills in Claude
  - Claude 官方博客：Building Skills for Claude Code
  - Claude Code Skills 官方文档（code.claude.com）
  - Cursor Skills 文档
- **GitHub 仓库**：添加 6 个包含 SKILL.md 的 GitHub 仓库
  - anthropics/skills（官方示例仓库）
  - letta-ai/skills（社区示例仓库）
  - letta-ai/letta-code（编码代理工具）
  - intellectronica/skillz（MCP 服务器）
  - gotalab/skillport（Skills 集成工具）
  - Skill Seeker（转换工具）

### 修正
- **项目定位明确**：修正项目定位，专注于 Skills 开发和使用，不是 Claude Code 使用教程
- **搜索关键词优化**：更新 resource-search Skill 的搜索关键词，专注于 Skills 相关内容
- **清理不相关资源**：删除 Claude Code 使用教程类资源，只保留 Skills 相关内容
- **文档更新**：更新所有文档，明确项目专注于 Skills

### 改进
- **动态搜索源机制**：建立可动态扩展的搜索源管理系统
  - 创建 `community-resources/data/search-sources.json` 配置文件
  - 创建 `community-resources/SEARCH-SOURCES.md` 管理文档
  - 更新 resource-search Skill，支持使用配置的搜索源进行定向搜索
  - 支持根据用户提供的资源自动提取来源并添加到搜索源
  - 初始添加 8 个搜索源（Cursor 官方博客、Claude 官方博客、Claude 中文社区等）
- 更新 resource-search Skill，添加筛选规则，排除 Claude Code 使用教程
- 更新所有资源文件的说明，明确只收录 Skills 相关内容
- 修正 Skills 描述，去掉 "Claude Code" 前缀
- 添加工具和插件资源：Skill Seeker

---

## 2024-01-01

### 新增
- 创建社区资源目录结构
- 添加资源分类文件（博客文章、GitHub 仓库、视频教程、案例研究、工具和插件）
- 首次全网搜索归档：
  - 博客文章：9 篇
  - 视频教程：1 个
  - 案例研究：1 个

### 改进
- 优化目录结构，支持迭代更新
- 添加 JSON 数据格式支持
- 添加更新日志文件

---

## 更新说明

每次更新资源时，请在此文件中记录：
1. 更新日期
2. 新增的资源数量和类型
3. 修改的内容
4. 删除的资源（如有）
