# Setting values to None means using defaults

from core import pkg
from polyaxon import _dist

ENCRYPTION_BACKEND = None
CONF_CHECK_OWNERSHIP = False
AUDITOR_BACKEND = None
AUDITOR_EVENTS_TASK = None
WORKERS_BACKEND = None
EXECUTOR_BACKEND = "core.orchestration.executor.service.ExecutorService"
WORKERS_SERVICE = "core.common.workers"
HANDLERS_SERVICE = "core.orchestration.executor.handlers.APIHandler"
EXECUTOR_SERVICE = "core.orchestration.executor"
OPERATIONS_BACKEND = None
PLATFORM_VERSION = pkg.VERSION
PLATFORM_DIST = _dist.CE
CONF_BACKEND = "core.common.conf.service.ConfService"
STORE_OPTION = "env"
K8S_IN_CLUSTER = True
PERMISSIONS_MAPPING = None
HAS_ORG_MANAGEMENT = False
