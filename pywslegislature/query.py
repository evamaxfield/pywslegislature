#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import requests
from typing import Dict, Union
from xml.etree import ElementTree
import xmltodict

from .services.apifunction import APIFunction

###############################################################################

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)4s: %(module)s:%(lineno)4s %(asctime)s] %(message)s'
)
log = logging.getLogger(__file__)

###############################################################################

# Defaults
WSL_HEADER = "http://wslwebservices.leg.wa.gov"


class WSLResults(object):
    """
    Use a WSLRequest to retrieve data from web services.

    :param request: The string used to retrieve the results.
    """

    def __init__(self, request: str, response: requests.models.Response):
        # Make hidden
        self._request = request
        self._response = response

        # Check the response
        log.debug("WSLResults {}, initialized with response status: {}".format(self, self.response.status_code))
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
        # Lazy load parsed xml
        if self._xml is None:
            self._xml = ElementTree.fromstring(self.response.content)
            log.debug("Parsed ElementTree from: {}".format(self))

        return self._xml

    @property
    def json(self):
        # Lazy load parsed json
        if self._json is None:
            self._json = xmltodict.parse(self.response.content)
            self._json = json.loads(json.dumps(self._json))
            log.debug("Parsed JSON from: {}".format(self))

        return self._json

    def __str__(self):
        return "<WSLResults [{}]>".format(str(self.request))

    def __repr__(self):
        return str(self)


class WSLRequest(object):
    """
    Construct an HTTP request for WSL Web Services API.

    :param service: The API service to be targeted.
    :param call: The API function to call.
    :param attachments: The parameters for the call.
    """

    def __init__(self, service: str, call: Union[str, APIFunction], attachments: Dict[str, str] = {}):
        # These do not need to be hidden as users can edit them as much.
        # Any changing of values post-initialization won't result in any downstream errors.
        self.service = service

        # Set the call if provided a string
        if isinstance(call, str):
            self.call = call
            self.attachments = attachments
        # If the call is an APIFunction, check the attachments
        elif isinstance(call, APIFunction):
            for param in call.parameters:
                if param.name not in attachments:
                    raise KeyError(f"Missing required query parameter: {param.name}")

            # Drop any attachments that aren't in the APIFunction definition
            required_attachments = [param.name for param in call.parameters]
            valid_attachments = {}
            for attachment, value in attachments.items():
                if attachment in required_attachments:
                    valid_attachments[attachment] = value

            # Finally set the call to the string
            self.call = call.name
            self.attachments = valid_attachments
        # Anything else should raise an error
        else:
            raise TypeError(f"WSLRequest call expects either: [str, APIFunction], received: {type(call)} {call}")

    @property
    def formatted_prefix(self):
        return "/".join([WSL_HEADER, self.service, self.call])

    @property
    def formatted_attachments(self):
        return ["{}={}".format(key, str(att).replace("&", "%26")) for key, att in self.attachments.items()]

    def process(self, mock_return=None):
        """
        Process the request and return the results.

        :param mock_return: Data return override for available for testing.
        """
        # Check mock return
        if mock_return is None:
            # Pass the response from requests.get
            log.debug("Requesting repsonse from: {}".format(str(self)))
            return WSLResults(str(self), requests.get(str(self)))

        return mock_return

    def __str__(self):
        return "{}?{}".format(self.formatted_prefix, "&".join(self.formatted_attachments))

    def __repr__(self):
        return "<WSLRequest [{}]>".format(str(self))
