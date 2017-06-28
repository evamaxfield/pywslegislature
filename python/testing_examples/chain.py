### NEEDS TO BE UPDATED ###
# changed my version of the api a lot for easier usage
# it is easier to chain calls together than ever before, just haven't updated examples

from legislative_api import *
from pprint import pprint

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

returnedChain = getHouseCommitteeMembers()
pprint(returnedChain)

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
