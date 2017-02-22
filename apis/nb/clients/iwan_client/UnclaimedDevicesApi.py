#!/usr/bin/env python
#pylint: skip-file

"""
UnclaimedDevicesApi.py

NOTE: This class was generated manually to emulate swagger.
"""
import sys
import os
import urllib.request, urllib.parse, urllib.error

from .models import *


class UnclaimedDevicesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    def getList(self, **kwargs):
        """Retrieves list of configured Sites

        Args:

            scope, str: Authorization Scope for RBAC (required)

        Returns: list[UnprovisionedSite]
        """

        allParams = ['scope']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getList" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/iwan/unclaimed-devices'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        headerParams['Accept'] = 'application/json'
        headerParams['Content-Type'] = 'application/json'

        if ('scope' in params):
            headerParams['scope'] = params['scope']

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'UnclaimedDeviceResponse')

        return responseObject
