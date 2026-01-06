# 文档处理 Skill

## 描述

这个 Skill 提供了处理 Word、Excel 和 PDF 文档的能力，支持读取、转换和提取信息。

## 用途

处理各种格式的文档，包括：
- Word 文档（.docx）的读取和内容提取
- Excel 文件（.xlsx）的数据读取和分析
- PDF 文件的文本提取

## 指令

当用户要求处理文档时，请按照以下规则操作：

### Word 文档处理

1. **参数说明：**
   - `action`: 操作类型，可选值：`read`（读取）、`extract_text`（提取文本）、`get_metadata`（获取元数据）
   - `file_path`: Word 文档路径（必填）

2. **处理流程：**
   - 调用 `scripts/word_processor.py` 脚本
   - 根据 action 参数执行相应操作
   - 返回处理结果

### Excel 文档处理

1. **参数说明：**
   - `action`: 操作类型，可选值：`read_sheet`（读取工作表）、`get_cell`（获取单元格）、`analyze_data`（数据分析）
   - `file_path`: Excel 文件路径（必填）
   - `sheet_name`: 工作表名称（可选，默认第一个工作表）
   - `cell_range`: 单元格范围（可选，如 "A1:B10"）

2. **处理流程：**
   - 调用 `scripts/excel_processor.py` 脚本
   - 根据 action 参数执行相应操作
   - 返回处理结果

### PDF 文档处理

1. **参数说明：**
   - `action`: 操作类型，可选值：`extract_text`（提取文本）、`get_pages`（获取页数）、`extract_tables`（提取表格）
   - `file_path`: PDF 文件路径（必填）

2. **处理流程：**
   - 调用 `scripts/pdf_processor.py` 脚本
   - 根据 action 参数执行相应操作
   - 返回处理结果

## 脚本调用

- Word: `python scripts/word_processor.py <action> <file_path> [options]`
- Excel: `python scripts/excel_processor.py <action> <file_path> [options]`
- PDF: `python scripts/pdf_processor.py <action> <file_path> [options]`

## 示例

**用户输入：** "读取 Word 文档 /path/to/document.docx 的内容"

**预期输出：** 文档的完整文本内容

**用户输入：** "分析 Excel 文件 /path/to/data.xlsx 的数据"

**预期输出：** 数据分析结果（行数、列数、统计信息等）

**用户输入：** "提取 PDF 文件 /path/to/document.pdf 的文本"

**预期输出：** PDF 文档的文本内容


