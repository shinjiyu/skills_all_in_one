# 社区资源目录

本目录收集 Claude Code Skills 相关的社区资源，包括示例项目、教程、博客文章等。

## 目录结构

### 资源分类文件
- [GitHub 仓库](github-repositories.md) - Skills 相关的 GitHub 项目和示例
- [博客文章](blog-posts.md) - 技术博客和教程文章
- [视频教程](video-tutorials.md) - 视频教学资源
- [案例研究](case-studies.md) - 实际应用案例
- [工具和插件](tools-and-plugins.md) - 相关开发工具和插件

### 管理文件
- [更新日志](CHANGELOG.md) - 记录所有资源更新历史
- [资源模板](TEMPLATE.md) - 添加资源时使用的模板格式
- [数据文件](data/resources.json) - JSON 格式的资源数据（便于程序处理）

### 报告目录
- [reports/](reports/) - 存储生成的简报和日报文件

## 贡献指南

欢迎提交社区资源！请按照以下方式贡献：

1. 找到对应的分类文件
2. 按照格式添加资源链接
3. 提交 Pull Request

### 资源格式

每个资源应包含：
- **标题**：资源名称
- **链接**：资源 URL
- **描述**：简要说明资源内容
- **作者**：资源作者（如有）
- **标签**：相关标签（如：入门、进阶、实战等）

### 示例

```markdown
- **Claude Skills 入门教程**
  - 链接：https://example.com/tutorial
  - 描述：从零开始学习 Claude Code Skills 的完整教程
  - 作者：John Doe
  - 标签：入门、教程
```

## 更新日志

详细的更新记录请查看 [CHANGELOG.md](CHANGELOG.md)

### 快速统计
- 2024-01-01：创建社区资源目录
- 2024-01-01：首次全网搜索归档，添加 11 个资源
- 2024-01-01：优化目录结构，支持迭代更新
- 2024-01-01：添加 GitHub 仓库：skills_all_in_one

## 相关 Skills

以下 Skills 可以帮助维护资源库：

1. **资源搜索 Skill** (`skills/resource-management/09-resource-search/`) - 搜索最新资料
2. **资源简报生成 Skill** (`skills/resource-management/10-resource-briefing/`) - 生成定期简报
3. **更新日报生成 Skill** (`skills/resource-management/11-update-daily-report/`) - 生成每日更新报告

