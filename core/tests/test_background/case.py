from core.common.test_cases.base import PolyaxonBaseTest
from core.db.factories.projects import ProjectFactory
from core.db.factories.users import UserFactory


class BaseTest(PolyaxonBaseTest):
    def setUp(self):
        super().setUp()
        # Force tasks autodiscover
        from core.background.scheduler import tasks  # noqa

        self.user = UserFactory()
        self.project = ProjectFactory()
