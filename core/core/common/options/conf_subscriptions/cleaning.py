from core.common import conf
from core.common.options.registry import cleaning

conf.subscribe(cleaning.CleaningIntervalsActivityLogs)
conf.subscribe(cleaning.CleaningIntervalsNotifications)
conf.subscribe(cleaning.CleaningIntervalsArchives)
conf.subscribe(cleaning.CleaningIntervalsDeletion)
