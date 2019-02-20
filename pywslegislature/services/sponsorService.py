#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class SponsorService(object):
    header = "SponsorService.asmx"
    description = "Information on sponsors of legislation in the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/SponsorService.asmx"
    GetHouseSponsors = APIFunction("GetHouseSponsors", {
        **ExampleParameters.biennium
    })
    GetRequesters = APIFunction("GetRequesters", {
        **ExampleParameters.biennium
    })
    GetSenateSponsors = APIFunction("GetSenateSponsors", {
        **ExampleParameters.biennium
    })
    GetSponsors = APIFunction("GetSponsors", {
        **ExampleParameters.biennium
    })
