#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import logging
from typing import List, Union

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class Meeting(object):
    """
    Create a Meeting object to interact and manage all of the primary queries
    for a Washington State Legislature meeting.

    :param agenda_id: WSL Web Services Database Id for the agenda.
    :param agency: Which agency the member belongs to. Ex: House, Senate, etc.
    :param committees: The committees present in the meeting.
    :param room: Which room the meeting is set to be or was held in.
    :param building: Which building the meeting is set to be or was held in.
    :param address: The address the meeting is set to be or was held in.
    :param city: The city the meeting is set to be or was held in.
    :param state: The state the meeting is set to be or was held in.
    :param zipcode: The zipcode the meeting is set to be or was held in.
    :param datetime: The datetime the meeting is set to be or was held at.
    :param cancelled: Is the meeting cancelled or not.
    :param revised_date: A revised datetime for the meeting.
    :param contact_info: Special information about how to contact members present at the meeting.
    :param meeting_type: What type of meeting is being held. Ex: Full Committee, Special Committee, etc.
    :param notes: Extra notes about the meeting.
    """

    def __init__(
        self,
        agenda_id: Union[int, str],
        agency: str,
        committees: List["Committee"],
        room: str,
        building: str,
        address: str,
        city: str,
        state: str,
        zipcode: Union[int, str],
        date: Union[datetime, str],
        cancelled: Union[bool, str],
        revised_date: Union[datetime, str],
        contact_info: str,
        meeting_type: str,
        notes: str
    ):
        # Make hidden
        self._agenda_id = agenda_id if isinstance(agenda_id, int) else int(agenda_id)
        self._agency = agency
        self._committees = committees
        self._room = room
        self._building = building
        self._address = address
        self._city = city
        self._state = state
        self._zipcode = zipcode if isinstance(zipcode, int) else int(zipcode)
        self._date = date if isinstance(date, datetime) else datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        if isinstance(cancelled, bool):
            self._cancelled = cancelled
        else:
            self._cancelled = cancelled not in ["false", "False", "FALSE"]
        self._revised_date = revised_date if isinstance(revised_date, datetime) else datetime.strptime(
            # We don't really need to care about the microsecond
            revised_date.split(".")[0],
            "%Y-%m-%dT%H:%M:%S"
        )
        self._contact_info = contact_info
        self._meeting_type = meeting_type
        self._notes = notes

    @property
    def agenda_id(self):
        return self._agenda_id

    @property
    def agency(self):
        return self._agency

    @property
    def committees(self):
        return self._committees

    @property
    def room(self):
        return self._room

    @property
    def building(self):
        return self._building

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def zipcode(self):
        return self._zipcode

    @property
    def date(self):
        return self._date

    @property
    def cancelled(self):
        return self._cancelled

    @property
    def revised_date(self):
        return self._revised_date

    @property
    def contact_info(self):
        return self._contact_info

    @property
    def meeting_type(self):
        return self._meeting_type

    @property
    def notes(self):
        return self._notes

    def __str__(self):
        return "<Meeting [{} {} {} {}]>".format(self.agenda_id, self.agency, self.meeting_type, self.date)

    def __repr__(self):
        return str(self)
