# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

from nipyapi import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.counters_api import CountersApi


class TestCountersApi(unittest.TestCase):
    """ CountersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.counters_api.CountersApi()

    def tearDown(self):
        pass

    def test_get_counters(self):
        """
        Test case for get_counters

        Gets the current counters for this NiFi
        """
        pass

    def test_update_counter(self):
        """
        Test case for update_counter

        Updates the specified counter. This will reset the counter value to 0
        """
        pass


if __name__ == '__main__':
    unittest.main()
