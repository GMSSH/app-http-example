#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project :HttpExample
@File    :setting.py
@IDE     :PyCharm
@Date    :2025/7/10 09:59
@Author  :xiaozheng
"""
import os.path

APP_NAME = "official/example"
GM_BASE_PATH = "/.__gmssh/plugin"
APP_BASE_PATH = os.path.join(GM_BASE_PATH, APP_NAME)
APP_TMP_PATH = os.path.join(APP_BASE_PATH, "tmp")
APP_PORT_FILE_PATH = os.path.join(APP_BASE_PATH, "app.port")
