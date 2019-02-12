#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pywslegislature import Biennium
from pywslegislature.query import WSL_HEADER, WSLRequest
from pywslegislature.services import COMMITTEE_SERVICE, EXAMPLE_BIENNIUM

# Preconstructed
COMMITTEES_REQUEST = WSLRequest(COMMITTEE_SERVICE.header, COMMITTEE_SERVICE.GetCommittees.name, EXAMPLE_BIENNIUM)


@pytest.mark.parametrize("service, call, attachments, expected", [
    (COMMITTEE_SERVICE.header, COMMITTEE_SERVICE.GetCommittees.name, {},
        "{}/{}/{}?".format(WSL_HEADER, COMMITTEE_SERVICE.header, COMMITTEE_SERVICE.GetCommittees.name)),
    (COMMITTEE_SERVICE.header, COMMITTEE_SERVICE.GetCommittees.name, EXAMPLE_BIENNIUM,
        "{}/{}/{}?{}".format(
        WSL_HEADER, COMMITTEE_SERVICE.header,
        COMMITTEE_SERVICE.GetCommittees.name, "biennium=2019-20"
        )),
    (COMMITTEE_SERVICE.header, COMMITTEE_SERVICE.GetCommittees.name, {**EXAMPLE_BIENNIUM, "hello": "wo&rld"},
        "{}/{}/{}?{}&{}".format(
            WSL_HEADER, COMMITTEE_SERVICE.header,
            COMMITTEE_SERVICE.GetCommittees.name, "biennium=2019-20", "hello=wo%26rld"
        )),
    pytest.param("this", "fails", ["because", "list"], None, marks=pytest.mark.raises(exception=AttributeError))
])
def test_wslrequest_init(service, call, attachments, expected):
    """Test the initialization portion of the WSLRequest object."""
    r = WSLRequest(service, call, attachments)

    assert str(r) == expected
#
# @pytest.mark.parametrize("request, mock, expected", [
#     (COMMITTEES_REQUEST, None, None)
# ])
# def test_wslrequest_process(request, mock, expected):
#     """Test the processing portion of the WSLRequest object."""
#
#     results = request.process()
