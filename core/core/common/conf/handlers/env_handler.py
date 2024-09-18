import os

from typing import Any

from core.common.conf.exceptions import ConfException
from core.common.conf.handler import BaseConfHandler
from core.common.options.option import Option


class EnvConfHandler(BaseConfHandler):
    def get(self, option: Option, **kwargs) -> Any:  # pylint:disable=arguments-differ
        value = os.environ.get(option.key)
        if value:
            return option.parse(value)
        if not option.is_optional:
            raise ConfException(
                "The config option `{}` was not found or not correctly "
                "set on the settings backend.".format(option.key)
            )
        return option.default_value()

    def set(  # pylint:disable=arguments-differ
        self, option: Option, value: Any, **kwargs
    ):
        os.environ[option.key] = str(value)

    def delete(self, option: Option, **kwargs):  # pylint:disable=arguments-differ
        os.environ.pop(option.key, None)
