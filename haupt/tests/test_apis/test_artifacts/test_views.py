#!/usr/bin/python
#
# Copyright 2018-2023 Polyaxon, Inc.
# This file and its contents are licensed under the AGPLv3 License.
# Please see the included NOTICE for copyright information and
# LICENSE-AGPL for a copy of the license.


import pytest
import uuid

from unittest.mock import patch

from rest_framework import status

from django.db import IntegrityError

from haupt.apis.serializers.artifacts import (
    RunArtifactNameSerializer,
    RunArtifactSerializer,
)
from haupt.background.celeryp.tasks import CoreSchedulerCeleryTasks
from haupt.db.factories.artifacts import ArtifactFactory
from haupt.db.factories.projects import ProjectFactory
from haupt.db.factories.runs import RunFactory
from haupt.db.models.artifacts import Artifact, ArtifactLineage
from haupt.db.queries import artifacts as artifacts_queries
from polyaxon.api import API_V1
from tests.base.case import BaseTest
from traceml.artifacts import V1ArtifactKind, V1RunArtifact


@pytest.mark.lineages_mark
class TestRunArtifactNameListViewV1(BaseTest):
    serializer_class = RunArtifactNameSerializer
    model_class = Artifact
    factory_class = ArtifactFactory
    num_objects = 3
    queryset = artifacts_queries.artifacts

    def setUp(self):
        super().setUp()
        self.project = ProjectFactory()
        self.run = RunFactory(
            user=self.user,
            project=self.project,
            content="test",
            raw_content="test",
            is_managed=True,
        )
        self.url = "/{}/{}/{}/runs/{}/artifacts_lineage/names/".format(
            API_V1, "polyaxon", self.project.name, self.run.uuid.hex
        )
        self.objects = []
        for i in range(self.num_objects):
            obj = self.factory_class(
                name=f"foo{i}",
                state=uuid.uuid4(),
            )
            self.objects.append(obj)
            ArtifactLineage.objects.create(run=self.run, artifact=obj)

        self.query = self.queryset.filter(run=self.run)

        # Other user objects
        other_project = ProjectFactory()
        other_run = RunFactory(
            user=self.user,
            project=other_project,
            content="test",
            raw_content="test",
            is_managed=True,
        )
        other_obj = self.factory_class(
            state=uuid.uuid4(),
        )
        ArtifactLineage.objects.create(run=other_run, artifact=other_obj)

    def test_get(self):
        resp = self.client.get(self.url)
        assert resp.status_code == status.HTTP_200_OK

        assert resp.data["next"] is None
        assert resp.data["count"] == len(self.objects)

        data = resp.data["results"]
        assert len(data) == self.query.count()
        assert data == self.serializer_class(self.query, many=True).data


@pytest.mark.lineages_mark
class TestRunArtifactNameListViewV15(TestRunArtifactNameListViewV1):
    def setUp(self):
        super().setUp()
        self.url = "/{}/{}/{}/runs/{}/lineage/artifacts/names/".format(
            API_V1, "polyaxon", self.project.name, self.run.uuid.hex
        )


