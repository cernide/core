from django.db import models

from core.common.validation.slugs import validate_slug_with_dots
from core.db.abstracts.catalogs import BaseCatalog
from core.db.abstracts.contributors import ContributorsModel
from core.db.abstracts.readme import ReadmeModel
from core.db.abstracts.stage import StageModel
from core.db.abstracts.state import OptionalStateModel
from polyaxon.schemas import V1ProjectVersionKind


class BaseProjectVersion(
    BaseCatalog, StageModel, ReadmeModel, OptionalStateModel, ContributorsModel
):
    live_state = None

    kind = models.CharField(
        max_length=12,
        db_index=True,
        choices=V1ProjectVersionKind.to_choices(),
    )
    name = models.CharField(max_length=128, validators=[validate_slug_with_dots])
    project = models.ForeignKey(
        "db.Project", on_delete=models.CASCADE, related_name="versions"
    )
    content = models.TextField(
        help_text="The yaml/json content/metadata.",
        blank=True,
        null=True,
    )
    lineage = models.ManyToManyField(
        "db.ArtifactLineage", blank=True, related_name="versions"
    )
    run = models.ForeignKey(
        "db.Run",
        on_delete=models.CASCADE,
        related_name="versions",
        blank=True,
        null=True,
    )

    class Meta(BaseCatalog.Meta):
        abstract = True
        app_label = "db"
        db_table = "db_projectversion"
        unique_together = (("project", "name", "kind"),)
