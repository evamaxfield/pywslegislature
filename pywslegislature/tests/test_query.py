#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pywslegislature import Biennium
from pywslegislature.query import WSL_HEADER, WSLRequest
from pywslegislature.services import CommitteeService, ExampleParameters

# Preconstructed
COMMITTEES_REQUEST = WSLRequest(
    CommitteeService.header,
    CommitteeService.GetCommittees.name,
    ExampleParameters.biennium
)


@pytest.mark.parametrize("service, call, attachments, expected", [
    (CommitteeService.header, CommitteeService.GetCommittees.name, {},
        "{}/{}/{}?".format(WSL_HEADER, CommitteeService.header, CommitteeService.GetCommittees.name)),
    (CommitteeService.header, CommitteeService.GetCommittees.name, ExampleParameters.biennium,
        "{}/{}/{}?{}".format(
        WSL_HEADER, CommitteeService.header,
        CommitteeService.GetCommittees.name, "biennium=2019-20"
        )),
    (CommitteeService.header, CommitteeService.GetCommittees.name, {**ExampleParameters.biennium, "hello": "wo&rld"},
        "{}/{}/{}?{}&{}".format(
            WSL_HEADER, CommitteeService.header,
            CommitteeService.GetCommittees.name, "biennium=2019-20", "hello=wo%26rld"
        )),
    pytest.param("this", "fails", ["because", "list"], None, marks=pytest.mark.raises(exception=AttributeError))
])
def test_wslrequest_init(service, call, attachments, expected):
    """Test the initialization portion of the WSLRequest object."""
    r = WSLRequest(service, call, attachments)

    assert str(r) == expected
