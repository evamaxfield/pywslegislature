# All possible HTTP GET requests to
# Washington State Legislature Web Services

# Created by Jackson Maxfield Brown
# 19 April 2017

# imports
from CallWashingtonLegislature  import httpGET
from pprint                     import pprint

# connection to services
services_all                = 'http://wslwebservices.leg.wa.gov/'

# connection to specific service
service_committee           = 'CommitteeService.asmx/'
service_committee_meetings  = 'CommitteeMeetingService.asmx/'
service_document            = 'LegislativeDocumentService.asmx/'
service_legislation         = 'LegislationService.asmx/'
service_sponsor             = 'SponsorService.asmx/'

# attachments (conditionals)
biennium_current            = 'biennium=2017-18'
agency_house                = 'agency=House'
agency_senate               = 'agency=Senate'
committees_house            = [ 'committeeName=Agriculture & Natural Resources',
                                'committeeName=Appropriations',
                                'committeeName=Business & Financial Services',
                                'committeeName=Capital Budget',
                                'committeeName=Commerce & Gaming',
                                'committeeName=Community Development, Housing & Tribal Affairs',
                                'committeeName=Early Learning & Human Services',
                                'committeeName=Education',
                                'committeeName=Environment',
                                'committeeName=Finance',
                                'committeeName=Health Care & Wellness',
                                'committeeName=Higher Education',
                                'committeeName=Judiciary',
                                'committeeName=Labor & Workplace Standards',
                                'committeeName=Local Government',
                                'committeeName=Public Safety',
                                'committeeName=Rules',
                                'committeeName=State Government, Elections & Information Technology',
                                'committeeName=Technology & Economic Development',
                                'committeeName=Transportation']
committees_house_active     = [ 'committeeName=Agriculture & Natural Resources',
                                'committeeName=Appropriations',
                                'committeeName=Business & Financial Services',
                                'committeeName=Capital Budget',
                                'committeeName=Commerce & Gaming',
                                'committeeName=Community Development, Housing & Tribal Affairs',
                                'committeeName=Early Learning & Human Services',
                                'committeeName=Education',
                                'committeeName=Environment',
                                'committeeName=Finance',
                                'committeeName=Health Care & Wellness',
                                'committeeName=Higher Education',
                                'committeeName=Judiciary',
                                'committeeName=Labor & Workplace Standards',
                                'committeeName=Local Government',
                                'committeeName=Public Safety',
                                'committeeName=Rules',
                                'committeeName=State Government, Elections & Information Technology',
                                'committeeName=Technology & Economic Development',
                                'committeeName=Transportation']
committees_senate           = [ 'committeeName=Agriculture, Water, Trade & Economic Development',
                                'committeeName=Commerce, Labor & Sports',
                                'committeeName=Early Learning & K-12 Education',
                                'committeeName=Energy, Environment & Telecommunications',
                                'committeeName=Financial Institutions & Insurance',
                                'committeeName=Health Care',
                                'committeeName=Higher Education',
                                'committeeName=Human Services, Mental Health & Housing',
                                'committeeName=Law & Justice',
                                'committeeName=Local Government',
                                'committeeName=Natural Resources & Parks',
                                'committeeName=Rules',
                                'committeeName=State Government',
                                'committeeName=Transportation',
                                'committeeName=Ways & Means']
committees_senate_active    = [ 'committeeName=Agriculture, Water, Trade & Economic Development',
                                'committeeName=Commerce, Labor & Sports',
                                'committeeName=Early Learning & K-12 Education',
                                'committeeName=Energy, Environment & Telecommunications',
                                'committeeName=Financial Institutions & Insurance',
                                'committeeName=Health Care',
                                'committeeName=Higher Education',
                                'committeeName=Human Services, Mental Health & Housing',
                                'committeeName=Law & Justice',
                                'committeeName=Local Government',
                                'committeeName=Natural Resources & Parks',
                                'committeeName=Rules',
                                'committeeName=State Government',
                                'committeeName=Transportation',
                                'committeeName=Ways & Means']
documents_classes           = [ 'documentClass=Amendments',
                                'documentClass=Bill Reports',
                                'documentClass=Bills',
                                'documentClass=Digests',
                                'documentClass=Initiatives',
                                'documentClass=Reports',
                                'documentClass=Workroom Reports']

# GETTING DATA FROM SERVICES:
# function: httpGET
#
# requires main legislation service
#       (services_all)
# requires targeted service
#       (service_legislation, etc.)
# requires targeted user defined call
#       ('GetCommittees', etc.)
# requires list of attachments or conditionals
#       (biennium_current, billNumber)
#
# returns orderedDictionary parsed from XML
# commonly, actual data found in sub-orderedDictionaries


# ACTUAL DATA PULLING
# uncomment dictRead and pprint to view data

# IDENTITY OBJECTS
# can be used in other get requests
# usually only requires biennium

# GetCommittees
# requires biennium attachment
# returns all (joint, senate, and house) committees
#dictRead = httpGET(services_all, service_committee, 'GetCommittees', [biennium_current])
#pprint(dictRead['ArrayOfCommittee']['Committee'])

# GetHouseCommittees
# requires biennium attachment
# returns house committees
#dictRead = httpGET(services_all, service_committee, 'GetHouseCommittees', [biennium_current])
#pprint(dictRead['ArrayOfCommittee']['Committee'])

