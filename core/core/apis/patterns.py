from django.urls import include, re_path

from core.common.apis.index import get_urlpatterns, handler403, handler404, handler500
from core.common.apis.regex import OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
from core.streams.endpoints.agents import agent_routes, internal_agent_routes
from core.streams.endpoints.artifacts import artifacts_routes
from core.streams.endpoints.auth_request import auth_request_routes
from core.streams.endpoints.events import events_routes
from core.streams.endpoints.k8s import k8s_routes
from core.streams.endpoints.logs import internal_logs_routes, logs_routes
from core.streams.endpoints.notifications import notifications_routes
from polyaxon.api import API_V1, AUTH_REQUEST_V1, INTERNAL_V1, STREAMS_V1

api_patterns = [
    re_path(
        r"", include(("core.apis.versions.urls", "versions"), namespace="versions")
    ),
    re_path(r"", include(("core.apis.agents.urls", "agents"), namespace="agents")),
    re_path(
        r"",
        include(
            ("core.apis.project_resources.urls", "project_resources"),
            namespace="project_resources",
        ),
    ),
    re_path(
        r"",
        include(
            ("core.apis.run_lineage.urls", "run_lineage"), namespace="run_lineage"
        ),
    ),
    re_path(r"", include(("core.apis.runs.urls", "runs"), namespace="runs")),
    re_path(
        r"", include(("core.apis.projects.urls", "projects"), namespace="projects")
    ),
]


# UI
projects_urls = "{}/{}".format(OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN)
orgs_urls = "orgs/{}".format(OWNER_NAME_PATTERN)
ui_urlpatterns = [
    r"^$",
    r"^{}/?".format(orgs_urls),
    r"^{}/.*/?".format(orgs_urls),
    # Projects
    r"^{}/?$".format(projects_urls),
    r"^{}/runs.*/?".format(projects_urls),
    r"^{}/job.*/?".format(projects_urls),
    r"^{}/service.*/?".format(projects_urls),
    r"^{}/matrix.*/?".format(projects_urls),
    r"^{}/matrices.*/?".format(projects_urls),
    r"^{}/dag.*/?".format(projects_urls),
    r"^{}/schedule.*/?".format(projects_urls),
    r"^{}/artifacts.*/?".format(projects_urls),
    r"^{}/components.*/?".format(projects_urls),
    r"^{}/models.*/?".format(projects_urls),
    r"^{}/dashboards.*/?".format(projects_urls),
    r"^{}/reports.*/?".format(projects_urls),
    r"^{}/searches.*/?".format(projects_urls),
    r"^{}/cli.*/?".format(projects_urls),
    r"^{}/settings.*/?".format(projects_urls),
    r"^{}/new.*/?".format(projects_urls),
]

# Streams
streams_routes = (
    agent_routes
    + logs_routes
    + k8s_routes
    + notifications_routes
    + artifacts_routes
    + events_routes
)
app_urlpatterns = [
    re_path(
        r"^{}/".format(INTERNAL_V1),
        include(
            (internal_agent_routes + internal_logs_routes, "internal-v1"),
            namespace="internal-v1",
        ),
    ),
    re_path(
        r"^{}/".format(AUTH_REQUEST_V1),
        include((auth_request_routes, "auth-request-v1"), namespace="auth-request-v1"),
    ),
    re_path(
        r"^{}/".format(STREAMS_V1),
        include((streams_routes, "streams-v1"), namespace="streams-v1"),
    ),
    re_path(
        r"^{}/".format(API_V1), include((api_patterns, "api-v1"), namespace="api-v1")
    ),
]

handler404 = handler404
handler403 = handler403
handler500 = handler500
urlpatterns = get_urlpatterns(
    app_patterns=app_urlpatterns, no_healthz=False, ui_urlpatterns=ui_urlpatterns
)
