#!/usr/bin/python
#
# Copyright 2018-2022 Polyaxon, Inc.
# This file and its contents are licensed under the AGPLv3 License.
# Please see the included NOTICE for copyright information and
# LICENSE-AGPL for a copy of the license.

from unittest import TestCase

from haupt.common.events.registry import run
from haupt.db import executor


class TestExecutorsSubscriptions(TestCase):
    def setUp(self):
        super().setUp()
        executor.validate_and_setup()
        # load subscriptions
        from haupt.db.executor import subscriptions  # noqa

    def _assert_events_subscription(self, events):
        for event in events:
            assert executor.event_manager.knows(event)

    def _assert_events_no_subscription(self, events):
        for event in events:
            assert executor.event_manager.knows(event) is False

    def test_events_subjects_runs(self):
        subscribed_events = {
            run.RUN_CREATED,
            run.RUN_RESUMED_ACTOR,
            run.RUN_STOPPED_ACTOR,
            run.RUN_APPROVED_ACTOR,
            run.RUN_DELETED_ACTOR,
            run.RUN_DONE,
            run.RUN_NEW_ARTIFACTS,
            run.RUN_NEW_STATUS,
        }

        self._assert_events_subscription(subscribed_events)
        self._assert_events_no_subscription(run.EVENTS - subscribed_events)
