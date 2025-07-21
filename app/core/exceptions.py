#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import http
from typing import Optional

from app.core.response import custom_response


class CustomBaseException(Exception):
    """基础异常"""

    def __init__(
        self,
        message=http.HTTPStatus.BAD_REQUEST.description,
        code=http.HTTPStatus.BAD_REQUEST.value,
        data: Optional[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.message = message
        self.code = code
        self.data = data

    def __str__(self):
        """返回异常的字符串表示"""
        return f"CustomBaseException(code={self.code}, message='{self.message}', data={self.data})"

    def to_response(self):
        """返回 JSONResponse 对象"""
        return custom_response(code=self.code, data=self.data, msg=self.message)


class UnauthorizedError(CustomBaseException):
    """未授权异常"""


class ValidationError(CustomBaseException):
    """验证异常"""


class RuntimeError(CustomBaseException):
    """ """


class FileNotFoundError(CustomBaseException):
    """ """


class ValueError(CustomBaseException):
    """ """


class AttributeError(CustomBaseException):
    """ """


class TypeError(CustomBaseException):
    """ """
