#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import requests
from typing import Dict
from xml.etree import ElementTree
import xmltodict

###############################################################################

log = logging.getLogger(__name__)

###############################################################################

# Defaults
WSL_HEADER = "http://wslwebservices.leg.wa.gov"


class WSLResults(object):

    def __init__(self, request: str, response: requests.models.Response):
        """
        Use a WSLRequest to retrieve data from web services.

        :param request: The string used to retrieve the results.
        """
        self._request = request
        self._response = response

        # Check the response
        log.info("WSLResults {}, initialized with response status: {}".format(self, self.response.status_code))
        self.response.raise_for_status()

        # Lazy loaded
        self._xml = None
        self._json = None

    @property
    def request(self):
        return self._request

    @property
    def response(self):
        return self._response

    @property
    def xml(self):
        if self._xml is None:
            self._xml = ElementTree.fromstring(self.response.content)
            log.info("Parsed ElementTree from: {}".format(self))

        return self._xml

    @property
    def json(self):
        if self._json is None:
            self._json = xmltodict.parse(self.response.content)
            log.info("Parsed OrderedDict from: {}".format(self))

        return self._json

    def __str__(self):
        return "<WSLResults [{}]>".format(str(self.request))

    def __repr__(self):
        return str(self)


class WSLRequest(object):

    def __init__(self, service: str, call: str, attachments: Dict[str, str] = {}):
        """
        Construct an HTTP request for WSL Web Services API.

        :param service: The API service to be targeted.
        :param call: The API function to call.
        :param attachments: The parameters for the call.
        """
        self.service = service
        self.call = call
        self.attachments = attachments

    @property
    def formatted_prefix(self):
        return "/".join([WSL_HEADER, self.service, self.call])

    @property
    def formatted_attachments(self):
        return ["{}={}".format(key, attachment.replace("&", "%26")) for key, attachment in self.attachments.items()]

    def process(self, mock_return=None):
        """
        Process the request and return the results.

        :param request: A WSLRequest to use.
        :param mock_return: Data return override for available for testing.
        """
        if mock_return is None:
            log.debug("Requesting repsonse from: {}".format(str(self)))
            return WSLResults(str(self), requests.get(str(self)))

        return mock_return

    def __str__(self):
        return "{}?{}".format(self.formatted_prefix, "&".join(self.formatted_attachments))

    def __repr__(self):
        return "<WSLRequest [{}]>".format(str(self))
