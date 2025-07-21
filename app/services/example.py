"""
@文件        :__init__.py
@说明        :example
@时间        :2025/07/08 10:20:30
@作者        :xxx
@邮箱        :xxxxx@xxx.com
@版本        :1.0.0
"""

from app.core.exceptions import CustomBaseException
from app.core.i18n import T as i18n
class Example:
    """ Example class """
    async def hello(self, name):
        """ """
        return f"Hello {name}"