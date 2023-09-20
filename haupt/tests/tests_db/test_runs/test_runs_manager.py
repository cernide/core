from unittest.mock import patch

from django.test import TestCase

from haupt.common.events.registry import run as run_events
from haupt.db.factories.projects import ProjectFactory
from haupt.db.factories.runs import RunFactory
from haupt.db.factories.users import UserFactory
from haupt.orchestration import operations
from polyaxon._constants.metadata import META_COPY_ARTIFACTS, META_UPLOAD_ARTIFACTS
from polyaxon._polyaxonfile import (
    CompiledOperationSpecification,
    OperationSpecification,
)
from polyaxon._utils.fixtures import get_fxt_job_with_inputs
from polyaxon.schemas import V1CloningKind, V1CompiledOperation, V1Statuses


class TestRunManager(TestCase):
    def setUp(self):
        super().setUp()
        self.user = UserFactory()
        self.user2 = UserFactory()
        self.project = ProjectFactory()
        op_spec = OperationSpecification.read(values=get_fxt_job_with_inputs())
        self.run = operations.init_and_save_run(
            project_id=self.project.id, op_spec=op_spec, user_id=self.user.id
        )

    @patch("haupt.common.auditor.record")
    def test_create_run(self, auditor_record):
        run = RunFactory(project=self.project, user=self.user)
        assert auditor_record.call_count == 1
        call_args, call_kwargs = auditor_record.call_args
        assert call_kwargs["event_type"] == run_events.RUN_CREATED

        assert run.user == self.user
        assert run.project == self.project
        assert run.name is None
        assert run.description is None
        assert run.content is None
        assert run.readme is None
        assert run.tags is None
        assert run.cloning_kind is None
        assert run.original is None

    @patch("haupt.common.auditor.record")
    def test_copy_run(self, auditor_record):
        run = operations.copy_run(run=self.run)
        assert auditor_record.call_count == 1
        call_args, call_kwargs = auditor_record.call_args
        assert call_kwargs["event_type"] == run_events.RUN_CREATED
        assert run.user == self.run.user
        assert run.kind == self.run.kind
        assert run.project == self.run.project
        assert run.name == self.run.name
        assert run.description == self.run.description
        assert run.content == self.run.content
        assert run.meta_info == {META_COPY_ARTIFACTS: {"dirs": [self.run.uuid.hex]}}
        config = CompiledOperationSpecification.read(run.content)
        original_config = CompiledOperationSpecification.read(self.run.content)
        assert len(config.run.init or []) == len(original_config.run.init or [])
        assert run.raw_content == self.run.raw_content
        assert run.readme == self.run.readme
        assert run.tags == self.run.tags
        assert run.cloning_kind == V1CloningKind.COPY
        assert run.original == self.run
        assert run.inputs == {"image": "foo/bar"}

        run = operations.copy_run(
            run=self.run,
            user_id=self.user2.id,
            name="new-name",
            description="new-description",
            content={"trigger": "all_done"},
            readme="new-readme",
            tags=["tag1", "tag2"],
        )
        assert run.user != self.run.user
        assert run.user == self.user2
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content != self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.meta_info == {META_COPY_ARTIFACTS: {"dirs": [self.run.uuid.hex]}}
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.inputs == {"image": "foo/bar"}
        assert run.cloning_kind == V1CloningKind.COPY
        assert run.original == self.run

        # Copy with uploads
        self.run.meta_info[META_UPLOAD_ARTIFACTS] = "foo"
        self.run.save()
        run = operations.copy_run(
            run=self.run,
            user_id=self.user2.id,
            name="new-name",
            description="new-description",
            content={"trigger": "all_done"},
            readme="new-readme",
            tags=["tag1", "tag2"],
        )
        assert run.user != self.run.user
        assert run.user == self.user2
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content != self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.meta_info == {
            META_UPLOAD_ARTIFACTS: "foo",
            META_COPY_ARTIFACTS: {"dirs": [self.run.uuid.hex]},
        }
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.inputs == {"image": "foo/bar"}
        assert run.cloning_kind == V1CloningKind.COPY
        assert run.original == self.run

        # Copy with uploads and specific fields
        self.run.meta_info[META_UPLOAD_ARTIFACTS] = "foo"
        self.run.save()
        run = operations.copy_run(
            run=self.run,
            user_id=self.user2.id,
            name="new-name",
            description="new-description",
            content={"trigger": "all_done"},
            readme="new-readme",
            tags=["tag1", "tag2"],
            meta_info={
                META_COPY_ARTIFACTS: {
                    "dirs": ["{}/resources".format(self.run.uuid.hex)]
                }
            },
        )
        assert run.user != self.run.user
        assert run.user == self.user2
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content != self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.meta_info == {
            META_UPLOAD_ARTIFACTS: "foo",
            META_COPY_ARTIFACTS: {"dirs": ["{}/resources".format(self.run.uuid.hex)]},
        }
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.inputs == {"image": "foo/bar"}
        assert run.cloning_kind == V1CloningKind.COPY
        assert run.original == self.run

    @patch("haupt.common.auditor.record")
    def test_resume_run(self, auditor_record):
        run = operations.resume_run(run=self.run)
        assert auditor_record.call_count == 2
        call_args_list = auditor_record.call_args_list
        assert call_args_list[0][0] == ()
        assert call_args_list[1][0] == ()
        assert call_args_list[0][1]["event_type"] == run_events.RUN_NEW_STATUS
        assert call_args_list[1][1]["event_type"] == run_events.RUN_RESUMED
        assert run.user == self.run.user
        assert run.kind == self.run.kind
        assert run.project == self.run.project
        assert run.name == self.run.name
        assert run.description == self.run.description
        assert run.content == self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.readme == self.run.readme
        assert run.tags == self.run.tags
        assert run.status == V1Statuses.RESUMING
        assert run.cloning_kind is None
        assert run.original is None
        assert run.inputs == {"image": "foo/bar"}

        user = UserFactory()
        run = operations.resume_run(
            run=self.run,
            user_id=user.id,
            name="new-name",
            description="new-description",
            content={"trigger": "all_done"},
            readme="new-readme",
            tags=["tag1", "tag2"],
        )
        assert run.user == user
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content == self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.cloning_kind is None
        assert run.original is None

    @patch("haupt.common.auditor.record")
    def test_restart_run(self, auditor_record):
        run = operations.restart_run(run=self.run)
        assert auditor_record.call_count == 1
        call_args, call_kwargs = auditor_record.call_args
        assert call_kwargs["event_type"] == run_events.RUN_CREATED
        assert run.kind == self.run.kind
        assert run.user == self.run.user
        assert run.project == self.run.project
        assert run.name == self.run.name
        assert run.description == self.run.description
        assert run.content == self.run.content
        assert run.meta_info == {}
        assert run.readme == self.run.readme
        assert run.tags == self.run.tags
        assert run.cloning_kind == V1CloningKind.RESTART
        assert run.original == self.run

        # Test restart with updated info
        run = operations.restart_run(
            run=self.run,
            user_id=self.user.id,
            name="new-name",
            description="new-description",
            content={"trigger": "all_done"},
            readme="new-readme",
        )
        assert run.user == self.user
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content != self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.cloning_kind == V1CloningKind.RESTART
        assert run.original == self.run
        assert run.meta_info == {}

        # Restart with patch strategy
        job = V1CompiledOperation.read(self.run.content)
        assert job.run.container.command == ["foo"]
        assert job.run.container.args == ["foo"]
        run = operations.restart_run(
            run=self.run,
            user_id=self.user.id,
            name="new-name",
            description="new-description",
            content={
                "patchStrategy": "replace",
                "runPatch": {"container": {"command": ["bar"], "args": ["bar"]}},
            },
            readme="new-readme",
        )
        assert run.user == self.user
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content != self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.cloning_kind == V1CloningKind.RESTART
        assert run.original == self.run
        job = V1CompiledOperation.read(run.content)
        assert job.run.container.command == ["bar"]
        assert job.run.container.args == ["bar"]

        # Restart with upload
        self.run.meta_info[META_UPLOAD_ARTIFACTS] = "foo"
        self.run.save()
        run = operations.restart_run(
            run=self.run,
            user_id=self.user.id,
            name="new-name",
            description="new-description",
            content={"trigger": "all_done"},
            readme="new-readme",
        )
        assert run.user == self.user
        assert run.project == self.project
        assert run.name == "new-name"
        assert run.description == "new-description"
        assert run.content != self.run.content
        assert run.raw_content == self.run.raw_content
        assert run.readme == "new-readme"
        assert set(run.tags) == {"tag1", "tag2"}
        assert run.cloning_kind == V1CloningKind.RESTART
        assert run.original == self.run
        assert run.meta_info == {
            META_UPLOAD_ARTIFACTS: "foo",
            META_COPY_ARTIFACTS: {"dirs": ["{}/foo".format(self.run.uuid.hex)]},
        }
