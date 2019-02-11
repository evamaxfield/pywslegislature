#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from typing import Union

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class Committee(object):

    def __init__(
        self,
        id: Union[int, str],
        name: str,
        long_name: str,
        agency: str,
        acronym: str,
        phone: Union[int, str] = None
    ):
        """
        Enforce immutability and normalize committee details.
        """
        self._id = id if isinstance(id, int) else int(id)
        self._name = name
        self._long_name = long_name
        self._agency = agency
        self._acronym = acronym
        if phone:
            self._phone = phone if isinstance(phone, int) else int(
                phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
            )
        else:
            self._phone = None

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
    def phone(self):
        return self._phone

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "long_name": self.long_name,
            "agency": self.agency,
            "acronym": self.acronym,
            "phone": self.phone
        }

    def __str__(self):
        return "<Committee [{} {} {} {}]>".format(self.id, self.name, self.agency, self.acronym)

    def __repr__(self):
        return str(self)
