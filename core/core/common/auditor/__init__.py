from django.conf import settings

from core.common.auditor.manager import event_manager
from core.common.auditor.service import AuditorService
from core.common.service_interface import LazyServiceWrapper


def get_auditor_backend_path():
    return settings.AUDITOR_BACKEND or "core.common.auditor.service.AuditorService"


def get_auditor_options():
    return {
        "auditor_events_task": settings.AUDITOR_EVENTS_TASK,
        "workers_service": settings.WORKERS_SERVICE,
        "executor_service": settings.EXECUTOR_SERVICE or "core.orchestration.executor",
    }


backend = LazyServiceWrapper(
    backend_base=AuditorService,
    backend_path=get_auditor_backend_path(),
    options=get_auditor_options(),
)
backend.expose(locals())

subscribe = event_manager.subscribe
