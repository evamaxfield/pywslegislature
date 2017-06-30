from legislative_api import *

'''print(GetCommittees(info=True), '\n')
print(type(GetCommittees()), '\n')

print(GetHouseCommittees(info=True), '\n')
print(type(GetHouseCommittees()), '\n')

print(GetSenateCommittees(info=True), '\n')
print(type(GetSenateCommittees()), '\n')

print(GetActiveCommittees(info=True), '\n')
print(type(GetActiveCommittees()), '\n')

print(GetActiveHouseCommittees(info=True), '\n')
print(type(GetActiveHouseCommittees()), '\n')

print(GetActiveSenateCommittees(info=True), '\n')
print(type(GetActiveSenateCommittees()), '\n')

print(GetDocumentClasses(info=True), '\n')
print(type(GetDocumentClasses()), '\n')

print(GetAmendments(info=True), '\n')
print(type(GetAmendments()), '\n')

print(GetSponsors(info=True), '\n')
print(type(GetSponsors()), '\n')

print(GetHouseSponsors(info=True), '\n')
print(type(GetHouseSponsors()), '\n')

print(GetSenateSponsors(info=True), '\n')
print(type(GetSenateSponsors()), '\n')

print(GetRequesters(info=True), '\n')
print(type(GetRequesters()), '\n')

print(GetCommitteeMembers(info=True), '\n')
print(type(GetCommitteeMembers()), '\n')

print(GetActiveCommitteeMembers(info=True), '\n')
print(type(GetActiveCommitteeMembers()), '\n')

print(GetAllDocumentsByClass(info=True), '\n')
print(type(GetAllDocumentsByClass()), '\n')

print(GetDocumentsByClass(info=True), '\n')
print(type(GetDocumentsByClass()), '\n')

print(GetDocuments(info=True), '\n')
print(type(GetDocuments()), '\n')
'''
# known issue with orderedDictionary returned in attribute
print(GetCommitteeMeetings(info=True), '\n')
print(GetCommitteeMeetings(), '\n')

