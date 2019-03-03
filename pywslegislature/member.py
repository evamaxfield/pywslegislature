#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from typing import Union

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class Member(object):
    """
    Create a Member object to interact and manage all of the primary queries
    for a Washington State Legislature member.

    :param id: WSL Web Services Database Id for the member.
    :param name: The short name for the member.
    :param long_name: The long name for the member.
    :param agency: Which agency the member belongs to. Ex: House, Senate, etc.
    :param acronym: The member acronoym.
    :param party: The party the member belongs to. Ex: Democrat, Republican, etc.
    :param district: The district the member represents.
    :param phone: The string or integer representation of the member's phone number.
    :param email: The member's email.
    :param first_name: The member's first name.
    :param last_name: The member's last name.
    """

    def __init__(
        self,
        id: Union[int, str],
        long_name: str,
        agency: str,
        acronym: str,
        district: Union[int, str],
        party: str = None,
        phone: Union[int, str] = None,
        email: str = None,
        name: str = None,
        first_name: str = None,
        last_name: str = None
    ):
        # Enforce either name or first-last pairing provided
        if name is None and (first_name is None and last_name is None):
            raise AttributeError("'name', or 'first_name' and 'last_name' are required to initialize a Member object.")

        # Expand depending on parameters
        if name is None and (first_name and last_name):
            name = f"{first_name} {last_name}"
        else:
            first_name = name.split()[0]
            last_name = name.split()[1]

        # Make hidden
        self._id = id if isinstance(id, int) else int(id)
        self._name = name
        self._long_name = long_name
        self._agency = agency
        self._acronym = acronym
        self._district = district if isinstance(district, int) else int(district)
        self._party = party
        if phone:
            self._phone = phone if isinstance(phone, int) else int(
                phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
            )
        else:
            self._phone = None
        self._email = email
        self._first_name = first_name
        self._last_name = last_name

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
    def acronym(self):
        return self._acronym

    @property
    def district(self):
        return self._district

    @property
    def party(self):
        return self._party

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    def __str__(self):
        return "<Member [{} {} {} {}]>".format(self.id, self.name, self.agency, self.party)

    def __repr__(self):
        return str(self)
