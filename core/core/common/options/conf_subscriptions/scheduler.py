from core.common import conf
from core.common.options.registry import scheduler

conf.subscribe(scheduler.SchedulerCountdown)
