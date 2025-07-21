"""
@文件        :__init__.py
@说明        :example
@时间        :2025/07/08 10:20:30
@作者        :xxx
@邮箱        :xxxxx@xxx.com
@版本        :1.0.0
"""

from sanic import Request
from loguru import logger
from app.core.response import error_response
from app.core.exceptions import CustomBaseException


# 中间件：请求日志
def setup_middlewares(app):
    @app.middleware('request')
    async def log_request(request: Request):
        """ """
        # logger.info(f"收到请求: {request.method} {request.url}")

    @app.middleware('response')
    async def log_response(request: Request, response):
        """ """
        # logger.info(f"响应请求: {request.method} {request.url} - 状态码: {response.status}")


def setup_error_handlers(app):
    """设置错误处理器"""

    # 捕获其他自定义异常
    @app.exception(CustomBaseException)
    async def handle_custom_base_exception(request: Request, exception):
        """ """
        return exception.to_response()

    # Exception 作为保底异常处理器
    @app.exception(Exception)
    async def handle_general_exception(request: Request, exception):
        """ """
        logger.error(f"未处理的异常: {exception}")
        return error_response(
            data={'error': str(exception)},
            msg='服务器内部错误',
            code=500,
            endpoint=request.path,
        )

    @app.exception(404)
    async def handle_not_found(request: Request, exception):
        return error_response(
            data={'path': request.path},
            msg='请求的资源不存在',
            code=404,
            endpoint=request.path,
        )
