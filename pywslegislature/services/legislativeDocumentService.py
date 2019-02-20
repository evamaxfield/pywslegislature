#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class LegislativeDocumentService(object):
    header = "LegislativeDocumentService.asmx"
    description = "Information on documents relating to legislation of the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/LegislativeDocumentService.asmx"
    GetAllDocumentsByClass = APIFunction("GetAllDocumentsByClass", {
        **ExampleParameters.biennium,
        **ExampleParameters.documentClass
    })
    GetDocuments = APIFunction("GetDocuments", {
        **ExampleParameters.biennium,
        **ExampleParameters.namedLike
    })
    GetDocumentClasses = APIFunction("GetDocumentClasses", {
        **ExampleParameters.biennium
    })
    GetDocumentsByClass = APIFunction("GetDocumentsByClass", {
        **ExampleParameters.biennium,
        **ExampleParameters.documentClass,
        **ExampleParameters.namedLike
    })
