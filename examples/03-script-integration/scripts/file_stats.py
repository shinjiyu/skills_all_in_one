#!/usr/bin/env python3
"""
文件统计脚本
统计文件的字符数、单词数和行数
"""

import sys
import os


def count_file_stats(file_path):
    """
    统计文件信息
    
    Args:
        file_path: 文件路径
        
    Returns:
        dict: 包含字符数、单词数、行数的字典
    """
    if not os.path.exists(file_path):
        return {
            "error": f"文件不存在: {file_path}"
        }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(content.splitlines())
        
        return {
            "char_count": char_count,
            "word_count": word_count,
            "line_count": line_count
        }
    except Exception as e:
        return {
            "error": f"读取文件时出错: {str(e)}"
        }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("错误: 请提供文件路径")
        print("用法: python file_stats.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    result = count_file_stats(file_path)
    
    if "error" in result:
        print(result["error"])
        sys.exit(1)
    
    print(f"字符数: {result['char_count']}")
    print(f"单词数: {result['word_count']}")
    print(f"行数: {result['line_count']}")


