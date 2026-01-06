# 06｜脚本集成：把确定性交给代码，把解释性交给模型

关键词：cursor, claude code, skills, skill

Git 链接：
- 仓库：[shinjiyu/skills_all_in_one](https://github.com/shinjiyu/skills_all_in_one)
- 本文：[docs/wechat-series/06-script-integration-as-contract/README.md](https://github.com/shinjiyu/skills_all_in_one/blob/main/docs/wechat-series/06-script-integration-as-contract/README.md)

Skills 一旦进入“需要计算/处理文件/API 请求”的场景，最容易出问题的点只有一个：你让模型去“猜”。正确姿势是：**确定性工作交给脚本，模型负责解释、组织与对外表达**。

## 1）脚本与 Skill 的分工

- **脚本**：读取、计算、校验、调用 API、输出结构化结果（JSON/表格/字段）
- **Skill**：定义输入边界、调用脚本的参数、把结构化结果翻译成“人能读懂的交付物”

这样分工的好处是：结果可复现、可测试、可回归。

## 2）本仓库的现成例子

你可以直接看这些路径理解“分工”：

- `examples/03-script-integration/scripts/file_stats.py`：确定性统计
- `examples/scripts/data_validator.js`：数据校验
- `examples/06-api-integration/scripts/api_client.py`：API 客户端

它们共同体现一个原则：**脚本输出越结构化，Skill 输出越稳定**。

## 3）如何让脚本输出“更适合 Skill 消费”

推荐输出包含三层：

1. **摘要字段**：总数、耗时、成功/失败
2. **详情列表**：Top N、异常条目
3. **错误信息**：错误类型 + 可行动建议（而不是堆栈原样输出）

如果脚本只输出一段自然语言，Skill 反而难做“稳定排版”。

## 4）判断题（欢迎评论区回复“对/错”）

**判断题：** 当任务需要确定性处理时，让脚本输出结构化结果（如 JSON 字段）通常比输出一段自然语言更适合被 Skill 消费。（对 / 错？）

