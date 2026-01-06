# Skills 完整指南

本指南包含 Skills 的规范性检查、设置和使用说明。

## 目录

1. [Skills 位置和设置](#skills-位置和设置)
2. [规范性要求](#规范性要求)
3. [常见问题](#常见问题)
4. [检查清单](#检查清单)

## Skills 位置和设置

### 正确的 Skills 位置

根据 [Claude Code Skills 官方文档](https://code.claude.com/docs/en/skills)，Skills 必须放在以下位置之一：

#### 1. 项目 Skills（推荐用于团队项目）

```
项目根目录/
└── .claude/
    └── skills/
        └── your-skill/
            └── SKILL.md
```

**优点：**
- 团队成员都可以使用
- 可以提交到版本控制
- 适合团队共享的 Skills

#### 2. 个人 Skills（适合个人偏好）

```
~/.claude/skills/
└── your-skill/
    └── SKILL.md
```

**优点：**
- 跨所有项目可用
- 适合个人工作流

### 问题：Skills 没有触发？

最常见的原因是 **Skills 位置不正确**。

**解决方案：**
1. 确保 Skills 在 `.claude/skills/` 或 `~/.claude/skills/` 目录下
2. 重启 Claude Code（Skills 在启动时加载）
3. 验证：询问 "What Skills are available?"

## 规范性要求

### 文件结构

1. **目录位置**
   - 必须位于：`~/.claude/skills/`（个人）或 `.claude/skills/`（项目）
   - 每个 Skill 有独立的子目录
   - 目录中包含 `SKILL.md` 文件（大小写敏感）

2. **YAML Frontmatter（必需）**
   - 文件必须以 YAML frontmatter 开头
   - 用 `---` 标记包围（第一行必须是 `---`，不能有空白行）
   - 必须包含 `name` 字段
   - 必须包含 `description` 字段

3. **Description 字段要求**
   - 必须明确说明 Skill 做什么（具体能力）
   - 必须包含触发词（用户会自然说出的关键词）
   - 使用 "Use when..." 格式说明使用场景

### 标准格式示例

```markdown
---
name: your-skill-name
description: Brief description of what this Skill does. Use when [trigger conditions] or when the user asks [specific questions].
---

# Your Skill Name

## 描述
详细描述...

## 指令
具体指令...
```

### Description 编写最佳实践

**好的示例：**
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**不好的示例：**
```yaml
description: Helps with documents  # 太模糊，没有触发词
```

## 常见问题

### Q: Skills 在 `skills/` 目录下为什么不工作？

**A:** `skills/` 不是 Claude Code 识别的标准位置。必须使用 `.claude/skills/` 或 `~/.claude/skills/`。

### Q: 为什么需要重启 Claude Code？

**A:** Claude Code 在启动时加载 Skills。修改或添加 Skills 后需要重启才能生效。

### Q: 如何验证 Skill 已加载？

**A:** 询问 Claude "What Skills are available?"，如果能看到你的 Skill 名称和描述，说明已成功加载。

### Q: Skill 没有触发怎么办？

**A:** 检查以下几点：
1. description 字段是否包含用户会说的关键词
2. 你的请求是否匹配 description 中的触发词
3. 是否有其他 Skills 的 description 太相似导致冲突

### Q: 多个 Skills 冲突怎么办？

**A:** 如果 Claude 使用了错误的 Skill 或在相似 Skills 之间混淆，说明 descriptions 太相似。让每个 description 更具体，使用不同的触发词。

## 检查清单

### ✅ 文件位置
- [ ] Skills 在 `.claude/skills/` 或 `~/.claude/skills/` 目录下
- [ ] 每个 Skill 有独立的子目录
- [ ] 文件名为 `SKILL.md`（大小写敏感）

### ✅ 文件格式
- [ ] 文件以 YAML frontmatter 开头（`---` 标记）
- [ ] 包含 `name` 字段
- [ ] 包含 `description` 字段
- [ ] description 包含触发词

### ✅ 加载和测试
- [ ] 重启了 Claude Code
- [ ] 询问 "What Skills are available?" 能看到你的 Skill
- [ ] 使用触发词测试 Skill 是否激活

## 本项目的 Skills

本项目中的 Skills 位于：

- `.claude/skills/daily-report/` - 生成每日更新报告
- `.claude/skills/resource-briefing/` - 生成资源简报
- `.claude/skills/resource-search/` - 搜索最新资源

## 参考文档

- [Claude Code Skills 官方文档](https://code.claude.com/docs/en/skills)
- [Cursor Skills 文档](https://cursor.com/cn/docs/context/skills)
