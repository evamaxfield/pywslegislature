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
service_committee_actions   = 'CommitteeActionService.asmx/'
service_amendment           = 'AmendmentService.asmx/'
service_document            = 'LegislativeDocumentService.asmx/'
service_legislation         = 'LegislationService.asmx/'
service_session_law         = 'SessionLawService.asmx/'
service_sponsor             = 'SponsorService.asmx/'

# attachments (conditionals)
biennium_current            = 'biennium=2017-18'
year_current                = 'year=2017'
session_current             = ''
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

# GetAmendments
# requires year attachment
# returns all documents with type as 'amendment'
#dictRead = httpGET(services_all, service_amendment, 'GetAmendments', [year_current])
#pprint(dictRead['ArrayOfAmendment']['Amendment'])

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

# GetCommitteeExecutiveActionsByBill
# requires biennium attachment
# requires billNumber attachment
#       (get from GetDocuments, attribute: 'BillId', string split [1] on ' ')
# returns committee actions from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetCommitteeExecutiveActionsByBill', [biennium_current, 'billNumber=1017'])
#pprint(dictRead['ArrayOfCommitteeAction']['CommitteeAction'])

# GetCommitteeReferralsByBill
# requires biennium attachment
# requires billNumber attachment
#       (get from GetDocuments, attribute: 'BillId', string split [1] on ' ')
# returns committee referrals from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetCommitteeReferralsByBill', [biennium_current, 'billNumber=1017'])
#pprint(dictRead['ArrayOfCommitteeReferral']['CommitteeReferral'])

# GetCommitteeReferralsByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns committee referrals from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetCommitteeReferralsByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfCommitteeReferral']['CommitteeReferral'])

# GetDoPassByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with do pass label from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetDoPassByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetDoPassSubstituteByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with do pass with substitute label from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetDoPassSubstituteByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetDoPassWithAmendmentsByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with do pass with amendments label from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetDoPassWithAmendmentsByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

### VERY UNCOMMON ###
# GetDoPassWithAmendmentsToSubByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with do pass with amendments to substitute label from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetDoPassWithAmendmentsToSubByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetInCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills currently in target
#dictRead = httpGET(services_all, service_committee_actions, 'GetInCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetLegislationReportedOutOfCommittee
# requires committeeName attachment
# requires agency attachment
# requires beginDate attachment
# requires endDate attachment
# returns all legislation out from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetLegislationReportedOutOfCommittee', [committees_house[1], agency_house, 'beginDate=2017-02-06', 'endDate=2017-04-30'])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetMajorityReportByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with status majority report from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetMajorityReportByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetMinorityReportByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with status minority report from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetMinorityReportByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

### VERY UNCOMMON ###
# GetReReferralByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with status re-referral from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetReReferralByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

### VERY UNCOMMON ###
# GetReferredToAnotherCommitteeByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with status referred to another from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetReferredToAnotherCommitteeByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetReferredToCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with status referred to target
#dictRead = httpGET(services_all, service_committee_actions, 'GetReferredToCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetRemovedFromCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with removed status from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetRemovedFromCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

### VERY UNCOMMON ###
# GetWithoutRecommendationByCommittee
# requires biennium attachment
# requires agency attachment
# requires committeeName attachment
# returns all bills with status without recommendation from target
#dictRead = httpGET(services_all, service_committee_actions, 'GetWithoutRecommendationByCommittee', [biennium_current, agency_house, committees_house[1]])
#pprint(dictRead['ArrayOfLegislationInfo']['LegislationInfo'])

# GetChapterNumbersByYear
# requires year attachment
# returns all chapters in target
#dictRead = httpGET(services_all, service_session_law, 'GetChapterNumbersByYear', [year_current])
#pprint(dictRead['ArrayOfSessionLaw']['SessionLaw'])

# GetSessionLawByBill
# requires biennium attachment
# require billNumber attachment
# returns session law information for target
#dictRead = httpGET(services_all, service_session_law, 'GetSessionLawByBill', [biennium_current, 'billNumber=1001'])
#pprint(dictRead['SessionLaw'])

# GetBillByChapterNumber
# requires year attachment
# requires session attachment
# requires chapterNumber attachment
# returns bill information from target
#dictRead = httpGET(services_all, service_session_law, 'GetBillByChapterNumber', [year_current, 'session=0', 'chapterNumber=43'])
#pprint(dictRead['Legislation'])


# EXAMPLE CHAIN CALLS
# get all house committees and their members
def getHouseCommitteeMembers():
    committeesRead = httpGET(services_all, service_committee, 'GetActiveHouseCommittees', [])
    committeesList = []
    for committee in committeesRead['ArrayOfCommittee']['Committee']:
        if ('&' not in committee['Name']):
            committeesList.append('committeeName=' + committee['Name'])

    print('Safe to run committees:')
    print(committeesList)
    print('---------------------------------------------------------------')

    committeesDict = {}
    for committee in committeesList:
        membersRead = httpGET(services_all, service_committee, 'GetActiveCommitteeMembers', [agency_house, committee])
        membersList = []
        for member in membersRead['ArrayOfMember']['Member']:
            membersList.append(member['Name'])

        committeesDict[committee] = membersList

    return committeesDict

#returnedChain = getHouseCommitteeMembers()
#pprint(returnedChain)

# get all documents of type 'Bill' and get their committee actions
def getBillsAndActions():
    billsRead = httpGET(services_all, service_document, 'GetAllDocumentsByClass', [biennium_current, documents_classes[2]])
    billsList = []
    for bill in billsRead['ArrayOfLegislativeDocument']['LegislativeDocument']:
        billsList.append(bill['BillId'].split()[1])

    print('Safe to run bills:')
    print(billsList)
    print('---------------------------------------------------------------')

    actionsDict = {}
    for bill in billsList[:10]:
        actionsRead = httpGET(services_all, service_committee_actions, 'GetCommitteeExecutiveActionsByBill', [biennium_current, 'billNumber=' + bill])
        dataBack = {}
        try:
            dataBack = actionsRead['ArrayOfCommitteeAction']['CommitteeAction']
        except:
            dataBack = {'Action' : 'None'}

        actionsDict[bill] = dataBack
    return actionsDict

#pprint(getBillsAndActions())
