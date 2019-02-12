#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict


class APIFunction(object):

    def __init__(self, name: str, parameters: Dict[str, str] = {}):
        self._name = name
        self._parameters = [{"name": name, "example": example} for name, example in parameters.items()]

    @property
    def name(self):
        return self._name

    @property
    def parameters(self):
        return self._parameters

    def __str__(self):
        return "<{}, parameters: {}>".format(self.name, self.parameters)

    def __repr__(self):
        return str(self)
