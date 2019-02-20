#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class CommitteeMeetingService(object):
    header = "CommitteeMeetingService.asmx"
    description = "Information on committee meetings of the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/CommitteeMeetingService.asmx"
    GetCommitteeMeetings = APIFunction("GetCommitteeMeetings", {
        **ExampleParameters.beginDate,
        **ExampleParameters.endDate
    })
    GetCommitteeMeetingItems = APIFunction("GetCommitteeMeetingItems", {
        **ExampleParameters.agendaId
    })
    GetRevisedCommitteeMeetings = APIFunction("GetRevisedCommitteeMeetings", {
        **ExampleParameters.changedSinceDate
    })
