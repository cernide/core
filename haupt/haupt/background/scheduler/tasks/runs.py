import logging

from typing import Dict, List

from haupt.background.celeryp.tasks import SchedulerCeleryTasks
from haupt.common import workers
from haupt.orchestration.scheduler.manager import RunsManager
from haupt.polyconf.settings import Intervals

_logger = logging.getLogger("polyaxon.scheduler")


@workers.app.task(name=SchedulerCeleryTasks.RUNS_PREPARE, ignore_result=True)
def runs_prepare(run_id):
    RunsManager.runs_prepare(run_id=run_id, run=None)


@workers.app.task(name=SchedulerCeleryTasks.RUNS_HOOKS, ignore_result=True)
def runs_hooks(run_id):
    RunsManager.runs_hooks(run_id=run_id, run=None)


@workers.app.task(name=SchedulerCeleryTasks.RUNS_START, ignore_result=True)
def runs_start(run_id):
    RunsManager.runs_start(run_id=run_id, run=None)


@workers.app.task(name=SchedulerCeleryTasks.RUNS_BUILT, ignore_result=True)
def runs_built(run_id):
    RunsManager.runs_built(run_id=run_id)


@workers.app.task(name=SchedulerCeleryTasks.RUNS_SET_ARTIFACTS, ignore_result=True)
def runs_set_artifacts(run_id, artifacts: List[Dict]):
    RunsManager.runs_set_artifacts(run_id=run_id, run=None, artifacts=artifacts)


@workers.app.task(
    name=SchedulerCeleryTasks.RUNS_STOP,
    bind=True,
    max_retries=3,
    ignore_result=True,
)
def runs_stop(self, run_id, update_status=False, message=None):
    stopped = RunsManager.runs_stop(
        run_id=run_id, run=None, update_status=update_status, message=message
    )
    if not stopped and self.request.retries < 2:
        _logger.info("Trying again to delete job `%s` in run.", run_id)
        self.retry(countdown=Intervals.RUNS_SCHEDULER)
        return
