#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class AmendmentService(object):
    header = "AmendmentService.asmx"
    description = "Information on Amendments to legislation considered by the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/AmendmentService.asmx"
    GetAmendments = APIFunction(
        "GetAmendments",
        [ExampleParameters.year]
    )
