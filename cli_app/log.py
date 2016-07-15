#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

import logging
import datetime


class MyFormatter(logging.Formatter):

    converter = datetime.datetime.fromtimestamp

    def formatTime(self, record, date_fmt=None):
        ct = self.converter(record.created)
        t = ct.strftime("%Y-%m-%dT%H:%M:%S")
        s = "%s.%03dZ" % (t, record.msecs)
        return s


class Logger(object):
    FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
    LOGGERLIST = [
        'options',
        'main',
        'output',
    ]

    def __init__(self):
        self.handler = logging.StreamHandler()

        self.formatter = MyFormatter(fmt=self.FORMAT)

        self.handler.setFormatter(self.formatter)
        self.handler.setLevel(logging.DEBUG)

        for name in self.LOGGERLIST:
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            logger.addHandler(self.handler)

    def setLevel(self, level):
        self.handler.setLevel(level)

    @staticmethod
    def get(logger_name):
        return logging.getLogger(logger_name)
