#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import EXAMPLE_BIENNIUM


class CommitteeService(object):

    def __init__(self):
        self._header = "CommitteeService.asmx"
        self._description = "Information on committees of the Washington State Legislature."

        # All functions available to this service
        self._functions = {
            "GetCommittees": APIFunction("GetCommittees", {**EXAMPLE_BIENNIUM}),
            "GetHouseCommittees": APIFunction("GetHouseCommittees", {**EXAMPLE_BIENNIUM}),
            "GetSenateCommittees": APIFunction("GetSenateCommittees", {**EXAMPLE_BIENNIUM}),
            "GetActiveCommittees": APIFunction("GetActiveCommittees"),
            "GetActiveHouseCommittees": APIFunction("GetActiveHouseCommittees"),
            "GetActiveSenateCommittees": APIFunction("GetActiveSenateCommittees"),
            "GetCommitteeMembers": APIFunction("GetCommitteeMembers", {**EXAMPLE_BIENNIUM}),
            "GetActiveCommitteeMembers": APIFunction("GetActiveCommitteeMembers")
        }

        # Add all functions as attributes of this service
        for func, details in self._functions.items():
            setattr(self, func, details)

    @property
    def header(self):
        return self._header

    @property
    def description(self):
        return self._description

    @property
    def functions(self):
        return [getattr(self, key) for key in self._functions]

    def __str__(self):
        return "<CommitteeService [{}]>".format(self.description)

    def __repr__(self):
        return str(self)
