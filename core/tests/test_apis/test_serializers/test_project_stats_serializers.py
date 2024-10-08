import pytest

from core.apis.serializers.project_stats import ProjectStatsSerializer
from polyaxon.schemas import V1ProjectVersionKind
from tests.base.case import BaseTestProjectStatsSerializer


@pytest.mark.serializers_mark
class TestProjectStatsSerializer(BaseTestProjectStatsSerializer):
    serializer_class = ProjectStatsSerializer
    expected_keys = {
        "created_at",
        "updated_at",
        "user",
        "run",
        "status",
        "version",
        "tracking_time",
    }

    def test_serialize_one_light(self):
        obj1 = self.create_one()
        data = self.serializer_class(obj1).data

        assert set(data.keys()) == self.expected_keys
        data.pop("created_at")
        data.pop("updated_at")
        expected = dict(
            user={"count": 1},
            run={"1": 1, "0": 2},
            status={"running": 1, "succeeded": 2},
            version={
                V1ProjectVersionKind.COMPONENT: 1,
                V1ProjectVersionKind.MODEL: 2,
                V1ProjectVersionKind.ARTIFACT: 3,
            },
            tracking_time={"1": 1111, "0": 200},
        )
        assert data == expected

    def test_serialize_one(self):
        obj1 = self.create_one()
        self.serializer_class.LIGHT = False
        data = self.serializer_class(obj1).data

        assert set(data.keys()) == self.expected_keys
        data.pop("created_at")
        data.pop("updated_at")
        expected = dict(
            user={"count": 1, "users": [self.user.username]},
            run={"1": 1, "0": 2},
            status={"running": 1, "succeeded": 2},
            version={
                V1ProjectVersionKind.COMPONENT: 1,
                V1ProjectVersionKind.MODEL: 2,
                V1ProjectVersionKind.ARTIFACT: 3,
            },
            tracking_time={"1": 1111, "0": 200},
        )
        assert data == expected
        self.serializer_class.LIGHT = True


del BaseTestProjectStatsSerializer
