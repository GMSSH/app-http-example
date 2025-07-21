#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@文件        :main.py
@说明        :Sanic HTTP 服务启动入口
@时间        :2025/07/08 10:20:30
@作者        :xxx
@邮箱        :xxxxx@xxx.com
@版本        :1.0.0
"""
import os

# python3 -m nuitka --follow-imports --standalone --show-progress --include-data-files=config.yaml=config.yaml --include-data-dir=app/i18n=app/i18n  main.py

import socket

from app.consts import setting
from app.server import app


def get_random_free_port():
    """让操作系统自动分配一个未被占用的端口,确保"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def write_port_file(port):
    """将随机分配的端口写入文件"""
    if os.path.exists(setting.APP_TMP_PATH):
        with open(setting.APP_PORT_FILE_PATH, "w") as f:
            f.write(str(port))


if __name__ == "__main__":
    # 获取一个随机空闲端口
    port = get_random_free_port()
    write_port_file(port)
    # 启动服务
    app.run(host="127.0.0.1", port=port, debug=True, single_process=True)
