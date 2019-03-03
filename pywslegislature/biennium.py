#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import logging

###############################################################################

log = logging.getLogger(__name__)

###############################################################################

def pstnow():
    return datetime.utcnow() - timedelta(hours=8)


class Biennium(object):

    def __init__(self, year: int = None):
        """
        Create a Biennium object that handles specifically Washington State Legislature biennium details.

        :param year: An integer year to create a biennium from.
        """
        # Get year if None provided
        if year is None:
            # Washington timezone is UTC-8
            self._dt = pstnow()
            log.debug("Setting biennium object to current PST datetime: {}".format(self.dt))
        # Get datetime if passes
        else:
            self._dt = datetime.strptime(str(year), "%Y")
            log.debug("Setting biennium object to passed year as datetime: {}".format(self.dt))

        log.info("Biennium object created using dateime: {}".format(self.dt))

        # Process biennium
        year_is_odd = self.year % 2 == 1
        self._first_year = self.year if year_is_odd else self.year - 1
        self._second_year = self.year if not year_is_odd else self.year + 1

    @property
    def dt(self):
        return self._dt

    @property
    def year(self):
        return self._dt.year

    @property
    def first_year(self):
        return self._first_year

    @property
    def second_year(self):
        return self._second_year

    def __str__(self):
        return "{}-{}".format(self.first_year, str(self.second_year)[2:])

    def __repr__(self):
        return "<Biennium [{}]>".format(str(self))
