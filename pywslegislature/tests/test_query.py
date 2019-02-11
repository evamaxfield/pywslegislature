#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pywslegislature import Biennium
from pywslegislature.query import WSL_HEADER, WSLRequest
from pywslegislature.services import CommitteeService

# Preconstructed
COMMITTEES_REQUEST = WSLRequest(CommitteeService, "GetCommittees", {"biennium": str(Biennium(2019))})


@pytest.mark.parametrize("service, call, attachments, expected", [
    (CommitteeService, "GetCommittees", {},
        "{}/{}/{}?".format(WSL_HEADER, CommitteeService, "GetCommittees")),
    (CommitteeService, "GetCommittees", {"biennium": str(Biennium(2019))},
        "{}/{}/{}?{}".format(WSL_HEADER, CommitteeService, "GetCommittees", "biennium=2019-20")),
    (CommitteeService, "GetCommittees", {"biennium": str(Biennium(2019)), "hello": "wo&rld"},
        "{}/{}/{}?{}&{}".format(
            WSL_HEADER, CommitteeService, "GetCommittees", "biennium=2019-20", "hello=wo%26rld")),
    pytest.param("this", "fails", ["because", "list"], None, marks=pytest.mark.raises(exception=AttributeError))
])
def test_wslrequest_init(service, call, attachments, expected):
    """Test the initialization portion of the WSLRequest object."""
    r = WSLRequest(service, call, attachments)

    assert str(r) == expected


# @pytest.mark.parametrize("request, mock, expected", [
#     (COMMITTEES_REQUEST, None, None)
# ])
# def test_wslrequest_process(request, mock, expected):
#     """Test the processing portion of the WSLRequest object."""
#
#     results = request.process()
