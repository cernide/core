#!/usr/bin/python
#
# Copyright 2018-2023 Polyaxon, Inc.
# This file and its contents are licensed under the AGPLv3 License.
# Please see the included NOTICE for copyright information and
# LICENSE-AGPL for a copy of the license.
import pytest

from haupt.proxies.schemas.server import get_server_config
from tests.test_proxies.base import BaseProxiesTestCase


@pytest.mark.proxies_mark
class TestServer(BaseProxiesTestCase):
    SET_PROXIES_SETTINGS = True

    def test_api_and_streams_config(self):
        expected = """
upstream polyaxon {
  server unix:/polyaxon/web/polyaxon.sock;
}


server {
    include polyaxon/polyaxon.base.conf;
}
"""  # noqa
        assert get_server_config(use_upstream=True, use_redirect=False) == expected

    def test_gateway_config(self):
        expected = """
server {
    include polyaxon/polyaxon.base.conf;
}


include polyaxon/polyaxon.redirect.conf;
"""  # noqa
        assert get_server_config(use_upstream=False, use_redirect=True) == expected
