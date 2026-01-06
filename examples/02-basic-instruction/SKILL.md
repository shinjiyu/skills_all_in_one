# 基础指令 Skill

## 描述

这个 Skill 演示了如何编写包含参数的基础指令，用于处理简单的文本转换任务。

## 用途

将用户输入的文本转换为大写、小写或首字母大写格式。

## 指令

当用户要求转换文本格式时，请按照以下规则处理：

1. **参数说明：**
   - `text`: 需要转换的文本（必填）
   - `format`: 转换格式，可选值：`uppercase`（大写）、`lowercase`（小写）、`capitalize`（首字母大写）

2. **处理逻辑：**
   - 如果 format 为 `uppercase`，将文本转换为全大写
   - 如果 format 为 `lowercase`，将文本转换为全小写
   - 如果 format 为 `capitalize`，将每个单词的首字母大写
   - 如果未指定 format，默认使用 `capitalize`

3. **输出格式：**
   - 返回转换后的文本
   - 如果参数缺失，提示用户提供必要信息

## 示例

**用户输入：** "将 'hello world' 转换为大写"

**预期输出：** "HELLO WORLD"

**用户输入：** "将 'HELLO WORLD' 转换为小写"

**预期输出：** "hello world"

**用户输入：** "将 'hello world' 首字母大写"

**预期输出：** "Hello World"


