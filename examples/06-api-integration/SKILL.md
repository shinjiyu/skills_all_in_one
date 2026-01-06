# API 集成 Skill

## 描述

这个 Skill 演示了如何集成外部 API，用于获取和处理数据。

## 用途

调用外部 API 获取数据，支持多种 API 类型和认证方式。

## 指令

当用户要求调用 API 时，请按照以下规则操作：

### 通用 API 调用

1. **参数说明：**
   - `api_url`: API 端点 URL（必填）
   - `method`: HTTP 方法，可选值：`GET`、`POST`、`PUT`、`DELETE`（默认：GET）
   - `headers`: 请求头（可选，JSON 格式）
   - `data`: 请求数据（可选，JSON 格式，用于 POST/PUT）
   - `auth_type`: 认证类型，可选值：`none`、`api_key`、`bearer`、`basic`
   - `auth_value`: 认证值（根据 auth_type 提供）

2. **处理流程：**
   - 调用 `scripts/api_client.py` 脚本
   - 传递所有参数
   - 处理响应数据
   - 返回格式化结果

3. **错误处理：**
   - 网络错误：重试 3 次，每次间隔 1 秒
   - HTTP 错误：返回错误状态码和消息
   - 超时：设置 30 秒超时

### 特定 API 示例

#### 天气 API
- **用途：** 获取指定城市的天气信息
- **参数：** `city`（城市名称）
- **调用：** `python scripts/api_client.py weather <city>`

#### 新闻 API
- **用途：** 获取最新新闻
- **参数：** `category`（分类，可选）
- **调用：** `python scripts/api_client.py news [category]`

## 脚本调用

```bash
python scripts/api_client.py <api_type> <parameters>
```

或通用调用：
```bash
python scripts/api_client.py call <api_url> [options]
```

## 示例

**用户输入：** "获取北京的天气信息"

**预期输出：**
```
城市: 北京
温度: 25°C
天气: 晴天
湿度: 60%
```

**用户输入：** "调用 API https://api.example.com/data，使用 Bearer token 认证"

**预期输出：** API 返回的数据（格式化后）


