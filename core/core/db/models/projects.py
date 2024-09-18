from django.core.validators import validate_slug
from django.db import models

from core.common.validation.blacklist import validate_blacklist_name
from core.db.abstracts.catalogs import BaseLiveStateCatalog
from core.db.abstracts.contributors import ContributorsModel
from core.db.abstracts.projects import Actor, Owner
from core.db.abstracts.readme import ReadmeModel


class Project(BaseLiveStateCatalog, ReadmeModel, ContributorsModel):
    latest_stats = models.OneToOneField(
        "db.ProjectStats",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=128, validators=[validate_slug, validate_blacklist_name], unique=True
    )

    class Meta(BaseLiveStateCatalog.Meta):
        app_label = "db"
        db_table = "db_project"

    @property
    def owner(self):
        return Owner

    @property
    def owner_id(self):
        return Owner.id

    @property
    def actor(self):
        return Actor
