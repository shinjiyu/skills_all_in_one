# 社区资源搜索日报 - 2026-01-20

> 本报告记录 2026 年 1 月 20 日的 Skills/Agent Skills 相关资料搜索结果（重点：多 Agent 规模化实践、Codex 生态补全、中文教程补充、跨平台技能管理工具）

---

## 📊 搜索概况

- **搜索时间**：2026-01-20
- **搜索范围**：Agent Skills / SKILL.md / 多 Agent 协作 / Codex 配置（AGENTS.md）/ 跨平台技能管理 / 中文教程
- **搜索策略**：优先使用配置的搜索源做定向搜索（官方博客/文档/社区/索引平台），再补充全网搜索；最后对照仓库现有资源做去重核验
- **新增候选资源**：10 项（本次仅生成报告，尚未写入 `community-resources/data/resources.json`）

---

## 🎉 今日新发现

### 1. Scaling long-running autonomous coding（Cursor Blog）⭐⭐⭐⭐⭐

- **类型**：官方博客 / 多 Agent 规模化实践 / 组织与提示工程
- **链接**：[查看文章](https://cursor.com/blog/scaling-agents)
- **发布日期**：2026-01-14
- **要点**：
  - 给出 “Planners / Workers / Judge” 的分工与迭代循环，解释为何扁平自协调（锁/并发控制）会导致瓶颈与“风险规避”
  - 关注长跑任务中的漂移（drift）与上下文管理，并强调“提示 > harness > 模型”的影响权重
  - 提供多个长期运行项目规模指标（LoC、commit 等）作为实践参考
- **价值评估**：⭐⭐⭐⭐⭐（强烈推荐，面向工程实践的多 Agent 协作复盘）

---

### 2. Skills explained: How Skills compares to prompts, Projects, MCP, and subagents（Claude Blog）⭐⭐⭐⭐⭐

- **类型**：官方博客 / 概念对齐 / 生态组件边界
- **链接**：[查看文章](https://claude.com/blog/skills-explained)
- **发布日期**：2025-11-13
- **要点**：
  - 系统解释 Skills/Prompts/Projects/Subagents/MCP 的“提供什么、何时加载、是否持久、最佳适用场景”
  - 重点阐述 progressive disclosure（元数据先加载、指令与资源按需加载）的上下文效率优势
- **价值评估**：⭐⭐⭐⭐⭐（强烈推荐，适合做团队共识材料）

---

### 3. Improving frontend design through Skills（Claude Blog）⭐⭐⭐⭐

- **类型**：官方博客 / 案例方法论 / 前端设计技能
- **链接**：[查看文章](https://www.claude.com/blog/improving-frontend-design-through-skills)
- **发布日期**：2025-11-12
- **要点**：
  - 用 Skills 解决“前端审美分布收敛”导致的同质化 UI 输出，给出可复用的前端审美 Skill 结构与示例片段
  - 强调“按需加载”避免把前端设计上下文常驻到所有任务中
- **价值评估**：⭐⭐⭐⭐（推荐，适合作为前端/设计类 Skills 的写法参考）

---

### 4. Create skills（OpenAI Codex Docs）⭐⭐⭐⭐⭐

- **类型**：官方文档 / 技能创建指南 / SKILL.md 规范与排障
- **链接**：[查看文档](https://developers.openai.com/codex/skills/create-skill)
- **发布日期**：未知
- **要点**：
  - 明确 skill 的运行时注入策略：默认只注入 name/description/path；正文仅在显式调用时注入
  - 提供 `$skill-creator` 的创建流程与手动创建 `SKILL.md` 的最小模板
  - 给出 repo/user scope 的保存位置建议与 best practices / troubleshoot
- **价值评估**：⭐⭐⭐⭐⭐（强烈推荐，补齐 Codex 在“如何写/放/调试 skills”层面的关键文档）

---

### 5. Custom instructions with AGENTS.md（OpenAI Codex Docs）⭐⭐⭐⭐⭐

- **类型**：官方文档 / 项目指令链 / 与 skills 的分层组合
- **链接**：[查看文档](https://developers.openai.com/codex/guides/agents-md)
- **发布日期**：未知
- **要点**：
  - 说明 Codex 的 `AGENTS.md` 发现顺序（global → project path 逐级）与 override 规则
  - 提供 fallback 文件名与 size limit（max bytes）配置方法
  - 适合作为“持久规范（AGENTS.md）+ 按需能力（Skills）”的工程化落地参考
- **价值评估**：⭐⭐⭐⭐⭐（强烈推荐，和 skills 体系互补）

---

### 6. Create Skill - Skill Creation Framework（Agent-Skills.md）⭐⭐⭐⭐

- **类型**：Skills 索引条目 / Skill 写作框架 / 模板与分层
- **链接**：[查看条目](https://agent-skills.md/skills/danielmiessler/PAIPlugin/create-skill)
- **发布日期**：未知
- **要点**：
  - 给出 simple/complex skills 的分层建议（`SKILL.md` 快速参考、`CLAUDE.md` 深度上下文）
  - 强调 description 触发词与可发现性（discoverable）的写法要点
- **价值评估**：⭐⭐⭐⭐（推荐，适合作为“写技能的框架”参考）

---

### 7. Agent Skills 管理神器：SkillsLM 一条命令覆盖9 个平台（53AI）⭐⭐⭐⭐

- **类型**：工具介绍 / 跨平台技能管理 / CLI
- **链接**：[查看文章](https://www.53ai.com/news/gerentixiao/2026011816529.html)
- **发布日期**：2026-01-18
- **作者**：AIGC胶囊
- **要点**：
  - 介绍 `SkillsLM` 的 install/list/update 等命令与多平台 `--agent` 安装策略
  - 覆盖多平台落盘路径与“项目级 vs 全局”实践建议
- **价值评估**：⭐⭐⭐⭐（推荐，适合多 Agent/多工具链用户做技能分发与同步）

---

### 8. Agent Skills入门指南，看这篇就够了 | 保姆级教程（53AI）⭐⭐⭐⭐

- **类型**：中文教程 / 入门指南
- **链接**：[查看文章](https://www.53ai.com/news/LargeLanguageModel/2026011283765.html)
- **发布日期**：2026-01-12
- **作者**：硅基客
- **要点**：
  - 从零解释 Skills 是“专业能力包”，强调 description 触发写法与三层加载（元数据/指令/资源）
  - 给出个人/项目 skills 的目录落位与扩展目录（references/examples/scripts）建议
- **价值评估**：⭐⭐⭐⭐（推荐，中文上手材料较完整）

---

### 9. Claude Skills 到底是什么？万字长文深度解析（53AI）⭐⭐⭐⭐

- **类型**：中文长文 / 概念与落地
- **链接**：[查看文章](https://www.53ai.com/news/LargeLanguageModel/2026011221065.html)
- **发布日期**：2026-01-12
- **作者**：AI前端探索
- **要点**：
  - 解释 Skill vs Workflow/Prompt/MCP 的边界与组合方式
  - 重点阐释“渐进式披露”如何让大量 skills 仍保持上下文高效
- **价值评估**：⭐⭐⭐⭐（推荐，适合做中文科普/团队对齐）

---

### 10. Agent Skill 开放标准（53AI）⭐⭐⭐⭐

- **类型**：中文解读 / 标准摘要 / 安全与验证
- **链接**：[查看文章](https://www.53ai.com/news/tishicikuangjia/2026011416325.html)
- **发布日期**：2026-01-14
- **作者**：极客工具XTool
- **要点**：
  - 汇总 `agentskills.io` 的目录结构、`SKILL.md` 字段约束、渐进式披露与验证方式
  - 提及脚本执行的安全风险与基本防护思路（sandbox/allowlist/confirmation/logging）
- **价值评估**：⭐⭐⭐⭐（推荐，中文标准要点速览）

---

## 📈 资源统计

| 分类 | 新增数量 |
|------|---------|
| 官方博客 | 3 |
| 官方文档 | 2 |
| 工具/平台 | 1 |
| Skills 索引条目 | 1 |
| 中文教程/解读 | 3 |
| **合计** | **10** |

---

## 💡 建议与后续跟踪

1. **入库更新**：将上述 10 条资源写入 `community-resources/data/resources.json`（对应 blog_posts / tools_and_plugins 等分类），并同步更新统计字段与 `last_updated`
2. **更新日志**：在 `community-resources/CHANGELOG.md` 追加 `2026-01-20` 条目（新增数量与链接）
3. **搜索源**：保持现有搜索源不变；后续可按需补充“Cursor forum / GitHub openai/skills”等作为可选扩展来源

---

**报告生成时间**：2026-01-20

