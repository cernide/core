from haupt.background.celeryp.tasks import CoreSchedulerCeleryTasks
from haupt.common import conf
from haupt.common.options.registry.core import SCHEDULER_ENABLED
from haupt.orchestration.scheduler import manager
from polyaxon.constants.metadata import META_EAGER_MODE
from polyaxon.lifecycle import V1Statuses


def handle_run_created(workers_backend, event: "Event") -> None:  # noqa: F821
    """Handles creation, resume, and restart"""
    eager = False
    if (
        event.instance
        and event.instance.status != V1Statuses.RESUMING
        and (event.instance.meta_info or {}).get(META_EAGER_MODE)
    ):
        eager = True
    if not eager:
        eager = (
            not event.data["is_managed"]
            and event.instance
            and event.instance.content is not None
        )
    # Run is not managed by Polyaxon
    if not event.data["is_managed"] and not eager:
        return
    # Run is managed by a pipeline
    if event.data.get("pipeline_id") is not None:
        return
    # Run is pending
    if event.instance.pending is not None:
        return

    workers_backend.send(
        CoreSchedulerCeleryTasks.RUNS_PREPARE,
        delay=conf.get(SCHEDULER_ENABLED) and not eager,
        kwargs={"run_id": event.instance_id},
        eager_kwargs={"run": event.instance, "eager": eager},
    )


def handle_run_approved_triggered(
    workers_backend, event: "Event"
) -> None:  # noqa: F821
    run = manager.get_run(run_id=event.instance_id, run=event.instance)
    if not run:
        return

    # Check if it should prepare
    if run.status == V1Statuses.CREATED:
        workers_backend.send(
            CoreSchedulerCeleryTasks.RUNS_PREPARE,
            kwargs={"run_id": event.instance_id},
            eager_kwargs={"run": event.instance},
        )
        return
    if run.is_managed:
        workers_backend.send(
            CoreSchedulerCeleryTasks.RUNS_START,
            kwargs={"run_id": event.instance_id},
            eager_kwargs={"run": event.instance},
        )


def handle_run_stopped_triggered(workers_backend, event: "Event") -> None:  # noqa: F821
    run = manager.get_run(run_id=event.instance_id, run=event.instance)
    if not run:
        return

    if run.is_managed:
        workers_backend.send(
            CoreSchedulerCeleryTasks.RUNS_STOP,
            kwargs={"run_id": event.instance_id},
            eager_kwargs={"run": event.instance},
        )


def handle_new_artifacts(workers_backend, event: "Event") -> None:  # noqa: F821
    artifacts = event.data.get("artifacts")
    if not artifacts:
        return

    workers_backend.send(
        CoreSchedulerCeleryTasks.RUNS_SET_ARTIFACTS,
        kwargs={"run_id": event.instance_id, "artifacts": artifacts},
        eager_kwargs={"run": event.instance},
    )


def handle_run_deleted(workers_backend, event: "Event") -> None:  # noqa: F821
    run = manager.get_run(run_id=event.instance_id, run=event.instance)
    if not run:
        return

    if not run.is_managed:
        run.delete()
        return

    run.delete_in_progress()
    workers_backend.send(
        CoreSchedulerCeleryTasks.RUNS_DELETE,
        kwargs={"run_id": run.id},
        eager_kwargs={"run": run},
    )
