# Claude Code 项目配置

此目录包含 Claude Code 的项目级配置和 Skills。

## 目录结构

```
.claude/
└── skills/          # 项目级 Skills
    ├── daily-report/
    ├── resource-briefing/
    └── resource-search/
```

## Skills 位置说明

根据 [Claude Code Skills 官方文档](https://code.claude.com/docs/en/skills)，Skills 可以放在以下位置：

1. **项目 Skills**（当前使用）：`.claude/skills/`
   - 项目中的任何人都可以使用
   - 适合团队共享的 Skills

2. **个人 Skills**：`~/.claude/skills/`
   - 仅当前用户可用
   - 适合个人偏好的 Skills

3. **企业 Skills**：由管理员配置
   - 整个组织可用

## 当前 Skills

- **daily-report** - 生成每日更新报告
- **resource-briefing** - 生成资源简报
- **resource-search** - 搜索最新资源

## 使用说明

1. 重启 Claude Code 以加载新的 Skills
2. 询问 "What Skills are available?" 查看可用 Skills
3. 使用触发词来激活相应的 Skill

## 注意事项

- Skills 文件必须命名为 `SKILL.md`（大小写敏感）
- 每个 Skill 需要独立的子目录
- 必须包含 YAML frontmatter 和 description 字段
