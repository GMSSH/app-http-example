#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@文件        :response.py
@说明        :标准 API 响应格式封装
@时间        :2025/07/08 10:20:30
@作者        :xxx
@邮箱        :xxxxx@xxx.com
@版本        :1.0.0
"""

from sanic.response import json
from typing import Any
from app.core.i18n import T as i18n

def success_response(
    data: Any = None,
    msg: str = None,
    code: int = 200,
    endpoint: str = "",
    close: int = 0
) -> json:
    """
    成功响应格式
    
    Args:
        data: 响应数据
        msg: 响应消息
        code: 状态码，默认 200
        endpoint: API 端点
        close: 关闭标识，默认 0
    
    Returns:
        json: 标准格式的成功响应
    """
    msg = msg or i18n.translate("STATUS_OK")
    return json({
        'code': code,
        'data': data,
        'meta': {
            'close': close,
            'endpoint': endpoint
        },
        'msg': msg
    })


def error_response(
    data: Any = None,
    msg: str = None,
    code: int = 400,
    endpoint: str = "",
    close: int = 0
) -> json:
    """
    失败响应格式
    
    Args:
        data: 响应数据
        msg: 错误消息
        code: 错误状态码，默认 400
        endpoint: API 端点
        close: 关闭标识，默认 0
    
    Returns:
        json: 标准格式的错误响应
    """
    msg = msg or i18n.translate("STATUS_FAILED")
    return json({
        'code': code,
        'data': data,
        'meta': {
            'close': close,
            'endpoint': endpoint
        },
        'msg': msg,
    })


def custom_response(
    code: int,
    data: Any = None,
    msg: str = "",
    endpoint: str = "",
    close: int = 0
) -> json:
    """
    自定义响应格式
    
    Args:
        code: 状态码
        data: 响应数据
        msg: 响应消息
        endpoint: API 端点
        close: 关闭标识，默认 0
    
    Returns:
        json: 标准格式的自定义响应
    """
    return json({
        'code': code,
        'data': data,
        'meta': {
            'close': close,
            'endpoint': endpoint
        },
        'msg': msg
    })