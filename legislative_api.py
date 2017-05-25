import requests
import xmltodict
import pandas as pd
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

connection_labels           = {
                                'GetCommittees': 'committee',
                                'GetHouseCommittees': 'committee',
                                'GetSenateCommittees': 'committee',
                                'GetActiveCommittees': 'committee',
                                'GetActiveHouseCommittees': 'committee',
                                'GetActiveSenateCommittees': 'committee',
                                'GetDocumentClasses': 'document',
                                'GetAmendments': 'amendment',
                                'GetSponsors': 'sponsor'
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
                                'GetSponsors': ['ArrayOfMember', 'Member']
                            }

# Attachments
biennium_current            = 'biennium=2017-18'
year_current                = 'year=2017'

def httpGET(arch, service, call, attachments):
    getRequest = arch + service + call + '?'

    index = 0
    for attachment in attachments:
        if index < (len(attachments) - 1):
            getRequest += (attachment + '&')
        else:
            getRequest += attachment

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

def processRequest(call, params):
    if params['info']:
        print(call + ' Function:')
        print('optional parameters:')
        for key, value in params.items():
            if key == 'attachments':
                print('\tattachments:')
                for attachment in params['attachments']:
                    print('\t\tdefault: ' + attachment)
            elif key == 'info':
                print('\t' + key + ', default: False')
            else:
                print('\t' + key + ', default: ' + str(value))
        print('returns:')
        print('\tPandas DataFrame object')

    else:
        dictRead = httpGET(connection_main, connection_services[connection_labels[call]], call, params['attachments'])

        try:
            data = pd.DataFrame(dictRead[data_labels[call][0]][data_labels[call][1]])
            if params['toCSV']:
                if len(params['label']) == 0:
                    params['label'] = (call[3:] + '-')
                    for attachment in params['attachments']:
                        params['label'] += (attachment + '-')
                    params['label'] += '.csv'

                data.to_csv(params['label'], sep=',')
                print('Stored ' + call + ' at: ' + params['label'])

            return pd.DataFrame(data)

        except:
            print('There was an error in the request')
            print('Structure of returned:')
            return dictRead

def GetCommittees(attachments=[biennium_current], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetHouseCommittees(attachments=[biennium_current], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSenateCommittees(attachments=[biennium_current], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveCommittees(attachments=[], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveHouseCommittees(attachments=[], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetActiveSenateCommittees(attachments=[], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetDocumentClasses(attachments=[biennium_current], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetAmendments(attachments=[year_current], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSponsors(attachments=[biennium_current], toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())


#print(GetCommittees(toCSV=True))
#print(GetCommittees(info=True))
#print(GetCommittees(label='hello-world.csv'))

#print(GetActiveSenateCommittees())

#print(GetDocumentClasses())

#print(GetAmendments())
#print(GetAmendments().HtmUrl)

#print(GetSponsors())
