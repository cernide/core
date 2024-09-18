from django.conf import settings

from core.common.options import option_namespaces, option_subjects
from core.common.options.cache import LONG_CACHE_TTL
from core.common.options.option import (
    NAMESPACE_DB_OPTION_MARKER,
    Option,
    OptionScope,
    OptionStores,
)

STATS_DEFAULT_PREFIX = "{}{}{}".format(
    option_namespaces.STATS, NAMESPACE_DB_OPTION_MARKER, option_subjects.DEFAULT_PREFIX
)

OPTIONS = {STATS_DEFAULT_PREFIX}


class StatsDefaultPrefix(Option):
    key = STATS_DEFAULT_PREFIX
    scope = OptionScope.GLOBAL
    is_secret = False
    is_optional = True
    is_list = False
    typing = "str"
    store = OptionStores(settings.STORE_OPTION)
    default = None
    options = None
    cache_ttl = LONG_CACHE_TTL
