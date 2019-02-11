#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import logging

###############################################################################

log = logging.getLogger(__name__)

###############################################################################


class Biennium(object):

    def __init__(self, year: int = None):
        """
        Create a Biennium object that handles specifically Washington State Legislature biennium details.
        :param year: An integer year to create a biennium from.
        """
        if year is None:
            self._dt = datetime.utcnow() - timedelta(hours=8)
            log.debug("Setting biennium object to current PST datetime")
        else:
            self._dt = datetime.strptime(str(year), "%Y")
            log.debug("Setting biennium object to passed year as datetime")

        log.info("Biennium object created using dateime: {}".format(self.dt))

    @property
    def dt(self):
        return self._dt

    @property
    def year(self):
        return self._dt.year

    def __str__(self):
        if self.year % 2 == 1:
            return "{}-{}".format(self.year, str(self.year + 1)[2:])
        else:
            return "{}-{}".format(self.year - 1, str(self.year)[2:])

    def __repr__(self):
        return "<Biennium [{}]>".format(str(self))
