import requests
import xmltodict
import pandas as pd
import sys
import pprint

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
    print('-------------------------------------------------------------------------------------------------------')
    try:
        read = requests.get(getRequest)
        dictRead = xmltodict.parse(read.content)
    except:
        dictRead = read.content

    return dictRead

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
biennium_current            = '2017-18'

def GetCommittees(biennium=biennium_current, toCSV=False, info=False, label=''):
    if info:
        print(sys._getframe().f_code.co_name + ' Function:')
        print('optional attachments:')
        for key, value in locals().items():
            if key == 'info':
                print('\t' + key + '; default: False')
            else:
                print('\t' + key + '; default: ' + str(value))
        print('returns:')
        print('\tPandas DataFrame object')
    else:
        dictRead = httpGET(connection_main, connection_services['committee'], sys._getframe().f_code.co_name, [('biennium=' + biennium)])
        try:
            data = pd.DataFrame(dictRead['ArrayOfCommittee']['Committee'])
            if toCSV:
                if len(label) == 0:
                    label = (sys._getframe().f_code.co_name[3:] + '-' + biennium + '.csv')

                data.to_csv(label, sep=',')
                print('Stored ' + sys._getframe().f_code.co_name + ' at: ' + label)

            return pd.DataFrame(data)
        except:
            print('Structure of returned:')
            print(dictRead)
            return 'There was an error in the request!'

def GetHouseCommittees(biennium=biennium_current, toCSV=False, info=False, label=''):
    if info:
        print(sys._getframe().f_code.co_name + ' Function:')
        print('optional attachments:')
        for key, value in locals().items():
            if key == 'info':
                print('\t' + key + '; default: False')
            else:
                print('\t' + key + '; default: ' + str(value))
        print('returns:')
        print('\tPandas DataFrame object')
    else:
        dictRead = httpGET(connection_main, connection_services['committee'], sys._getframe().f_code.co_name, [('biennium=' + biennium)])
        try:
            data = pd.DataFrame(dictRead['ArrayOfCommittee']['Committee'])
            if toCSV:
                if len(label) == 0:
                    label = (sys._getframe().f_code.co_name[3:] + '-' + biennium + '.csv')

                data.to_csv(label, sep=',')
                print('Stored ' + sys._getframe().f_code.co_name + ' at: ' + label)

            return pd.DataFrame(data)
        except:
            print('Structure of returned:')
            print(dictRead)
            return 'There was an error in the request!'

print(GetHouseCommittees(toCSV=True))
