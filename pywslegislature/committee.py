#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import logging
import json
from typing import Union

from .biennium import Biennium, pstnow
from .services import CommitteeService, CommitteeMeetingService
from .meeting import Meeting
from .member import Member
from .query import WSLRequest

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class Committee(object):
    """
    Create a Committee object to interact and manage all of the primary queries
    for a Washington State Legislature committee.

    :param id: WSL Web Services Database Id for the committee.
    :param name: The short name for the committee.
    :param long_name: The long name for the committee.
    :param agency: Which agency the committee belongs to. Ex: House, Senate, etc.
    :param biennium: The biennium for the committee.
    :param acronym: The committe acronoym.
    :param phone: The string or integer representation of the committee phone number.
    """

    def __init__(
        self,
        id: Union[int, str],
        name: str,
        long_name: str,
        agency: str,
        biennium: Biennium,
        acronym: str,
        phone: Union[int, str] = None
    ):
        # Make hidden
        self._id = id if isinstance(id, int) else int(id)
        self._name = name
        self._long_name = long_name
        self._agency = agency
        self._biennium = biennium
        self._acronym = acronym
        if phone:
            self._phone = phone if isinstance(phone, int) else int(
                phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
            )
        else:
            self._phone = None

        # Lazy load
        self._meetings = None
        self._members = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def long_name(self):
        return self._long_name

    @property
    def agency(self):
        return self._agency

    @property
    def biennium(self):
        return self._biennium

    @property
    def acronym(self):
        return self._acronym

    @property
    def phone(self):
        return self._phone

    @property
    def meetings(self):
        if self._meetings is None:
            # Construct request
            # Use January 1st of earliest biennium year and the current date for begin and end
            today = pstnow()
            request = WSLRequest(
                CommitteeMeetingService.header,
                CommitteeMeetingService.GetCommitteeMeetings.name,
                {
                    "beginDate": f"{self.biennium.first_year}-01-01",
                    "endDate": f"{today.year}-{today.month}-{today.day}"
                }
            )

            # Get results from request
            results = request.process().json["ArrayOfCommitteeMeeting"]["CommitteeMeeting"]

            # Convert to meeting objects
            self._meetings = []
            for m in results:
                # Construct Committee objects
                committees = [
                    Committee(
                        id=m["Committees"][c]["Id"],
                        name=m["Committees"][c]["Name"],
                        long_name=m["Committees"][c]["LongName"],
                        agency=m["Committees"][c]["Agency"],
                        biennium=self.biennium,
                        acronym=m["Committees"][c]["Acronym"],
                        phone=m["Committees"][c]["Phone"]
                    ) for c in m["Committees"]
                ]

                # If any committee found in the meeting details retrieved
                # create add a Meeting object to the list of meetings
                if any(c.id==self.id for c in committees):
                    self._meetings.append(
                        Meeting(
                            agenda_id=m["AgendaId"],
                            agency=m["Agency"],
                            committees=committees,
                            room=m["Room"],
                            building=m["Building"],
                            address=m["Address"],
                            city=m["City"],
                            state=m["State"],
                            zipcode=m["ZipCode"],
                            date=m["Date"],
                            cancelled=m["Cancelled"],
                            revised_date=m["RevisedDate"],
                            contact_info=m["ContactInformation"],
                            meeting_type=m["CommitteeType"],
                            notes=m["Notes"]
                        )
                    )

        return self._meetings

    @property
    def members(self):
        if self._members is None:
            # Construct request
            request = WSLRequest(
                CommitteeService.header,
                CommitteeService.GetCommitteeMembers.name,
                {
                    "agency": self.agency,
                    "biennium": str(self.biennium),
                    "committeeName": self.name
                }
            )

            # Get results from request
            results = request.process().json["ArrayOfMember"]["Member"]

            # Convert to member objects
            self._members = [
                Member(
                    id=m["Id"],
                    name=m["Name"],
                    long_name=m["LongName"],
                    agency=m["Agency"],
                    acronym=m["Acronym"],
                    party=m["Party"],
                    district=m["District"],
                    phone=m["Phone"],
                    email=m["Email"],
                    first_name=m["FirstName"],
                    last_name=m["LastName"]
                ) for m in results
            ]
            log.info("Reduced returned results, {}, by selecting {}:{}".format(results, "ArrayOfMember", "Member"))

        return self._members

    def __str__(self):
        return "<Committee [{} {} {} {}]>".format(self.id, self.name, self.agency, self.acronym)

    def __repr__(self):
        return str(self)
