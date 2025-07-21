#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@文件        :server.py
@说明        :Sanic HTTP 服务器
@时间        :2025/07/08 10:20:30
@作者        :xxx
@邮箱        :xxxxx@xxx.com
@版本        :1.0.0
"""
import os
import yaml
from loguru import logger


def load_config():
    """加载配置文件"""
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config.yaml')
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"加载配置文件失败: {e}")
        return {}


def setup_logger(config):
    """配置日志"""
    if config.get('logger'):
        logger_config = config['logger']
        logger.add(
            logger_config.get('sink', 'app.log'),
            level=logger_config.get('level', 'DEBUG'),
            rotation=logger_config.get('rotation', '500 MB'),
            retention=logger_config.get('retention', '1 months'),
            compression=logger_config.get('compression', 'tar'),
            format=logger_config.get('format', '{time} | {level} | {message}'),
            diagnose=logger_config.get('diagnose', False),
            enqueue=logger_config.get('enqueue', True)
        )


# 全局配置实例
config = load_config()
setup_logger(config)