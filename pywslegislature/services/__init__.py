#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Services module for pywslegislature."""


# include all exampleParameters
from .exampleParameters import *  # noqa: F401, F403


# manually initialize every service
from .committeeService import CommitteeService
COMMITTEE_SERVICE = CommitteeService()