@pytest.mark.lineages_mark
class TestRunArtifactListViewV1(BaseTest):
    serializer_class = RunArtifactSerializer
    model_class = Artifact
    factory_class = ArtifactFactory
    queryset = artifacts_queries.artifacts
    num_objects = 3

    def setUp(self):
        super().setUp()
        self.project = ProjectFactory()
        self.run = RunFactory(
            user=self.user,
            project=self.project,
            content="test",
            raw_content="test",
            is_managed=True,
        )
        self.url = "/{}/{}/{}/runs/{}/artifacts_lineage/".format(
            API_V1, "polyaxon", self.project.name, self.run.uuid.hex
        )
        self.objects = []
        for i in range(self.num_objects):
            obj = self.factory_class(
                name=f"foo{i}",
                state=uuid.uuid4(),
            )
            self.objects.append(obj)
            ArtifactLineage.objects.create(run=self.run, artifact=obj)

        self.query = self.queryset.filter(run=self.run)

    def test_create_duplicate(self):
        # same obj with  different state
        self.factory_class(
            name=self.objects[0].name,
            state=uuid.uuid4(),
            kind=self.objects[0].kind,
            path=self.objects[0].path,
            summary=self.objects[0].summary,
        )
        # Same obj with same state
        with self.assertRaises(IntegrityError):
            self.factory_class(
                name=self.objects[0].name,
                state=self.objects[0].state,
                kind=self.objects[0].kind,
                path=self.objects[0].path,
                summary=self.objects[0].summary,
            )

    def test_get(self):
        resp = self.client.get(self.url)
        assert resp.status_code == status.HTTP_200_OK

        assert resp.data["next"] is None
        assert resp.data["count"] == len(self.objects)

        data = resp.data["results"]
        assert len(data) == self.queryset.count()
        assert data == self.serializer_class(self.query, many=True).data

    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    def test_get_filter(self):  # pylint:disable=too-many-statements
        # Name
        resp = self.client.get(self.url + "?query=name:foo1")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data["next"] is None
        assert resp.data["count"] == 1

        resp = self.client.get(self.url + "?query=name:foo2")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data["next"] is None
        assert resp.data["count"] == 1

        resp = self.client.get(self.url + "?query=name:foo200")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data["next"] is None
        assert resp.data["count"] == 0

        # Kind
        resp = self.client.get(self.url + f"?query=kind:{V1ArtifactKind.METRIC}")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data["next"] is None
        assert resp.data["count"] == 3

        resp = self.client.get(self.url + f"?query=kind:{V1ArtifactKind.HISTOGRAM}")
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data["next"] is None
        assert resp.data["count"] == 0

    def test_create(self):
        data = []
        resp = self.client.post(self.url, data)
        assert resp.status_code == status.HTTP_400_BAD_REQUEST

        metric1 = V1RunArtifact(
            name="accuracy",
            kind=V1ArtifactKind.METRIC,
            path="accuracy",
            summary=dict(last_value=0.9, max_value=0.99, min_value=0.1, max_step=100),
        )
        metric2 = V1RunArtifact(
            name="precision",
            kind=V1ArtifactKind.METRIC,
            path="precision",
            summary=dict(last_value=0.8, max_value=0.99, min_value=0.1, max_step=100),
        )
        data = [metric1.to_dict(), metric2.to_dict()]
        with patch("haupt.common.workers.send") as workers_send:
            resp = self.client.post(self.url, data)
        assert resp.status_code == status.HTTP_201_CREATED

        assert workers_send.call_count == 1
        assert {c[0][0] for c in workers_send.call_args_list} == {
            CoreSchedulerCeleryTasks.RUNS_SET_ARTIFACTS,
        }


@pytest.mark.lineages_mark
class TestRunArtifactListViewV15(TestRunArtifactListViewV1):
    def setUp(self):
        super().setUp()
        self.url = "/{}/{}/{}/runs/{}/lineage/artifacts/".format(
            API_V1, "polyaxon", self.project.name, self.run.uuid.hex
        )


@pytest.mark.lineages_mark
class TestRunArtifactDetailViewV1(BaseTest):
    serializer_class = RunArtifactSerializer
    model_class = Artifact
    factory_class = ArtifactFactory

    def setUp(self):
        super().setUp()
        self.project = ProjectFactory()
        self.run = RunFactory(
            user=self.user,
            project=self.project,
            content="test",
            raw_content="test",
            is_managed=True,
        )
        self.artifact = self.factory_class(name="foo", state=self.project.owner.uuid)
        self.artifact_lineage = ArtifactLineage.objects.create(
            artifact=self.artifact, run=self.run
        )
        self.url = "/{}/{}/{}/runs/{}/artifacts_lineage/{}/".format(
            API_V1,
            "polyaxon",
            self.project.name,
            self.run.uuid.hex,
            self.artifact.name,
        )
        self.queryset = Artifact.objects.all()

    def test_get(self):
        resp = self.client.get(self.url)
        assert resp.status_code == status.HTTP_200_OK
        assert resp.data == self.serializer_class(self.artifact_lineage).data

    def test_delete(self):
        assert Artifact.objects.count() == 1
        assert ArtifactLineage.objects.count() == 1
        resp = self.client.delete(self.url)
        assert resp.status_code == status.HTTP_204_NO_CONTENT
        assert Artifact.objects.count() == 1
        assert ArtifactLineage.objects.count() == 0


@pytest.mark.lineages_mark
class TestRunArtifactDetailViewV15(TestRunArtifactDetailViewV1):
    def setUp(self):
        super().setUp()
        self.url = "/{}/{}/{}/runs/{}/lineage/artifacts/{}/".format(
            API_V1,
            "polyaxon",
            self.project.name,
            self.run.uuid.hex,
            self.artifact.name,
        )
