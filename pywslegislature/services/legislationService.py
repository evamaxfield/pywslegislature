#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class LegislationService(object):
    header = "LegislationService.asmx"
    description = "Information on legislation being considered by the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/LegislationService.asmx"
    GetAmendmentsForBiennium = APIFunction("GetAmendmentsForBiennium", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetAmendmentsForYear = APIFunction("GetAmendmentsForYear", {
        **ExampleParameters.billNumber,
        **ExampleParameters.year
    })
    GetCurrentStatus = APIFunction("GetCurrentStatus", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetHearings = APIFunction("GetHearings", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetHouseLegislationPassedHouse = APIFunction("GetHouseLegislationPassedHouse", {
        **ExampleParameters.biennium
    })
    GetHouseLegislationPassedSenate = APIFunction("GetHouseLegislationPassedSenate", {
        **ExampleParameters.biennium
    })
    GetLegislation = APIFunction("GetLegislation", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetLegislationByRequestNumber = APIFunction("GetLegislationByRequestNumber", {
        **ExampleParameters.biennium,
        **ExampleParameters.requestNumber
    })
    GetLegislationByYear = APIFunction("GetLegislationByYear", {
        **ExampleParameters.year
    })
    GetLegislationGovernorPartialVeto = APIFunction("GetLegislationGovernorPartialVeto", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium
    })
    GetLegislationGovernorSigned = APIFunction("GetLegislationGovernorSigned", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium
    })
    GetLegislationGovernorVeto = APIFunction("GetLegislationGovernorVeto", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium
    })
    GetLegislationInfoIntroducedSince = APIFunction("GetLegislationInfoIntroducedSince", {
        **ExampleParameters.sinceDate
    })
    GetLegislationIntroducedSince = APIFunction("GetLegislationIntroducedSince", {
        **ExampleParameters.sinceDate
    })
    GetLegislationNotYetIntroducedInHouseOfOrigin = APIFunction("GetLegislationNotYetIntroducedInHouseOfOrigin", {
        **ExampleParameters.biennium
    })
    GetLegislationPassedHouse = APIFunction("GetLegislationPassedHouse", {
        **ExampleParameters.biennium
    })
    GetLegislationPassedHouseWithinTimeFrame = APIFunction("GetLegislationPassedHouseWithinTimeFrame", {
        **ExampleParameters.beginDate,
        **ExampleParameters.endDate
    })
    GetLegislationPassedLegislature = APIFunction("GetLegislationPassedLegislature", {
        **ExampleParameters.biennium
    })
    GetLegislationPassedLegislatureWithinTimeFrame = APIFunction("GetLegislationPassedLegislatureWithinTimeFrame", {
        **ExampleParameters.beginDate,
        **ExampleParameters.endDate
    })
    GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody = APIFunction(
        "GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody", {
        **ExampleParameters.biennium
    })
    GetLegislationPassedSenate = APIFunction("GetLegislationPassedSenate", {
        **ExampleParameters.biennium
    })
    GetLegislationPassedSenateWithinTimeFrame = APIFunction("GetLegislationPassedSenateWithinTimeFrame", {
        **ExampleParameters.beginDate,
        **ExampleParameters.endDate
    })
    GetLegislationTypes = APIFunction("GetLegislationTypes")
    GetLegislativeBillListFeatureData = APIFunction("GetLegislativeBillListFeatureData")
    GetLegislativeStatusChangesByBillId = APIFunction("GetLegislativeStatusChangesByBillId", {
        **ExampleParameters.beginDate,
        **ExampleParameters.biennium,
        **ExampleParameters.billId,
        **ExampleParameters.endDate
    })
    GetLegislativeStatusChangesByBillNumber = APIFunction("GetLegislativeStatusChangesByBillNumber", {
        **ExampleParameters.beginDate,
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber,
        **ExampleParameters.endDate
    })
    GetLegislativeStatusChangesByDateRange = APIFunction("GetLegislativeStatusChangesByDateRange", {
        **ExampleParameters.beginDate,
        **ExampleParameters.biennium,
        **ExampleParameters.endDate
    })
    GetPreFiledLegislationInfo = APIFunction("GetPreFiledLegislationInfo")
    GetPrefiledLegislation = APIFunction("GetPrefiledLegislation")
    GetPublishedEnrolledLegislation = APIFunction("GetPublishedEnrolledLegislation", {
        **ExampleParameters.biennium
    })
    GetRcwCitesAffected = APIFunction("GetRcwCitesAffected", {
        **ExampleParameters.biennium,
        **ExampleParameters.billId
    })
    GetRollCalls = APIFunction("GetRollCalls", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetSenateLegislationPassedHouse = APIFunction("GetSenateLegislationPassedHouse", {
        **ExampleParameters.biennium
    })
    GetSenateLegislationPassedSenate = APIFunction("GetSenateLegislationPassedSenate", {
        **ExampleParameters.biennium
    })
    GetSessionLawChapter = APIFunction("GetSessionLawChapter", {
        **ExampleParameters.biennium,
        **ExampleParameters.billId
    })
    GetSponsors = APIFunction("GetSponsors", {
        **ExampleParameters.biennium,
        **ExampleParameters.billId
    })
