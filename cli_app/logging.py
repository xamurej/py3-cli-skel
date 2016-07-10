#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

from logbook import Logger as logbookLogger
from logbook import StreamHandler

import sys


class Logger(object):

    def __init__(self):
        StreamHandler(sys.stdout).push_application()

    @staticmethod
    def get(logger_name):
        return logbookLogger(logger_name)
