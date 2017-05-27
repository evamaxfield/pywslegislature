import requests
import xmltodict
import pandas as pd
import collections
import datetime
import sys

# Targets
connection_main             = 'http://wslwebservices.leg.wa.gov/'
connection_services         = {
                                'committee': 'CommitteeService.asmx/',
                                'committee_meetings': 'CommitteeMeetingService.asmx/',
                                'committee_actions': 'CommitteeActionService.asmx/',
                                'amendment': 'AmendmentService.asmx/',
                                'document': 'LegislativeDocumentService.asmx/',
                                'legislation': 'LegislationService.asmx/',
                                'session_law': 'SessionLawService.asmx/',
                                'sponsor': 'SponsorService.asmx/'
                            }

attachment_sources          = {
                                'biennium': 'example: "2017-18"',
                                'year': 'example: "2017"',
                                'agency': 'example: "House"',
                                'committeeName': 'retrieved from GetCommittees and related calls, "Name" attribute',
                                'documentClass': 'retrieved from GetDocumentClasses and related calls, "#text" attribute',
                                'namedLike': 'retrieved from GetAllDocumentsByClass and related calls, "Name" attribute',
                                'beginDate': 'example: "2017-05-26"',
                                'endDate': 'example: "2017-05-26"',
                                'changedSinceDate': 'example: "2017-05-26"',
                                'agendaId': 'retrieved from GetCommitteeMeetings and related calls, "AgendaId" attribute',
                                'billNumber': 'retrieved from GetDocuments and related calls, "BillId" attribute; String.split(' ')[1]'
                            }

connection_labels           = {
                                'GetCommittees': 'committee',
                                'GetHouseCommittees': 'committee',
                                'GetSenateCommittees': 'committee',
                                'GetActiveCommittees': 'committee',
                                'GetActiveHouseCommittees': 'committee',
                                'GetActiveSenateCommittees': 'committee',
                                'GetDocumentClasses': 'document',
                                'GetAmendments': 'amendment',
                                'GetSponsors': 'sponsor',
                                'GetHouseSponsors': 'sponsor',
                                'GetSenateSponsors': 'sponsor',
                                'GetRequesters': 'sponsor',
                                'GetCommitteeMembers': 'committee',
                                'GetActiveCommitteeMembers': 'committee',
                                'GetAllDocumentsByClass': 'document',
                                'GetDocumentsByClass': 'document',
                                'GetDocuments': 'document',
                                'GetCommitteeMeetings': 'committee_meetings',
                                'GetRevisedCommitteeMeetings': 'committee_meetings',
                                'GetCommitteeMeetingItems': 'committee_meetings',
                                'GetCommitteeExecutiveActionsByBill': 'committee_actions',
                                'GetCommitteeReferralsByBill': 'committee_actions',
                                'GetCommitteeReferralsByCommittee': 'committee_actions',
                                'GetDoPassByCommittee': 'committee_actions',
                                'GetDoPassSubstituteByCommittee': 'committee_actions',
                                'GetDoPassWithAmendmentsByCommittee': 'committee_actions',
                                'GetDoPassWithAmendmentsToSubByCommittee': 'committee_actions'
                            }

data_labels                 = {
                                'GetCommittees': ['ArrayOfCommittee', 'Committee'],
                                'GetHouseCommittees': ['ArrayOfCommittee', 'Committee'],
                                'GetSenateCommittees': ['ArrayOfCommittee', 'Committee'],
                                'GetActiveCommittees': ['ArrayOfCommittee', 'Committee'],
                                'GetActiveHouseCommittees': ['ArrayOfCommittee', 'Committee'],
                                'GetActiveSenateCommittees': ['ArrayOfCommittee', 'Committee'],
                                'GetDocumentClasses': ['ArrayOfAnyType', 'anyType'],
                                'GetAmendments': ['ArrayOfAmendment', 'Amendment'],
                                'GetSponsors': ['ArrayOfMember', 'Member'],
                                'GetHouseSponsors': ['ArrayOfMember', 'Member'],
                                'GetSenateSponsors': ['ArrayOfMember', 'Member'],
                                'GetRequesters': ['ArrayOfLegislativeEntity', 'LegislativeEntity'],
                                'GetCommitteeMembers': ['ArrayOfMember', 'Member'],
                                'GetActiveCommitteeMembers': ['ArrayOfMember', 'Member'],
                                'GetAllDocumentsByClass': ['ArrayOfLegislativeDocument', 'LegislativeDocument'],
                                'GetDocumentsByClass': ['ArrayOfLegislativeDocument', 'LegislativeDocument'],
                                'GetDocuments': ['ArrayOfLegislativeDocument', 'LegislativeDocument'],
                                'GetCommitteeMeetings': ['ArrayOfCommitteeMeeting', 'CommitteeMeeting'],
                                'GetRevisedCommitteeMeetings': ['ArrayOfCommitteeMeeting', 'CommitteeMeeting'],
                                'GetCommitteeMeetingItems': ['ArrayOfCommitteeMeetingItem', 'CommitteeMeetingItem'],
                                'GetCommitteeExecutiveActionsByBill': ['ArrayOfCommitteeAction', 'CommitteeAction'],
                                'GetCommitteeReferralsByBill': ['ArrayOfCommitteeReferral', 'CommitteeReferral'],
                                'GetCommitteeReferralsByCommittee': ['ArrayOfCommitteeReferral', 'CommitteeReferral'],
                                'GetDoPassByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetDoPassSubstituteByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetDoPassWithAmendmentsByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetDoPassWithAmendmentsToSubByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo']
                            }