'''
print(GetRevisedCommitteeMeetings(info=True), '\n')
print(type(GetRevisedCommitteeMeetings()), '\n')

print(GetCommitteeMeetingItems(info=True), '\n')
print(type(GetCommitteeMeetingItems()), '\n')

print(GetCommitteeExecutiveActionsByBill(info=True), '\n')
print(type(GetCommitteeExecutiveActionsByBill()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetCommitteeReferralsByBill(info=True), '\n')
print(type(GetCommitteeReferralsByBill()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetCommitteeReferralsByCommittee(info=True), '\n')
print(type(GetCommitteeReferralsByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetDoPassByCommittee(info=True), '\n')
print(type(GetDoPassByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetDoPassSubstituteByCommittee(info=True), '\n')
print(type(GetDoPassSubstituteByCommittee()), '\n')

print(GetDoPassWithAmendmentsByCommittee(info=True), '\n')
print(type(GetDoPassWithAmendmentsByCommittee()), '\n')

print(GetDoPassWithAmendmentsToSubByCommittee(info=True), '\n')
print(type(GetDoPassWithAmendmentsToSubByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetInCommittee(info=True), '\n')
print(type(GetInCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationReportedOutOfCommittee(info=True), '\n')
print(type(GetLegislationReportedOutOfCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetMajorityReportByCommittee(info=True), '\n')
print(type(GetMajorityReportByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetMinorityReportByCommittee(info=True), '\n')
print(type(GetMinorityReportByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetReReferralByCommittee(info=True), '\n')
print(type(GetReReferralByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetReferredToAnotherCommitteeByCommittee(info=True), '\n')
print(type(GetReferredToAnotherCommitteeByCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetReferredToCommittee(info=True), '\n')
print(type(GetReferredToCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetRemovedFromCommittee(info=True), '\n')
print(type(GetRemovedFromCommittee()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetWithoutRecommendationByCommittee(info=True), '\n')
print(type(GetWithoutRecommendationByCommittee()), '\n')

print(GetChapterNumbersByYear(info=True), '\n')
print(type(GetChapterNumbersByYear()), '\n')

print(GetSessionLawByBill(info=True), '\n')
print(type(GetSessionLawByBill()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetBillByChapterNumber(info=True), '\n')
print(type(GetBillByChapterNumber()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationAffectingRcw(info=True), '\n')
print(type(GetLegislationAffectingRcw()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationAffectingRcwCite(info=True), '\n')
print(type(GetLegislationAffectingRcwCite()), '\n')

print(GetAmendmentsForBiennium(info=True), '\n')
print(type(GetAmendmentsForBiennium()), '\n')

print(GetAmendmentsForYear(info=True), '\n')
print(type(GetAmendmentsForYear()), '\n')

print(GetCurrentStatus(info=True), '\n')
print(type(GetCurrentStatus()), '\n')

print(GetHearings(info=True), '\n')
print(type(GetHearings()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetHouseLegislationPassedHouse(info=True), '\n')
print(type(GetHouseLegislationPassedHouse()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetHouseLegislationPassedSenate(info=True), '\n')
print(type(GetHouseLegislationPassedSenate()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislation(info=True), '\n')
print(type(GetLegislation()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationByRequestNumber(info=True), '\n')
print(type(GetLegislationByRequestNumber()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationByYear(info=True), '\n')
print(type(GetLegislationByYear()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationGovernorPartialVeto(info=True), '\n')
print(type(GetLegislationGovernorPartialVeto()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationGovernorSigned(info=True), '\n')
print(type(GetLegislationGovernorSigned()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationGovernorVeto(info=True), '\n')
print(type(GetLegislationGovernorVeto()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationInfoIntroducedSince(info=True), '\n')
print(type(GetLegislationInfoIntroducedSince()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationIntroducedSince(info=True), '\n')
print(type(GetLegislationIntroducedSince()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationNotYetIntroducedInHouseOfOrigin(info=True), '\n')
print(type(GetLegislationNotYetIntroducedInHouseOfOrigin()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedHouse(info=True), '\n')
print(type(GetLegislationPassedHouse()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedHouseWithinTimeFrame(info=True), '\n')
print(type(GetLegislationPassedHouseWithinTimeFrame()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedLegislature(info=True), '\n')
print(type(GetLegislationPassedLegislature()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedLegislatureWithinTimeFrame(info=True), '\n')
print(type(GetLegislationPassedLegislatureWithinTimeFrame()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody(info=True), '\n')
print(type(GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedSenate(info=True), '\n')
print(type(GetLegislationPassedSenate()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetLegislationPassedSenateWithinTimeFrame(info=True), '\n')
print(type(GetLegislationPassedSenateWithinTimeFrame()), '\n')

print(GetLegislationTypes(info=True), '\n')
print(type(GetLegislationTypes()), '\n')

# weird function, don't really see the value
print(GetLegislativeBillListFeatureData(info=True), '\n')
print(GetLegislativeBillListFeatureData(), '\n')

# THIS IS THE ONE
print(GetLegislativeStatusChangesByBillId(info=True), '\n')
print(GetLegislativeStatusChangesByBillId(), '\n')

# THIS IS KIND OF THE ONE
print(GetLegislativeStatusChangesByDateRange(info=True), '\n')
print(type(GetLegislativeStatusChangesByDateRange()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetPreFiledLegislationInfo(info=True), '\n')
print(type(GetPreFiledLegislationInfo()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetPrefiledLegislation(info=True), '\n')
print(type(GetPrefiledLegislation()), '\n')

print(GetPublishedEnrolledLegislation(info=True), '\n')
print(GetPublishedEnrolledLegislation(), '\n')

print(GetRcwCitesAffected(info=True), '\n')
print(type(GetRcwCitesAffected()), '\n')

# THIS IS THE ONE
# known issue with orderedDictionary returned in attribute
print(GetRollCalls(info=True), '\n')
print(GetRollCalls(), '\n')

# known issue with orderedDictionary returned in attribute
print(GetSenateLegislationPassedHouse(info=True), '\n')
print(type(GetSenateLegislationPassedHouse()), '\n')

# known issue with orderedDictionary returned in attribute
print(GetSenateLegislationPassedSenate(info=True), '\n')
print(type(GetSenateLegislationPassedSenate()), '\n')

print(GetSessionLawChapter(info=True), '\n')
print(type(GetSessionLawChapter()), '\n')

# THIS IS THE ONE
print(GetSponsorsByBillId(info=True), '\n')
print(GetSponsorsByBillId(), '\n')
'''
