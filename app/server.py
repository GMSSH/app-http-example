"""
@文件        :server.py
@说明        :Sanic HTTP 服务器
@时间        :2025/07/08 10:20:30
@作者        :xxx
@邮箱        :xxxxx@xxx.com
@版本        :1.0.0
"""

from sanic import Sanic, Request
from sanic.response import json
from sanic_cors import CORS

from app.core.wraps import with_lang
from app.services.example import Example
from app.core.response import success_response
from app.middlewares.example import setup_middlewares, setup_error_handlers

# 创建 Sanic 应用
app = Sanic("HttpExampleApp")

# 启用 CORS
CORS(app)

# 设置中间件和错误处理
setup_middlewares(app)
setup_error_handlers(app)


@app.get("/ping")
async def ping(request: Request):
    """Ping 接口,用于状态检查"""
    return json({"code": 200, "msg": "pong"})


@app.post("/hello")
@with_lang
async def hello(request: Request):
    """Hello 接口"""
    body = request.json or {}
    name = body.get("name", "World")

    hello_obj = Example()
    result = await hello_obj.hello(name)
    return success_response(data=result, endpoint=request.path)
