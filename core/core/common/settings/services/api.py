from typing import Dict, List, Optional, Tuple

from core.common.settings.apps import set_apps
from core.common.settings.assets import set_assets
from core.common.settings.celery import set_celery
from core.common.settings.core import set_core
from core.common.settings.cors import set_cors
from core.common.settings.middlewares import set_middlewares
from core.common.settings.ui import set_ui
from core.schemas.platform_config import PlatformConfig


def set_api_service(
    context,
    config: PlatformConfig,
    api_apps: Tuple,
    routes: Dict,
    db_app: Optional[str] = None,
    processors: Optional[List[str]] = None,
    enable_crsf: bool = False,
):
    project_apps = (
        "core.common.apis.apps.CommonApisConfig",
        "core.common.commands.apps.CommandsConfig",
    ) + api_apps
    set_apps(
        context=context,
        config=config,
        third_party_apps=("rest_framework", "corsheaders"),
        project_apps=project_apps,
        db_app=db_app,
        use_db_apps=True,
        use_admin_apps=True,
        use_staticfiles_app=True,
    )
    set_core(context=context, config=config, use_db=True)
    set_cors(context=context, config=config)
    set_ui(context=context, config=config, processors=processors)
    set_middlewares(context=context, config=config, enable_crsf=enable_crsf)
    set_assets(context=context, config=config)
    if config.scheduler_enabled:
        set_celery(context=context, config=config, routes=routes)


def set_service(context, config: PlatformConfig):
    from core.background.celeryp.routes import get_routes

    api_apps = (
        "core.apis.apps.APIsConfig",
        "core.streams.apps.StreamsConfig",
    )
    set_api_service(
        context, config, api_apps=api_apps, routes=get_routes(), db_app=None
    )
