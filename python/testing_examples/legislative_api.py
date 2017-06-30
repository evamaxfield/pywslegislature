import requests
import xmltodict
import pandas as pd
import collections
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
                                'sponsor': 'SponsorService.asmx/',
                                'rcw': 'RcwCiteAffectedService.asmx/'
                            }

attachment_sources          = {
                                'biennium': 'example: "2017-18"',
                                'year': 'example: "2017"',
                                'agency': 'example: "House"',
                                'session': 'example: "0", 0: normal session, 1: 1st special session, etc.',
                                'chapterNumber': 'retrieved from GetSessionLawChapter and related calls, "ChapterNumber" attribute\n\t\t\t\tor: found in http://apps.leg.wa.gov/Rcw/, each title has multiple chapters (use "Title" attribute as chapterNumber)',
                                'rcwCite': 'retrieved from GetRcwCitesAffected and related calls, "RcwCite" attribute\n\t\t\t\tor: found in http://apps.leg.wa.gov/Rcw/, "Title" attribute',
                                'committeeName': 'retrieved from GetCommittees and related calls, "Name" attribute',
                                'documentClass': 'retrieved from GetDocumentClasses and related calls, "#text" attribute',
                                'namedLike': 'retrieved from GetAllDocumentsByClass and related calls, "Name" attribute',
                                'beginDate': 'example: "2017-05-26"',
                                'sinceDate': 'example: "2017-05-26"',
                                'endDate': 'example: "2017-05-26"',
                                'changedSinceDate': 'example: "2017-05-26"',
                                'requestNumber': 'retrieved from GetLegislation and related calls, "Request" attribute',
                                'agendaId': 'retrieved from GetCommitteeMeetings and related calls, "AgendaId" attribute',
                                'billNumber': 'retrieved from GetDocuments and related calls, "BillId" attribute; String.split(' ')[1]',
                                'billId': 'retrieved from GetDocuments and related calls, "BillId" attribute; String.split(' ')[1]'
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
                                'GetDoPassWithAmendmentsToSubByCommittee': 'committee_actions',
                                'GetInCommittee': 'committee_actions',
                                'GetLegislationReportedOutOfCommittee': 'committee_actions',
                                'GetMajorityReportByCommittee': 'committee_actions',
                                'GetMinorityReportByCommittee': 'committee_actions',
                                'GetReReferralByCommittee': 'committee_actions',
                                'GetReferredToAnotherCommitteeByCommittee': 'committee_actions',
                                'GetReferredToCommittee': 'committee_actions',
                                'GetRemovedFromCommittee': 'committee_actions',
                                'GetWithoutRecommendationByCommittee': 'committee_actions',
                                'GetChapterNumbersByYear': 'session_law',
                                'GetSessionLawByBill': 'session_law',
                                'GetBillByChapterNumber': 'session_law',
                                'GetLegislationAffectingRcw': 'rcw',
                                'GetLegislationAffectingRcwCite': 'rcw',
                                'GetAmendmentsForBiennium': 'legislation',
                                'GetAmendmentsForYear': 'legislation',
                                'GetCurrentStatus': 'legislation',
                                'GetHearings': 'legislation',
                                'GetHouseLegislationPassedHouse': 'legislation',
                                'GetHouseLegislationPassedSenate': 'legislation',
                                'GetLegislation': 'legislation',
                                'GetLegislationByRequestNumber': 'legislation',
                                'GetLegislationByYear': 'legislation',
                                'GetLegislationGovernorPartialVeto': 'legislation',
                                'GetLegislationGovernorSigned': 'legislation',
                                'GetLegislationGovernorVeto': 'legislation',
                                'GetLegislationInfoIntroducedSince': 'legislation',
                                'GetLegislationIntroducedSince': 'legislation',
                                'GetLegislationNotYetIntroducedInHouseOfOrigin': 'legislation',
                                'GetLegislationPassedHouse': 'legislation',
                                'GetLegislationPassedHouseWithinTimeFrame': 'legislation',
                                'GetLegislationPassedLegislature': 'legislation',
                                'GetLegislationPassedLegislatureWithinTimeFrame': 'legislation',
                                'GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody': 'legislation',
                                'GetLegislationPassedSenate': 'legislation',
                                'GetLegislationPassedSenateWithinTimeFrame': 'legislation',
                                'GetLegislationTypes': 'legislation',
                                'GetLegislativeBillListFeatureData': 'legislation',
                                'GetLegislativeStatusChangesByBillId': 'legislation',
                                'GetLegislativeStatusChangesByDateRange': 'legislation',
                                'GetPreFiledLegislationInfo': 'legislation',
                                'GetPrefiledLegislation': 'legislation',
                                'GetPublishedEnrolledLegislation': 'legislation',
                                'GetRcwCitesAffected': 'legislation',
                                'GetRollCalls': 'legislation',
                                'GetSenateLegislationPassedHouse': 'legislation',
                                'GetSenateLegislationPassedSenate': 'legislation',
                                'GetSessionLawChapter': 'legislation',
                                'GetSponsorsByBillId': 'legislation'
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
                                'GetDoPassWithAmendmentsToSubByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetInCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationReportedOutOfCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetMajorityReportByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetMinorityReportByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetReReferralByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetReferredToAnotherCommitteeByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetReferredToCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetRemovedFromCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetWithoutRecommendationByCommittee': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetChapterNumbersByYear': ['ArrayOfSessionLaw', 'SessionLaw'],
                                'GetSessionLawByBill': ['SessionLaw'],
                                'GetBillByChapterNumber': ['Legislation'],
                                'GetLegislationAffectingRcw': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationAffectingRcwCite': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetAmendmentsForBiennium': ['ArrayOfAmendment', 'Amendment'],
                                'GetAmendmentsForYear': ['ArrayOfAmendment', 'Amendment'],
                                'GetCurrentStatus': ['LegislativeStatus'],
                                'GetHearings': ['ArrayOfHearing', 'Hearing'],
                                'GetHouseLegislationPassedHouse': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetHouseLegislationPassedSenate': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislation': ['ArrayOfLegislation', 'Legislation'],
                                'GetLegislationByRequestNumber': ['Legislation'],
                                'GetLegislationByYear': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationGovernorPartialVeto': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationGovernorSigned': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationGovernorVeto': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationInfoIntroducedSince': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationIntroducedSince': ['ArrayOfLegislation', 'Legislation'],
                                'GetLegislationNotYetIntroducedInHouseOfOrigin': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedHouse': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedHouseWithinTimeFrame': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedLegislature': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedLegislatureWithinTimeFrame': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedSenate': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationPassedSenateWithinTimeFrame': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetLegislationTypes': ['ArrayOfLegislationType', 'LegislationType'],
                                'GetLegislativeBillListFeatureData': ['DataTable'],
                                'GetLegislativeStatusChangesByBillId': ['ArrayOfLegislativeStatus', 'LegislativeStatus'],
                                'GetLegislativeStatusChangesByDateRange': ['ArrayOfLegislativeStatus', 'LegislativeStatus'],
                                'GetPreFiledLegislationInfo': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetPrefiledLegislation': ['ArrayOfLegislation', 'Legislation'],
                                'GetPublishedEnrolledLegislation': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetRcwCitesAffected': ['ArrayOfRcwCiteAffected', 'RcwCiteAffected'],
                                'GetRollCalls': ['ArrayOfRollCall', 'RollCall'],
                                'GetSenateLegislationPassedHouse': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetSenateLegislationPassedSenate': ['ArrayOfLegislationInfo', 'LegislationInfo'],
                                'GetSessionLawChapter': ['SessionLaw'],
                                'GetSponsorsByBillId': ['ArrayOfSponsor', 'Sponsor']
                            }

