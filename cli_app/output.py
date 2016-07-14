#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

from cli_app import logging

LOG = logging.Logger.get('output')


class Output(object):

    def __init__(self, text):
        LOG.debug('create Output with "{0}"', text)
        self.text = text

    def message(self):
        return self.text

    def printScreen(self):
        print(self.message())
