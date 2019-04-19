#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class RCWCiteAffectedService(object):
    header = "RcwCiteAffectedService.asmx"
    description = "Information on RCW cites affected by legislation of the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/RcwCiteAffectedService.asmx"
    GetLegislationAffectingRcw = APIFunction(
        "GetLegislationAffectingRcw",
        [ExampleParameters.biennium, ExampleParameters.rcwCite]
    )
    GetLegislationAffectingRcwCite = APIFunction(
        "GetLegislationAffectingRcwCite",
        [ExampleParameters.biennium, ExampleParameters.rcwCite]
    )
