# 资源文件集成 Skill

## 描述

这个 Skill 演示了如何使用资源文件（模板、配置文件等）来增强 Skills 的功能。

## 用途

根据模板生成邮件内容，支持多种邮件类型。

## 指令

当用户要求生成邮件时，请按照以下步骤操作：

1. **参数说明：**
   - `email_type`: 邮件类型，可选值：`welcome`（欢迎邮件）、`notification`（通知邮件）、`reminder`（提醒邮件）
   - `recipient_name`: 收件人姓名（必填）
   - `custom_content`: 自定义内容（可选）

2. **处理流程：**
   - 根据 `email_type` 选择对应的模板文件：
     - `welcome` → `resources/templates/welcome_email.md`
     - `notification` → `resources/templates/notification_email.md`
     - `reminder` → `resources/templates/reminder_email.md`
   - 读取模板文件内容
   - 替换模板中的占位符：
     - `{recipient_name}` → 收件人姓名
     - `{custom_content}` → 自定义内容（如有）
   - 返回生成的邮件内容

3. **输出格式：**
   - 返回完整的邮件内容，包括主题和正文

## 资源文件

- `resources/templates/welcome_email.md` - 欢迎邮件模板
- `resources/templates/notification_email.md` - 通知邮件模板
- `resources/templates/reminder_email.md` - 提醒邮件模板
- `resources/config.json` - 配置文件

## 示例

**用户输入：** "生成一封欢迎邮件，收件人是张三"

**预期输出：**
```
主题：欢迎加入我们！

亲爱的张三，

欢迎加入我们的团队！我们很高兴您能成为我们的一员。

如果您有任何问题，请随时联系我们。

祝好！
团队
```


