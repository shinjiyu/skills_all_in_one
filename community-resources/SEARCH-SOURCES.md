# 搜索源管理文档

本文档管理 Skills 资源搜索的动态搜索源，支持根据用户提供的资源自动扩展搜索范围。

## 搜索源分类

### 1. 官方博客 (official_blogs)

| 来源名称 | 基础 URL | 优先级 | 添加日期 | 添加原因 |
|---------|---------|--------|---------|---------|
| Cursor 官方博客 | https://cursor.com/cn/blog | 高 | 2026-01-06 | 用户提供资源：动态上下文发现文章 |
| Claude 官方博客 | https://www.claude.com/blog | 高 | 2026-01-06 | 官方文档归档时发现 |

### 2. 社区网站 (community_sites)

| 来源名称 | 基础 URL | 优先级 | 添加日期 | 添加原因 |
|---------|---------|--------|---------|---------|
| Claude 中文社区 | https://claudecn.com/docs | 高 | 2026-01-06 | 官方文档归档时发现 |
| Claude Skills 社区 | https://www.claudeskills.org | 中 | 2026-01-06 | 官方文档归档时发现 |

### 3. GitHub 组织 (github_organizations)

| 来源名称 | 基础 URL | 优先级 | 添加日期 | 添加原因 |
|---------|---------|--------|---------|---------|
| Anthropic | https://github.com/anthropics | 高 | 2026-01-06 | GitHub 仓库搜索时发现 |
| Letta AI | https://github.com/letta-ai | 中 | 2026-01-06 | GitHub 仓库搜索时发现 |

### 4. 文档网站 (documentation_sites)

| 来源名称 | 基础 URL | 优先级 | 添加日期 | 添加原因 |
|---------|---------|--------|---------|---------|
| Claude Code 官方文档 | https://code.claude.com/docs | 高 | 2026-01-06 | 官方文档归档时发现 |
| Cursor 文档 | https://cursor.com/docs | 高 | 2026-01-06 | 官方文档归档时发现 |

## 搜索策略

### 默认关键词

- `Agent Skills`
- `Claude Skills`
- `SKILL.md`
- `create Skills`
- `build Skills`
- `Skills examples`
- `Skills best practices`

### 排除关键词

- `Claude Code tutorial`（太宽泛，会搜到使用教程）
- `Claude Code install`（安装教程，不是 Skills）
- `Claude Code usage`（使用教程，不是 Skills）

### 优先级顺序

1. 官方博客（最高优先级）
2. 文档网站
3. 社区网站
4. GitHub 组织

## 如何添加新搜索源

### 自动添加流程

当用户提供新资源时，系统应该：

1. **提取来源信息**
   - 从 URL 中提取基础域名和路径
   - 识别来源类型（博客、文档、社区、GitHub 等）

2. **评估相关性**
   - 检查是否与 Skills 相关
   - 确认不是 Claude Code 使用教程

3. **生成搜索模式**
   - 基于来源 URL 生成 `site:` 搜索模式
   - 结合默认关键词生成完整搜索查询

4. **添加到搜索源**
   - 更新 `community-resources/data/search-sources.json`
   - 更新本文档
   - 记录添加原因和日期

### 手动添加流程

如果需要手动添加搜索源：

1. 编辑 `community-resources/data/search-sources.json`
2. 在相应的分类下添加新条目
3. 更新本文档
4. 在 `update_log` 中记录

### 示例：添加新搜索源

**场景：** 用户提供了 `https://example.com/blog/skills-tutorial`

**处理步骤：**

1. 提取基础 URL：`https://example.com/blog`
2. 识别类型：博客网站
3. 生成搜索模式：
   ```json
   {
     "name": "Example 博客",
     "base_url": "https://example.com/blog",
     "description": "Example 博客的 Skills 相关文章",
     "added_date": "2026-01-06",
     "added_reason": "用户提供资源：skills-tutorial 文章",
     "search_patterns": [
       "site:example.com/blog Skills",
       "site:example.com/blog Agent Skills",
       "site:example.com/blog SKILL.md"
     ],
     "priority": "medium"
   }
   ```
4. 添加到 `official_blogs` 或 `community_sites` 分类

## 使用搜索源

### 在 resource-search Skill 中使用

搜索时应该：

1. 按照优先级顺序遍历搜索源
2. 对每个搜索源使用其搜索模式
3. 结合默认关键词生成完整搜索查询
4. 执行搜索并筛选结果

### 搜索查询示例

对于 "Cursor 官方博客" 搜索源：

```
site:cursor.com/cn/blog Skills
site:cursor.com/cn/blog Agent Skills
site:cursor.com/cn/blog SKILL.md
```

## 更新日志

### 2026-01-06

- **创建搜索源管理机制**
- **添加初始搜索源**：
  - Cursor 官方博客（用户提供资源触发）
  - Claude 官方博客
  - Claude 中文社区
  - Claude Skills 社区
  - Anthropic GitHub
  - Letta AI GitHub
  - Claude Code 官方文档
  - Cursor 文档

## 维护建议

1. **定期检查**：每月检查一次搜索源的有效性
2. **更新优先级**：根据搜索结果质量调整优先级
3. **清理无效源**：移除不再有效的搜索源
4. **记录变更**：所有变更都应在 `update_log` 中记录

---

**注意：** 本文档与 `community-resources/data/search-sources.json` 同步维护，确保信息一致性。
