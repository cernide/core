from django.db import models

from core.db.abstracts.describable import DescribableModel
from core.db.abstracts.diff import DiffModel
from core.db.abstracts.live_state import LiveStateModel
from core.db.abstracts.nameable import RequiredNameableModel
from core.db.abstracts.tag import TagModel
from core.db.abstracts.uid import UuidModel


class BaseCatalog(
    UuidModel,
    RequiredNameableModel,
    DiffModel,
    DescribableModel,
    TagModel,
):
    class Meta:
        abstract = True
        indexes = [models.Index(fields=["name"])]


class BaseLiveStateCatalog(
    BaseCatalog,
    LiveStateModel,
):
    class Meta:
        abstract = True
        indexes = [models.Index(fields=["name"])]
