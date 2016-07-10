#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

import configargparse

from cli_app import logging

LOG = logging.Logger.get('options')

class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg


class Options(object):

    def __init__(self):
        self.parser = configargparse.ArgParser(
            default_config_files=['/etc/settings.ini', '~/.my_settings'])

        self.parser.add('-c', '--my-config',
                        required=True,
                        is_config_file=True,
                        help='config file path')

        # this option can be set in a config file because it starts with '--'
        self.parser.add('--genome',
                        required=True,
                        help='path to genome file')

        self.parser.add('-v',
                        help='verbose',
                        action='store_true')

        # this option can be set in a config file because it starts with '--'
        self.parser.add('-d', '--dbsnp',
                        help='known variants .vcf',
                        env_var='DBSNP_PATH')

        self.parser.add('vcf', nargs='+', help='variant file(s)')

    def parse(self):
        try:
            return self.parser.parse_args()
        except Exception as msg:
            raise Usage(msg)
