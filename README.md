# Claude Code Skills 教学系列示例代码

本仓库包含 Claude Code Skills 教学系列文章的所有示例代码和项目。

## 目录结构

```
claude-code-skills-tutorial/
├── examples/              # 示例项目
├── skills/                 # Skills 集合
│   └── resource-management/  # 资源管理 Skills
├── templates/             # 项目模板
├── docs/                  # 文档和参考资料
├── community-resources/   # 社区资源（与 docs 并列）
└── README.md             # 本文件
```

## 示例项目

### 基础示例
- `01-hello-world/` - 最简单的 Skills 示例
- `02-basic-instruction/` - 基础指令示例
- `03-script-integration/` - 脚本集成示例
- `04-resource-integration/` - 资源文件集成示例

### 实战案例
- `05-document-processor/` - 文档处理 Skills
- `06-api-integration/` - API 集成 Skills
- `07-team-shared/` - 团队共享 Skills
- `08-production-ready/` - 生产级 Skills

### 资源管理 Skills
位于 `skills/resource-management/` 目录：
- `resource-search/` - 资源搜索 Skill（搜索最新资料）
- `resource-briefing/` - 资源简报生成 Skill（生成定期简报）
- `daily-report/` - 更新日报生成 Skill（生成每日更新报告）

## 使用方法

每个示例项目都包含：
- `SKILL.md` - Skills 定义文件
- `README.md` - 项目说明和使用方法
- `scripts/` - 脚本文件（如有）
- `resources/` - 资源文件（如有）

## 文档

- [参考资料](docs/references.md) - 官方文档和社区资源
- [文章大纲](docs/article-outlines.md) - 10篇文章的详细大纲
- [质量检查清单](docs/quality-checklist.md) - 项目质量检查标准
- [阅读时间指南](docs/reading-time-guide.md) - 文章长度控制指南

## 模板

- `templates/basic-skill-template/` - 基础 Skill 模板
- `templates/advanced-skill-template/` - 高级 Skill 模板

## 资源文件

通用资源文件位于 `examples/resources/`：
- 模板文件（邮件、报告、代码模板）
- 配置文件（JSON、YAML）
- 示例数据（CSV、JSON）

## 脚本示例

通用脚本示例位于 `examples/scripts/`：
- Python 脚本（文件处理、API 客户端等）
- JavaScript 脚本（文本处理、数据验证等）

## 社区资源

- [社区资源目录](community-resources/README.md) - 收集的社区资源
- [GitHub 仓库](community-resources/github-repositories.md) - Skills 相关的 GitHub 项目
- [博客文章](community-resources/blog-posts.md) - 技术博客和教程
- [视频教程](community-resources/video-tutorials.md) - 视频教学资源
- [案例研究](community-resources/case-studies.md) - 实际应用案例
- [工具和插件](community-resources/tools-and-plugins.md) - 开发工具和插件

## 参考资料

详见 [docs/references.md](docs/references.md)

## 贡献

欢迎提交 Issue 和 Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

