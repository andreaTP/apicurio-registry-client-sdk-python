# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import apicurioregistryclient
from apicurioregistryclient.paths.admin_rules import delete  # noqa: E501
from apicurioregistryclient import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAdminRules(ApiTestMixin, unittest.TestCase):
    """
    AdminRules unit test stubs
        Delete all global rules  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()