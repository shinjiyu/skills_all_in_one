#!/usr/bin/env python3
"""
PDF 文档处理脚本
支持提取文本、获取页数和提取表格
"""

import sys
import os

try:
    import PyPDF2
except ImportError:
    print("错误: 请安装 PyPDF2 库")
    print("安装命令: pip install PyPDF2")
    sys.exit(1)


def extract_text(file_path):
    """提取 PDF 文本内容"""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = []
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content.append(page.extract_text())
            
            return {
                "success": True,
                "text": "\n".join(text_content),
                "pages": len(pdf_reader.pages)
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def get_pages(file_path):
    """获取 PDF 页数"""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            return {
                "success": True,
                "pages": len(pdf_reader.pages)
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def extract_tables(file_path):
    """提取 PDF 中的表格（基础实现）"""
    # 注意：PyPDF2 不直接支持表格提取
    # 这里返回提示信息，实际应用中可能需要使用其他库如 pdfplumber
    return {
        "success": False,
        "message": "表格提取功能需要使用 pdfplumber 库，当前使用 PyPDF2 仅支持文本提取"
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("错误: 参数不足")
        print("用法: python pdf_processor.py <action> <file_path>")
        print("action: extract_text, get_pages, extract_tables")
        sys.exit(1)
    
    action = sys.argv[1]
    file_path = sys.argv[2]
    
    if not os.path.exists(file_path):
        print(f"错误: 文件不存在: {file_path}")
        sys.exit(1)
    
    if action == "extract_text":
        result = extract_text(file_path)
        if result["success"]:
            print(f"页数: {result['pages']}")
            print("\n文本内容:")
            print(result["text"])
        else:
            print(f"错误: {result['error']}")
            sys.exit(1)
    
    elif action == "get_pages":
        result = get_pages(file_path)
        if result["success"]:
            print(f"页数: {result['pages']}")
        else:
            print(f"错误: {result['error']}")
            sys.exit(1)
    
    elif action == "extract_tables":
        result = extract_tables(file_path)
        print(result.get("message", "功能暂未实现"))
    
    else:
        print(f"错误: 未知的操作类型: {action}")
        sys.exit(1)