# Attachments
biennium_current            = '2017-18'
year_current                = '2017'

# dates must be within the same session
date_start                  = '2017-03-01'
date_current                = '2017-05-20'

session_current             = '0'
chapter_target              = '35'
rcw_target                  = '35'
agency_house                = 'House'
committee_agnr              = 'Agriculture & Natural Resources'
document_class              = 'Amendments'
document_name               = '1017-S AMH APPL HATF 109'
agenda_id                   = '26520'
bill_id                     = '2201'
request_target              = 'H-2635.1'

def httpGET(arch, service, call, attachments):
    if call == 'GetSponsorsByBillId':
        call = 'GetSponsors'

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

def reduceOrderedDict(data):
    changed = False

    for column in data.columns.values:
        if str(type(data[column].iloc[0])) == "<class 'collections.OrderedDict'>":
            reduction_keys = data[column].iloc[0].keys()
            reduction_series_ = {}
            for key in reduction_keys:
                reduction = pd.Series(name = key)
                reduction_series_[key] = reduction

            for key, value in data[column].iteritems():
                for real_key, real_value in value.items():
                    reduction_series_[real_key].set_value(key, real_value)

            del data[column]

            for name, value in reduction_series_.items():
                data[name] = value

            changed = True

        if changed:
            data = reduceOrderedDict(data)

    return data

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
        return ''

    else:
        dictRead = httpGET(connection_main, connection_services[connection_labels[call]], call, params['attachments'])

        if str(type(dictRead)) == "<class 'bytes'>":
            print('Error in retrieving data')
            print('Most likely: Error in parameter values')
            print('Or likely: No data found')
            print('Function info and full error shown below')
            print('----------------------------------------')
            print(globals()[call](info=True))
            print('Returned read:')
            print(dictRead)
            return None

        if len(dictRead[data_labels[call][0]]) < 4:
            print('No objects to return')
            return None

        if len(data_labels[call]) > 1:
            if str(type(dictRead[data_labels[call][0]][data_labels[call][1]])) == "<class 'collections.OrderedDict'>":
                try:
                    data = pd.DataFrame(columns=dictRead[data_labels[call][0]][data_labels[call][1]])
                    data.loc[0] = dictRead[data_labels[call][0]][data_labels[call][1]]

                    data = reduceOrderedDict(data)

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

                    data = reduceOrderedDict(data)

                    if params['toCSV']:
                        storeCSV(data, call, params['attachments'], params['label'])

                    return data

                except:
                    print('There was an error in the request')
                    print('Structure of returned:')
                    return dictRead

        if str(type(dictRead[data_labels[call][0]])) == "<class 'collections.OrderedDict'>":
            try:
                data = pd.DataFrame(columns=dictRead[data_labels[call][0]])
                data.loc[0] = dictRead[data_labels[call][0]]

                data = reduceOrderedDict(data)

                if params['toCSV']:
                    storeCSV(data, call, params['attachments'], params['label'])

                return data

            except:
                print('There was an error in the request')
                print('Structure of returned:')
                return dictRead

        else:
            try:
                data = pd.DataFrame(dictRead[data_labels[call][0]])

                data = reduceOrderedDict(data)

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

