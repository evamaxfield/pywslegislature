#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Top-level package for pywslegislature."""

__author__ = 'Jackson Maxfield Brown'
__email__ = 'jmaxfieldbrown@gmail.com'
__version__ = '0.1.0'


def get_module_version():
    return __version__


from .biennium import Biennium  # noqa: F401
from .legislature import Legislature  # noqa: F401
from .query import WSLRequest  # noqa: F401
