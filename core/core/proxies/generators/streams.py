from typing import Optional

from core.proxies.generators.base import write_to_conf_file
from core.proxies.schemas.server import get_server_config
from core.proxies.schemas.streams import get_base_config


def generate_streams_conf(path: Optional[str] = None, root: Optional[str] = None):
    write_to_conf_file(
        "polyaxon.main",
        get_server_config(root=root, use_upstream=True, use_redirect=False),
        path,
    )
    write_to_conf_file("polyaxon.base", get_base_config(), path)
