from core.common import conf
from core.common.options.registry import stats

conf.subscribe(stats.StatsDefaultPrefix)
