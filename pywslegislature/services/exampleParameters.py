#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import NamedTuple


class ExampleParameter(NamedTuple):
    name: str
    example_value: str


class ExampleParameters(object):
    biennium = ExampleParameter(
        name="biennium",
        example_value="2019-20"
    )
    year = ExampleParameter(
        name="year",
        example_value="2019"
    )
    agency = ExampleParameter(
        name="agency",
        example_value="House"
    )
    session = ExampleParameter(
        name="session",
        example_value="0: normal session, 1: 1st special session, etc."
    )
    chapterNumber = ExampleParameter(
        name="chapterNumber",
        example_value="From GetSessionLawChapter and related calls: 'ChapterNumber' attribute."
    )
    rcwCite = ExampleParameter(
        name="rcwCite",
        example_value="From GetRcwCitesAffected and related calls: 'RcwCite' attribute."
    )
    committeeName = ExampleParameter(
        name="committeeName",
        example_value="From GetCommittees and related calls: 'Name' attribute."
    )
    documentClass = ExampleParameter(
        name="documentClass",
        example_value="From GetDocumentClasses and related calls: '#text' attribute."
    )
    namedLike = ExampleParameter(
        name="namedLike",
        example_value="From GetAllDocumentsByClass and related calls: 'Name' attribute."
    )
    beginDate = ExampleParameter(
        name="beginDate",
        example_value="2017-05-26"
    )
    sinceDate = ExampleParameter(
        name="sinceDate",
        example_value="2017-05-26"
    )
    endDate = ExampleParameter(
        name="endDate",
        example_value="2017-05-26"
    )
    changedSinceDate = ExampleParameter(
        name="changedSinceDate",
        example_value="2017-05-26"
    )
    requestNumber = ExampleParameter(
        name="requestNumber",
        example_value="From GetLegislation and related calls: 'Request' attribute."
    )
    agendaId = ExampleParameter(
        name="agendaId",
        example_value="From GetCommitteeMeetings and related calls: 'AgendaId' attribute."
    )
    billNumber = ExampleParameter(
        name="billNumber",
        example_value="From GetDocuments and related calls: 'BillId' attribute."
    )
    billId = ExampleParameter(
        name="billId",
        example_value="From GetDocuments and related calls: 'BillId' attribute."
    )
