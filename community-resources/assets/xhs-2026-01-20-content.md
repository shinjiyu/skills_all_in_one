# 小红书发布物料 - 2026-01-20

## 封面图文案

**主标题**：多 Agent “长跑”怎么做？Cursor 放出实战复盘

**副标题**：再补齐 Codex 的 Skills / AGENTS.md 关键文档

**要点**：
- Cursor：Planners / Workers / Judge 多 Agent 分工
- Claude：Skills vs Prompt/Project/MCP/Subagent 一文讲清
- OpenAI Codex：Create Skill + AGENTS.md（项目指令链）
- SkillsLM：一条命令同步 9 个平台 Skills

**日期**：2026-01-20

---

## 正文内容（可直接发）

这两天补资源时发现：**Agent Skills 的生态开始从“概念讨论”走向“工程化落地”**。

今天值得收藏的 3 个关键词：**多 Agent 协作、技能/指令分层、跨平台分发**。

---

### ① Cursor：多 Agent 长时间自治编码怎么扩到“百人协作”？

文章：*Scaling long-running autonomous coding*（2026-01-14）
核心是把角色拆开：
- **Planners**：持续探索 + 产出任务
- **Workers**：只管把任务做完
- **Judge**：决定是否进入下一轮

重点：他们明确说“扁平自协调 + 锁”会变成瓶颈，反而让系统变慢、让 agent 变保守。

（搜索：`cursor.com/blog/scaling-agents`）

---

### ② Claude：Skills 到底放在整个栈的哪个位置？

文章：*Skills explained: Skills vs prompts, Projects, MCP, subagents*（2025-11-13）
如果你经常纠结：
- 这段规范该写进 Skill，还是写进 Project？
- MCP 是“连接”，Skill 是“方法论”，那边界到底怎么划？

这篇把边界讲得很清楚，建议团队统一口径时直接引用。

（搜索：`claude.com/blog/skills-explained`）

---

### ③ OpenAI Codex：补齐两个“落地必看”的官方文档

1) **Create skills**：怎么写 `SKILL.md`、放哪里、怎么排障  
（搜索：`developers.openai.com/codex/skills/create-skill`）

2) **AGENTS.md**：项目指令链怎么发现、怎么 override、怎么设 fallback 文件名  
（搜索：`developers.openai.com/codex/guides/agents-md`）

我自己的总结：**AGENTS.md 负责“持续的工作约定”，Skills 负责“按需加载的专业能力”。**

---

### ④ Bonus：多平台用户的“技能同步”工具

有个中文文章介绍了 `SkillsLM`（CLI）——目标很明确：**同一套 skills 同步装到 Cursor / Claude Code / Codex / OpenCode / Roo / Goose / Gemini…**

（搜索：`53ai SkillsLM 2026011816529`）

---

## 结尾一句话（引导互动）

你现在的工作流更像哪种？
- A：单 agent + 一堆 prompt（容易重复）
- B：AGENTS.md/规则（常驻）+ Skills（按需）
- C：多 Agent 并行（开始遇到协调问题）

我可以按你的选项，把对应的“目录结构/写法模板/最小可用清单”整理一份。

---

## 🏷️ 标签建议

#AgentSkills #AI编程 #Cursor #Claude #OpenAI #Codex #多智能体 #SKILL文件 #MCP #程序员日常 #技术分享

---

## 发布注意事项

1. **封面图**：信息卡片 4 条要点（多 Agent / Skills 边界 / Codex 文档 / SkillsLM）
2. **链接处理**：小红书可能不支持外链，建议用“域名+路径”或“关键词+站内搜索”
3. **字数**：如果需要精简，优先保留 ①②③ 三段，④ 作为一句话补充即可

