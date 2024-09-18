from django.test import TestCase

from core.db.factories.projects import ProjectFactory
from core.db.factories.runs import RunFactory
from core.db.factories.users import UserFactory


class BaseTestQuery(TestCase):
    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.project = ProjectFactory()
        self.run = RunFactory(project=self.project)