def GetLegislationTypes(attachments={}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislativeBillListFeatureData(attachments={}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetPreFiledLegislationInfo(attachments={}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetPrefiledLegislation(attachments={}, toCSV=False, info=False, label=''):
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

def GetInCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationReportedOutOfCommittee(attachments={'agency': agency_house, 'committeeName': committee_agnr, 'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetMajorityReportByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetMinorityReportByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetReReferralByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetReferredToAnotherCommitteeByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetReferredToCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetRemovedFromCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetWithoutRecommendationByCommittee(attachments={'biennium': biennium_current, 'agency': agency_house, 'committeeName': committee_agnr}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetChapterNumbersByYear(attachments={'year': year_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSessionLawByBill(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetBillByChapterNumber(attachments={'year': year_current, 'session': session_current, 'chapterNumber': chapter_target}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationAffectingRcw(attachments={'biennium': biennium_current, 'rcwCite': rcw_target}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationAffectingRcwCite(attachments={'biennium': biennium_current, 'rcwCite': rcw_target}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetAmendmentsForBiennium(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetAmendmentsForYear(attachments={'year': year_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetCurrentStatus(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetHearings(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetHouseLegislationPassedHouse(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetHouseLegislationPassedSenate(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislation(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationByRequestNumber(attachments={'biennium': biennium_current, 'requestNumber': request_target}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationByYear(attachments={'year': year_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationGovernorPartialVeto(attachments={'biennium': biennium_current, 'agency': agency_house}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationGovernorSigned(attachments={'biennium': biennium_current, 'agency': agency_house}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationGovernorVeto(attachments={'biennium': biennium_current, 'agency': agency_house}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationInfoIntroducedSince(attachments={'sinceDate': date_start}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationIntroducedSince(attachments={'sinceDate': date_start}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationNotYetIntroducedInHouseOfOrigin(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedHouse(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedHouseWithinTimeFrame(attachments={'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedLegislature(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedLegislatureWithinTimeFrame(attachments={'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedSenate(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislationPassedSenateWithinTimeFrame(attachments={'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislativeStatusChangesByBillId(attachments={'biennium': biennium_current, 'billId': bill_id, 'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetLegislativeStatusChangesByDateRange(attachments={'biennium': biennium_current, 'beginDate': date_start, 'endDate': date_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetPublishedEnrolledLegislation(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetRcwCitesAffected(attachments={'biennium': biennium_current, 'billId': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetRollCalls(attachments={'biennium': biennium_current, 'billNumber': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSenateLegislationPassedHouse(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSenateLegislationPassedSenate(attachments={'biennium': biennium_current}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSessionLawChapter(attachments={'biennium': biennium_current, 'billId': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())

def GetSponsorsByBillId(attachments={'biennium': biennium_current, 'billId': bill_id}, toCSV=False, info=False, label=''):
    return processRequest(call=sys._getframe().f_code.co_name, params=locals())
