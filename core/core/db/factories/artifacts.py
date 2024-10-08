import factory

from core.db.defs import Models
from tracer.artifacts import V1ArtifactKind


class ArtifactFactory(factory.django.DjangoModelFactory):
    name = "accuracy"
    kind = V1ArtifactKind.METRIC
    summary = {"last_value": 0.9, "max_value": 0.9, "min_value": 0.1}
    path = "accuracy"

    class Meta:
        model = Models.Artifact
