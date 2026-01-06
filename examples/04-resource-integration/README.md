# 资源文件集成 Skill

这个示例展示了如何在 Skills 中使用资源文件（模板、配置文件等）。

## 文件结构

```
04-resource-integration/
├── SKILL.md
└── resources/
    ├── templates/
    │   ├── welcome_email.md
    │   ├── notification_email.md
    │   └── reminder_email.md
    └── config.json
```

## 功能

- 根据模板生成邮件内容
- 支持多种邮件类型
- 使用配置文件管理设置
- 模板变量替换

## 使用方法

1. 启用这个 Skill
2. 对 Claude 说："生成一封<邮件类型>邮件，收件人是<姓名>"

支持的邮件类型：
- welcome（欢迎邮件）
- notification（通知邮件）
- reminder（提醒邮件）

## 说明

这个示例展示了：
- 如何组织资源文件
- 如何在 SKILL.md 中引用资源文件
- 如何使用模板文件
- 如何使用配置文件
- 如何进行变量替换


