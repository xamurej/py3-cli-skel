#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

from cli_app import log

LOG = log.Logger.get()


class Output(object):

    def __init__(self, text):
        LOG.info('create Output with "%s"', text)
        self.text = text

    def message(self):
        return self.text

    def printScreen(self):
        print(self.message())
