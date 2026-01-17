# 社区资源搜索日报 - 2026-01-13

> 本报告记录 2026 年 1 月 13 日的 Skills/Agent Skills 相关资料搜索结果（重点：Cursor Agent 最佳实践、Claude Code Skills/Plugins 一手入口）

---

## 📊 搜索概况

- **搜索时间**：2026-01-13
- **搜索范围**：Cursor Agent / Agent harness / Agent Skills / Claude Code Skills / Claude Code Plugins
- **搜索策略**：优先一手来源（官方博客 / 官方文档 / 官方仓库目录），避免二手搬运
- **新增资源**：2 项

---

## 🎉 今日新发现

### 1. Cursor 官方博客：使用 Agent 编码的最佳实践 ⭐⭐⭐⭐⭐

- **类型**：官方博客 / 最佳实践 / 工作流
- **链接**：[查看文章](https://cursor.com/cn/blog/agent-best-practices)
- **发布日期**：2026-01-09
- **要点**：
  - 明确提出 **agent harness** 三件套：**Instructions / Tools / User messages**
  - 强调 **Plan 模式**（先规划再写代码）和“从计划重启”的修正策略
  - 专门讲了 **Rules vs Skills**：Rules 是静态上下文，Skills 是动态能力
  - 给出一个“长时间运行的 Agent 循环（Stop hook + max iterations + DONE 信号）”的可操作示例
  - 明确提到：**Agent Skills 目前仅在 Nightly 通道可用**（对你之前的 GenerateImage/Nightly 观察也形成呼应）
- **价值评估**：⭐⭐⭐⭐⭐（强烈推荐，适合收录为“官方最佳实践”锚点）

---

### 2. Anthropic 官方仓库：Claude Code Plugins（官方插件目录）⭐⭐⭐⭐

- **类型**：官方仓库 / 插件目录 / 参考入口
- **链接**：[查看仓库](https://github.com/anthropics/claude-code/tree/main/plugins)
- **要点**：
  - 官方插件目录的“总入口”，包含多套可直接参考的插件形态：commands/agents/skills/hooks/MCP
  - 目录 README 里有一张结构化表格，能快速定位各插件提供的能力（例如：`plugin-dev`、`hookify`、`code-review`、`ralph-wiggum` 等）
  - 对想做“工程化技能/插件资产”的团队来说，这个入口非常适合作为长期跟踪源
- **价值评估**：⭐⭐⭐⭐（推荐，适合作为“官方插件样例集合”的索引）

---

## 📈 资源统计

| 分类 | 新增数量 |
|------|---------|
| 官方博客/文档 | 1 |
| 官方仓库/目录 | 1 |
| **合计** | **2** |

---

## 💡 建议与后续跟踪

1. **把 Cursor 的“Agent 最佳实践”当作本库的“工作流总纲”**：它把 Plan/Rules/Skills/Hooks 的关系讲得非常体系化。  
2. **把 Claude Code Plugins 目录当作“插件样板间”**：后续新增/变化也容易被发现。  
3. **下一步可追踪**：
   - Cursor：`/cn/blog` 新文章（尤其 Agent / hooks / skills / MCP 相关）
   - Anthropic：`anthropics/claude-code` 插件目录的新增/调整

---

**报告生成时间**：2026-01-13

