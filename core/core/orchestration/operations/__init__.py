from django.conf import settings

from core.common.service_interface import LazyServiceWrapper
from core.orchestration.operations.service import OperationInitSpec, OperationsService


def get_operation_backend_path():
    return (
        settings.OPERATIONS_BACKEND
        or "core.orchestration.operations.service.OperationsService"
    )


backend = LazyServiceWrapper(
    backend_base=OperationsService,
    backend_path=get_operation_backend_path(),
    options={},
)
backend.expose(locals())
