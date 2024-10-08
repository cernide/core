from core.common.apis.regex import (
    OWNER_NAME_PATTERN,
    PROJECT_NAME_PATTERN,
    VERSION_NAME_PATTERN,
)

URLS_PROJECT_COMPONENT_VERSIONS_LIST = r"^{}/{}/versions/component/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECT_COMPONENT_VERSIONS_NAMES = r"^{}/{}/versions/component/names/?$".format(
    OWNER_NAME_PATTERN,
    PROJECT_NAME_PATTERN,
)
URLS_PROJECT_COMPONENT_VERSIONS_DETAILS = r"^{}/{}/versions/component/{}/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
)
URLS_PROJECT_COMPONENT_VERSIONS_TRANSFER = (
    r"^{}/{}/versions/component/{}/transfer/?$".format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
    )
)
URLS_PROJECT_COMPONENT_VERSIONS_STAGES = (
    r"^{}/{}/versions/component/{}/stages/?$".format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
    )
)


URLS_PROJECT_MODEL_VERSIONS_LIST = r"^{}/{}/versions/model/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECT_MODEL_VERSIONS_NAMES = r"^{}/{}/versions/model/names/?$".format(
    OWNER_NAME_PATTERN,
    PROJECT_NAME_PATTERN,
)
URLS_PROJECT_MODEL_VERSIONS_DETAILS = r"^{}/{}/versions/model/{}/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
)
URLS_PROJECT_MODEL_VERSIONS_TRANSFER = r"^{}/{}/versions/model/{}/transfer/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
)
URLS_PROJECT_MODEL_VERSIONS_STAGES = r"^{}/{}/versions/model/{}/stages/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
)


URLS_PROJECT_ARTIFACT_VERSIONS_LIST = r"^{}/{}/versions/artifact/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN
)
URLS_PROJECT_ARTIFACT_VERSIONS_NAMES = r"^{}/{}/versions/artifact/names/?$".format(
    OWNER_NAME_PATTERN,
    PROJECT_NAME_PATTERN,
)
URLS_PROJECT_ARTIFACT_VERSIONS_DETAILS = r"^{}/{}/versions/artifact/{}/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
)
URLS_PROJECT_ARTIFACT_VERSIONS_TRANSFER = (
    r"^{}/{}/versions/artifact/{}/transfer/?$".format(
        OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
    )
)
URLS_PROJECT_ARTIFACT_VERSIONS_STAGES = r"^{}/{}/versions/artifact/{}/stages/?$".format(
    OWNER_NAME_PATTERN, PROJECT_NAME_PATTERN, VERSION_NAME_PATTERN
)
