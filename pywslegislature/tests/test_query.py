#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pywslegislature.query import WSL_HEADER, WSLRequest
from pywslegislature.services import CommitteeService, ExampleParameters


@pytest.mark.parametrize("service, call, attachments, expected", [
    (
        CommitteeService.header,
        CommitteeService.GetCommittees,
        {ExampleParameters.biennium.name: ExampleParameters.biennium.example_value},
        f"{WSL_HEADER}/{CommitteeService.header}/{CommitteeService.GetCommittees.name}?biennium=2019-20"
    ),
    (
        CommitteeService.header,
        CommitteeService.GetCommittees,
        {ExampleParameters.biennium.name: ExampleParameters.biennium.example_value},
        f"{WSL_HEADER}/{CommitteeService.header}/{CommitteeService.GetCommittees.name}?biennium=2019-20"
    ),
    (
        CommitteeService.header,
        CommitteeService.GetCommittees,
        {ExampleParameters.biennium.name: ExampleParameters.biennium.example_value, "foo": "bar"},
        f"{WSL_HEADER}/{CommitteeService.header}/{CommitteeService.GetCommittees.name}?biennium=2019-20"
    ),
    pytest.param(
        CommitteeService.header,
        CommitteeService.GetCommittees,
        {},
        None,
        marks=pytest.mark.raises(exception=KeyError)
    ),
    pytest.param(
        CommitteeService.header,
        12,
        None,
        None,
        marks=pytest.mark.raises(exception=TypeError)
    )
])
def test_wslrequest_init(service, call, attachments, expected):
    """Test the initialization portion of the WSLRequest object."""
    r = WSLRequest(service, call, attachments)

    assert str(r) == expected
