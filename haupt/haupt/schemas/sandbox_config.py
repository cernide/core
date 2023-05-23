from typing import Optional

from clipped.utils.http import clean_host
from pydantic import Field, StrictInt, StrictStr

from polyaxon.env_vars.keys import (
    EV_KEYS_K8S_NAMESPACE,
    EV_KEYS_SANDBOX_DEBUG,
    EV_KEYS_SANDBOX_HOST,
    EV_KEYS_SANDBOX_IS_LOCAL,
    EV_KEYS_SANDBOX_PER_CORE,
    EV_KEYS_SANDBOX_PORT,
    EV_KEYS_SANDBOX_SSL_ENABLED,
    EV_KEYS_SANDBOX_WORKERS,
)
from polyaxon.schemas.cli.agent_config import AgentConfig


class SandboxConfig(AgentConfig):
    _IDENTIFIER = "sandbox"

    namespace: Optional[StrictStr] = Field(
        alias=EV_KEYS_K8S_NAMESPACE, default="sandbox"
    )
    port: Optional[StrictInt] = Field(alias=EV_KEYS_SANDBOX_PORT)
    host: Optional[StrictStr] = Field(alias=EV_KEYS_SANDBOX_HOST)
    ssl_enabled: Optional[bool] = Field(alias=EV_KEYS_SANDBOX_SSL_ENABLED)
    debug: Optional[bool] = Field(alias=EV_KEYS_SANDBOX_DEBUG)
    workers: Optional[StrictInt] = Field(alias=EV_KEYS_SANDBOX_WORKERS)
    per_core: Optional[bool] = Field(alias=EV_KEYS_SANDBOX_PER_CORE)
    is_local: Optional[bool] = Field(alias=EV_KEYS_SANDBOX_IS_LOCAL)

    def __init__(
        self,
        host: Optional[str] = None,
        **data,
    ):
        super().__init__(
            host=clean_host(host) if host else host,
            **data,
        )
