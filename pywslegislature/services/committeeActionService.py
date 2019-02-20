#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .apifunction import APIFunction
from .exampleParameters import ExampleParameters


class CommitteeActionService(object):
    header = "CommitteeActionService.asmx"
    description = "Information on committee actions by the Washington State Legislature."
    source = "http://wslwebservices.leg.wa.gov/CommitteeActionService.asmx"
    GetCommitteeExecutiveActionsByBill = APIFunction("GetCommitteeExecutiveActionsByBill", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetCommitteeReferralsByBill = APIFunction("GetCommitteeReferralsByBill", {
        **ExampleParameters.biennium,
        **ExampleParameters.billNumber
    })
    GetCommitteeReferralsByCommittee = APIFunction("GetCommitteeReferralsByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetDoPassByCommittee = APIFunction("GetDoPassByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetDoPassSubstituteByCommittee = APIFunction("GetDoPassSubstituteByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetDoPassWithAmendmentsByCommittee = APIFunction("GetDoPassWithAmendmentsByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetDoPassWithAmendmentsToSubByCommittee = APIFunction("GetDoPassWithAmendmentsToSubByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetInCommittee = APIFunction("GetInCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetLegislationReportedOutOfCommittee = APIFunction("GetLegislationReportedOutOfCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.beginDate,
        **ExampleParameters.committeeName,
        **ExampleParameters.endDate
    })
    GetLegislationScheduledHearingsByCommittee = APIFunction("GetLegislationScheduledHearingsByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetMajorityReportByCommittee = APIFunction("GetMajorityReportByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetMinorityReportByCommittee = APIFunction("GetMinorityReportByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetReReferralByCommittee = APIFunction("GetReReferralByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetReferredToAnotherCommitteeByCommittee = APIFunction("GetReferredToAnotherCommitteeByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetReferredToCommittee = APIFunction("GetReferredToCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetRemovedFromCommittee = APIFunction("GetRemovedFromCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
    GetWithoutRecommendationByCommittee = APIFunction("GetWithoutRecommendationByCommittee", {
        **ExampleParameters.agency,
        **ExampleParameters.biennium,
        **ExampleParameters.committeeName
    })
