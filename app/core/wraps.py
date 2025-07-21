#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :HttpExample 
@File    :wraps.py
@IDE     :PyCharm 
@Date    :2025/7/8 15:43
@Author  :xiaozheng
"""
import os
from functools import wraps

import loguru
from sanic.request import Request

from app.core.i18n import GI18n


def with_lang(handler):
    @wraps(handler)
    async def wrapper(request: Request, *args, **kwargs):
        lang = (
            request.args.get("lang")
            or (request.json or {}).get("lang")
            or (request.form or {}).get("lang")
            or "en"
        )
        current_path = os.path.dirname(os.path.abspath(__file__))
        current_path = os.path.dirname(current_path)
        i18n_path = os.path.join(current_path,"i18n")
        loguru.logger.info(f"i18n_path: {i18n_path}, lang: {lang}")
        # 进行国际化设置
        GI18n(i18n_path, lang)
        return await handler(request)
    return wrapper