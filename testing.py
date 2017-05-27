from legislative_api import *


print(GetCommittees(info=True), '\n')
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

# known issue with orderedDictionary returned in attribute
print(GetCommitteeMeetings(info=True), '\n')
print(type(GetCommitteeMeetings()), '\n')

# known issue with orderedDictionary returned in attribute
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
