# API 集成 Skill

这个示例展示了如何创建集成外部 API 的 Skills。

## 文件结构

```
06-api-integration/
├── SKILL.md
├── scripts/
│   └── api_client.py
└── README.md
```

## 功能

- 通用 API 调用支持
- 多种 HTTP 方法（GET、POST、PUT、DELETE）
- 多种认证方式（API Key、Bearer Token、Basic Auth）
- 自动重试机制
- 错误处理

## 使用方法

1. 安装依赖：
   ```bash
   pip install requests
   ```

2. 启用这个 Skill

3. 使用示例：
   - "获取北京的天气信息"
   - "调用 API https://api.example.com/data"
   - "使用 Bearer token 调用 API"

## 说明

这个示例展示了：
- 如何集成外部 API
- 如何处理不同的认证方式
- 如何实现重试机制
- 如何格式化 API 响应
- 错误处理和超时设置

## 依赖

- Python 3.x
- requests

## 注意事项

- 示例中的 API URL 需要替换为真实的 API 端点
- 认证信息应该安全存储，不要硬编码在脚本中
- 生产环境中应该使用环境变量或配置文件管理 API 密钥


