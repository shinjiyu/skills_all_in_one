#!/usr/bin/env python3
"""
API 客户端脚本
支持多种 API 调用和认证方式
"""

import sys
import json
import time
import requests
from requests.auth import HTTPBasicAuth


def make_request(url, method="GET", headers=None, data=None, auth_type=None, auth_value=None, timeout=30, retries=3):
    """
    发送 HTTP 请求
    
    Args:
        url: API URL
        method: HTTP 方法
        headers: 请求头
        data: 请求数据
        auth_type: 认证类型
        auth_value: 认证值
        timeout: 超时时间（秒）
        retries: 重试次数
    """
    # 设置认证
    auth = None
    request_headers = headers or {}
    
    if auth_type == "api_key":
        request_headers["X-API-Key"] = auth_value
    elif auth_type == "bearer":
        request_headers["Authorization"] = f"Bearer {auth_value}"
    elif auth_type == "basic":
        username, password = auth_value.split(":", 1)
        auth = HTTPBasicAuth(username, password)
    
    # 重试逻辑
    for attempt in range(retries):
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=request_headers,
                json=data if isinstance(data, dict) else None,
                data=data if isinstance(data, str) else None,
                auth=auth,
                timeout=timeout
            )
            
            response.raise_for_status()
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text
            }
        
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(1)  # 等待 1 秒后重试
                continue
            return {
                "success": False,
                "error": str(e)
            }
    
    return {
        "success": False,
        "error": "请求失败，已达到最大重试次数"
    }


def get_weather(city):
    """获取天气信息（示例 API）"""
    # 注意：这里使用示例 API，实际使用时需要替换为真实的天气 API
    url = f"https://api.example.com/weather?city={city}"
    
    result = make_request(url, method="GET")
    
    if result["success"]:
        # 格式化输出
        data = result["data"]
        return {
            "success": True,
            "city": data.get("city", city),
            "temperature": data.get("temperature", "N/A"),
            "condition": data.get("condition", "N/A"),
            "humidity": data.get("humidity", "N/A")
        }
    
    return result


def get_news(category=None):
    """获取新闻（示例 API）"""
    url = "https://api.example.com/news"
    if category:
        url += f"?category={category}"
    
    result = make_request(url, method="GET")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("错误: 参数不足")
        print("用法:")
        print("  python api_client.py call <url> [options]")
        print("  python api_client.py weather <city>")
        print("  python api_client.py news [category]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "call":
        if len(sys.argv) < 3:
            print("错误: 请提供 API URL")
            sys.exit(1)
        
        url = sys.argv[2]
        method = sys.argv[3] if len(sys.argv) > 3 else "GET"
        
        result = make_request(url, method=method)
        
        if result["success"]:
            print(f"状态码: {result['status_code']}")
            print("\n响应数据:")
            print(json.dumps(result["data"], indent=2, ensure_ascii=False))
        else:
            print(f"错误: {result['error']}")
            sys.exit(1)
    
    elif command == "weather":
        if len(sys.argv) < 3:
            print("错误: 请提供城市名称")
            sys.exit(1)
        
        city = sys.argv[2]
        result = get_weather(city)
        
        if result["success"]:
            print(f"城市: {result['city']}")
            print(f"温度: {result['temperature']}°C")
            print(f"天气: {result['condition']}")
            print(f"湿度: {result['humidity']}%")
        else:
            print(f"错误: {result['error']}")
            sys.exit(1)
    
    elif command == "news":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        result = get_news(category)
        
        if result["success"]:
            print(json.dumps(result["data"], indent=2, ensure_ascii=False))
        else:
            print(f"错误: {result['error']}")
            sys.exit(1)
    
    else:
        print(f"错误: 未知命令: {command}")
        sys.exit(1)


