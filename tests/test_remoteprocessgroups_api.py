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
from swagger_client.apis.remoteprocessgroups_api import RemoteprocessgroupsApi


class TestRemoteprocessgroupsApi(unittest.TestCase):
    """ RemoteprocessgroupsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.remoteprocessgroups_api.RemoteprocessgroupsApi()

    def tearDown(self):
        pass

    def test_get_remote_process_group(self):
        """
        Test case for get_remote_process_group

        Gets a remote process group
        """
        pass

    def test_remove_remote_process_group(self):
        """
        Test case for remove_remote_process_group

        Deletes a remote process group
        """
        pass

    def test_update_remote_process_group(self):
        """
        Test case for update_remote_process_group

        Updates a remote process group
        """
        pass

    def test_update_remote_process_group_input_port(self):
        """
        Test case for update_remote_process_group_input_port

        Updates a remote port
        """
        pass

    def test_update_remote_process_group_output_port(self):
        """
        Test case for update_remote_process_group_output_port

        Updates a remote port
        """
        pass


if __name__ == '__main__':
    unittest.main()
