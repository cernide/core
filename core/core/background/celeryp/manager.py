from core.orchestration.crons.deletion import CronsDeletionManager
from core.orchestration.crons.heartbeats import CronsHeartbeatManager
from core.orchestration.crons.stats import CronsStatsManager
from core.orchestration.scheduler.manager import SchedulingManager


class BackgroundManager(
    SchedulingManager,
    CronsDeletionManager,
    CronsHeartbeatManager,
    CronsStatsManager,
):
    pass