# Attachments
now = datetime.datetime.now()

biennium_current            = '2017-18'
year_current                = '2017'
date_start                  = '2017-01-01'
date_current                = ('' + str(now.year) + '-' + str(now.month) + '-' + str(now.day))
agency_house                = 'House'
committee_agnr              = 'Agriculture & Natural Resources'
document_class              = 'Amendments'
document_name               = '1017-S AMH APPL HATF 109'
agenda_id                   = '26520'
bill_id                     = '2201'

def httpGET(arch, service, call, attachments):
    getRequest = arch + service + call + '?'

    index = 0
    for key, attachment in attachments.items():
        if '&' in attachment:
            attachment = attachment.replace('&', '%26')

        if index < (len(attachments) - 1):
            getRequest += (key + '=' + attachment + '&')
        else:
            getRequest += (key + '=' + attachment)

        index += 1

    print('Full Call:')
    print(getRequest)
    print('----------------------------------------------------------------------------------------------')
    try:
        read = requests.get(getRequest)
        dictRead = xmltodict.parse(read.content)
    except:
        dictRead = read.content

    return dictRead

def storeCSV(df, call, attachments, label):
    if len(label) == 0:
        label = (call[3:] + '-')
        for key, attachment in attachments.items():
            label += (attachment + '-')
        label += '.csv'

    df.to_csv(label, sep=',')
    print('Stored ' + call + ' at: ' + label)

def processRequest(call, params):
    if params['info']:
        print(call + ' Function:')
        print('\toptional parameters:')
        for key, value in params.items():
            if key == 'attachments':
                print('\t\tattachments:')
                for key, attachment in params['attachments'].items():
                    print('\t\t\t' + key + ', default: ' + attachment)
                    print('\t\t\t\t' + attachment_sources[key])
            elif key == 'info':
                print('\t\t' + key + ', default: False')
            else:
                print('\t\t' + key + ', default: ' + str(value))
        print('\treturns:')
        print('\t\t', type(pd.DataFrame()))
        print('\twsl info:')
        print('\t\t' + connection_main + connection_services[connection_labels[call]][:-1] + '?op=' + call)

    else:
        dictRead = httpGET(connection_main, connection_services[connection_labels[call]], call, params['attachments'])

        if len(dictRead[data_labels[call][0]]) == 3:
            print('No objects to return')
            return None

        if str(type(dictRead[data_labels[call][0]][data_labels[call][1]])) == "<class 'collections.OrderedDict'>":
            try:
                data = pd.DataFrame(columns=dictRead[data_labels[call][0]][data_labels[call][1]])
                data.loc[0] = dictRead[data_labels[call][0]][data_labels[call][1]]
                if params['toCSV']:
                    storeCSV(data, call, params['attachments'], params['label'])

                return data

            except:
                print('There was an error in the request')
                print('Structure of returned:')
                return dictRead

        else:
            try:
                data = pd.DataFrame(dictRead[data_labels[call][0]][data_labels[call][1]])
                if params['toCSV']:
                    storeCSV(data, call, params['attachments'], params['label'])

                return data

            except:
                print('There was an error in the request')
                print('Structure of returned:')
                return dictRead

# IDENTITY TABLES
def GetCommittees(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetHouseCommittees(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSenateCommittees(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveCommittees(attachments={}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveHouseCommittees(attachments={}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveSenateCommittees(attachments={}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDocumentClasses(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetAmendments(attachments={'year': year_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSponsors(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetHouseSponsors(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSenateSponsors(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetRequesters(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

# VALUE TABLES
def GetCommitteeMembers(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveCommitteeMembers(attachments={'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetAllDocumentsByClass(attachments={'biennium': biennium_current, 'documentClass': document_class}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDocumentsByClass(attachments={'biennium': biennium_current, 'documentClass': document_class, 'namedLike': document_name}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDocuments(attachments={'biennium': biennium_current, 'namedLike': document_name}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetCommitteeMeetings(attachments={'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetRevisedCommitteeMeetings(attachments={'changedSinceDate': date_start}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetCommitteeMeetingItems(attachments={'agendaId': agenda_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetCommitteeExecutiveActionsByBill(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetCommitteeReferralsByBill(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetCommitteeReferralsByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDoPassByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDoPassSubstituteByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDoPassWithAmendmentsByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDoPassWithAmendmentsToSubByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())
