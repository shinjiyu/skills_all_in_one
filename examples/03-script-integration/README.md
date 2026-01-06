# 脚本集成 Skill

这个示例展示了如何将 Python 脚本集成到 Skills 中。

## 文件结构

```
03-script-integration/
├── SKILL.md
└── scripts/
    └── file_stats.py
```

## 功能

- 统计文本文件的字符数、单词数和行数
- 通过脚本执行文件处理任务
- 错误处理和验证

## 使用方法

1. 确保 Python 环境已安装
2. 启用这个 Skill
3. 对 Claude 说："统计文件 <文件路径> 的信息"

## 说明

这个示例展示了：
- 如何在 SKILL.md 中定义脚本调用
- 如何组织脚本文件
- 如何传递参数给脚本
- 如何处理脚本执行结果

## 依赖

- Python 3.x


