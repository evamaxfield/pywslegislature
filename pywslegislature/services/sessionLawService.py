#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class SessionLawService(object):
    header = "SessionLawService.asmx"
    description = "Information on legislation relating to session laws of the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/SessionLawService.asmx"
    GetBillByChapterNumber = APIFunction("GetBillByChapterNumber", {
        **ExampleParameters.chapterNumber,
        **ExampleParameters.session,
        **ExampleParameters.year
    })
    GetChapterNumbersByYear = APIFunction("GetChapterNumbersByYear", {
        **ExampleParameters.year
    })
    GetSessionLawByBill = APIFunction("GetSessionLawByBill", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetSessionLawByBillId = APIFunction("GetSessionLawByBillId", {
        **ExampleParameters.biennium,
        **ExampleParameters.billId
    })
