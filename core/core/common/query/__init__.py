from core.common.query.service import QueryService
from core.common.service_interface import LazyServiceWrapper

backend = LazyServiceWrapper(
    backend_base=QueryService,
    backend_path="core.common.query.service.QueryService",
    options={},
)
backend.expose(locals())