# GetSenateCommittees
# requires biennium attachment
# returns senate committees
#dictRead = httpGET(services_all, service_committee, 'GetSenateCommittees', [biennium_current])
#pprint(dictRead['ArrayOfCommittee']['Committee'])

# GetActiveCommittees
# returns all (joint, senate, and house) active committees
#dictRead = httpGET(services_all, service_committee, 'GetActiveCommittees', [])
#pprint(dictRead['ArrayOfCommittee']['Committee'])

# GetActiveHouseCommittees
# returns active house committees
#dictRead = httpGET(services_all, service_committee, 'GetActiveHouseCommittees', [])
#pprint(dictRead['ArrayOfCommittee']['Committee'])

# GetActiveSenateCommittees
# returns active senate committees
#dictRead = httpGET(services_all, service_committee, 'GetActiveSenateCommittees', [])
#pprint(dictRead['ArrayOfCommittee']['Committee'])

# GetDocumentClasses
# requires biennium attachment
# returns all document types
#dictRead = httpGET(services_all, service_document, 'GetDocumentClasses', [biennium_current])
#pprint(dictRead['ArrayOfAnyType']['anyType'])

# GetSponsors
# requires biennium attachment
# returns all representatives and senators that servered during target
#dictRead = httpGET(services_all, service_sponsor, 'GetSponsors', [biennium_current])
#pprint(dictRead['ArrayOfMember']['Member'])

# GetHouseSponsors
# requires biennium attachment
# returns all representatives that servered during target
#dictRead = httpGET(services_all, service_sponsor, 'GetHouseSponsors', [biennium_current])
#pprint(dictRead['ArrayOfMember']['Member'])

# GetSenateSponsors
# requires biennium attachment
# returns all sentors that servered during target
#dictRead = httpGET(services_all, service_sponsor, 'GetSenateSponsors', [biennium_current])
#pprint(dictRead['ArrayOfMember']['Member'])

# GetRequesters
# requires biennium attachment
# returns all requesters that applied during target
#dictRead = httpGET(services_all, service_sponsor, 'GetRequesters', [biennium_current])
#pprint(dictRead['ArrayOfLegislativeEntity']['LegislativeEntity'])

# VALUE OBJECTS
# requires many more attachments for specific target

# GetCommitteeMembers
# Known Issue: committees with '&' in name fail to run
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns committee members of the targeted committee
#dictRead = httpGET(services_all, service_committee, 'GetCommitteeMembers', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfMember']['Member'])

# GetActiveCommitteeMembers
# Known Issue: committees with '&' in name fail to run
# requires agency attachment
# requires committeeName attachment
# returns committee members from the targeted committee
#dictRead = httpGET(services_all, service_committee, 'GetActiveCommitteeMembers', [agency_house, committees_house_active[1]])
#pprint(dictRead['ArrayOfMember']['Member'])

# GetAllDocumentsByClass
# requires biennium attachment
# requires documentClass attachment
# returns all documents from target
#dictRead = httpGET(services_all, service_document, 'GetAllDocumentsByClass', [biennium_current, documents_classes[0]])
#pprint(dictRead['ArrayOfLegislativeDocument']['LegislativeDocument'])

# GetDocumentsByClass
# requires biennium attachment
# requires documentClass attachment
# requires namedLike attachment
#       (get from GetAllDocumentsByClass, attribute: 'Name')
# returns all documents from target
#dictRead = httpGET(services_all, service_document, 'GetDocumentsByClass', [biennium_current, documents_classes[0], 'namedLike=1017-S AMH APPL HATF 109'])
#pprint(dictRead['ArrayOfLegislativeDocument']['LegislativeDocument'])

# GetDocuments
# requires biennium attachment
# requires namedLike attachment
#       (get from GetAllDocumentsByClass, attribute: 'Name')
# returns all documents from target
#dictRead = httpGET(services_all, service_document, 'GetDocuments', [biennium_current, 'namedLike=1017-S AMH APPL HATF 109'])
#pprint(dictRead['ArrayOfLegislativeDocument']['LegislativeDocument'])

# GetCommitteeMeetings
# requires beginDate attachment ('year-month-day')
# requires endDate attachment ('year-month-day')
# returns all committee meetings that occured in target
#dictRead = httpGET(services_all, service_committee_meetings, 'GetCommitteeMeetings', ['beginDate=2017-01-01', 'endDate=2017-04-19'])
#pprint(dictRead['ArrayOfCommitteeMeeting']['CommitteeMeeting'])

# GetRevisedCommitteeMeetings
# requires changedSinceDate attachment ('year-month-day')
# returns all committee meetings that have been revised since target
#dictRead = httpGET(services_all, service_committee_meetings, 'GetRevisedCommitteeMeetings', ['changedSinceDate=2017-04-19'])
#pprint(dictRead['ArrayOfCommitteeMeeting']['CommitteeMeeting'])

# GetCommitteeMeetingItems
# requires agendaId attachment
#       (get from GetCommitteeMeetings, attribute: 'AgendaId')
# returns all items discussed during target
#dictRead = httpGET(services_all, service_committee_meetings, 'GetCommitteeMeetingItems', ['agendaId=27512'])
#pprint(dictRead['ArrayOfCommitteeMeetingItem']['CommitteeMeetingItem'])
