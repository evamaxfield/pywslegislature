#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class CommitteeService(object):
    header = "CommitteeService.asmx"
    description = "Information on committees of the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/CommitteeService.asmx"
    GetCommittees = APIFunction("GetCommittees", {**ExampleParameters.biennium})
    GetHouseCommittees = APIFunction("GetHouseCommittees", {**ExampleParameters.biennium})
    GetSenateCommittees = APIFunction("GetSenateCommittees", {**ExampleParameters.biennium})
    GetActiveCommittees = APIFunction("GetActiveCommittees")
    GetActiveHouseCommittees = APIFunction("GetActiveHouseCommittees")
    GetActiveSenateCommittees = APIFunction("GetActiveSenateCommittees")
    GetCommitteeMembers = APIFunction("GetCommitteeMembers", {**ExampleParameters.biennium})
    GetActiveCommitteeMembers = APIFunction("GetActiveCommitteeMembers")
