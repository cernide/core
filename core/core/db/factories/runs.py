import factory

from core.db.defs import Models
from core.db.factories.projects import ProjectFactory
from core.db.factories.users import UserFactory
from polyaxon.schemas import ManagedBy


class RunFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    project = factory.SubFactory(ProjectFactory)
    original = None
    pipeline = None
    managed_by = ManagedBy.USER

    class Meta:
        model = Models.Run
