# 文档处理 Skill

这个示例展示了如何创建处理 Word、Excel 和 PDF 文档的 Skills。

## 文件结构

```
05-document-processor/
├── SKILL.md
├── scripts/
│   ├── word_processor.py
│   ├── excel_processor.py
│   └── pdf_processor.py
└── README.md
```

## 功能

- **Word 文档处理：**
  - 读取文档内容
  - 提取文本
  - 获取元数据

- **Excel 文档处理：**
  - 读取工作表数据
  - 获取单元格值
  - 数据分析

- **PDF 文档处理：**
  - 提取文本内容
  - 获取页数
  - 基础表格提取（需要额外库）

## 使用方法

1. 安装依赖：
   ```bash
   pip install python-docx openpyxl PyPDF2
   ```

2. 启用这个 Skill

3. 使用示例：
   - "读取 Word 文档 <文件路径> 的内容"
   - "分析 Excel 文件 <文件路径> 的数据"
   - "提取 PDF 文件 <文件路径> 的文本"

## 说明

这个示例展示了：
- 如何处理多种文档格式
- 如何组织多个脚本文件
- 如何定义复杂的指令逻辑
- 错误处理和参数验证

## 依赖

- Python 3.x
- python-docx
- openpyxl
- PyPDF2


