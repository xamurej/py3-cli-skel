#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

from cli_app import logging
from cli_app import options


logging.Logger()
LOG = logging.Logger.get('main')


def main():
    # configargparse raises a SystemExit on error
    args = options.Options().parse()
    LOG.info(args)

if __name__ == '__main__':
    sys.exit(main())
