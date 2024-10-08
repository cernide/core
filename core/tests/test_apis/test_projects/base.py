from core.db.factories.projects import ProjectFactory
from core.db.factories.runs import RunFactory
from core.db.factories.users import UserFactory
from core.db.models.projects import Project
from polyaxon.api import API_V1
from tests.base.case import BaseTest


class BaseTestProjectApi(BaseTest):
    model_class = Project
    factory_class = ProjectFactory

    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.project = self.factory_class()
        self.url = "/{}/{}/{}/".format(API_V1, self.user.username, self.project.name)
        self.queryset = self.model_class.objects.filter()
        self.object_query = self.model_class.objects.get(id=self.project.id)

        # Create related fields
        for _ in range(2):
            RunFactory(user=self.user, project=self.project)
