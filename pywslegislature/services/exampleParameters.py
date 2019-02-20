#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ExampleParameters(object):
    biennium = {"biennium": "2019-20"}
    year = {"year": "2019"}
    agency = {"agency": "House"}
    session = {"session": "0: normal session, 1: 1st special session, etc."}
    chapterNumber = {"chapterNumber": "From GetSessionLawChapter and related calls: 'ChapterNumber' attribute."}
    rcwCite = {"rcwCite": "From GetRcwCitesAffected and related calls: 'RcwCite' attribute."}
    committeeName = {"committeeName": "From GetCommittees and related calls: 'Name' attribute."}
    documentClass = {"documentClass": "From GetDocumentClasses and related calls: '#text' attribute."}
    namedLike = {"namedLike": "From GetAllDocumentsByClass and related calls: 'Name' attribute."}
    beginDate = {"beginDate": "2017-05-26"}
    sinceDate = {"sinceDate": "2017-05-26"}
    endDate = {"endDate": "2017-05-26"}
    changedSinceDate = {"changedSinceDate": "2017-05-26"}
    requestNumber = {"requestNumber": "From GetLegislation and related calls: 'Request' attribute."}
    agendaId = {"agendaId": "From GetCommitteeMeetings and related calls: 'AgendaId' attribute."}
    billNumber = {"billNumber": "From GetDocuments and related calls: 'BillId' attribute."}
    billId = {"billId": "From GetDocuments and related calls: 'BillId' attribute."}
