from core.polyconf.settings import PLATFORM_CONFIG

if PLATFORM_CONFIG.is_scheduler_service:
    urlpatterns = []
elif PLATFORM_CONFIG.is_streams_service:
    from core.streams.patterns import *  # noqa
else:
    from core.apis.patterns import *  # noqa
