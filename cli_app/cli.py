#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

from cli_app import logging
from cli_app import options


logging.Logger()
LOG = logging.Logger.get('main')


def main():

    try:
        args = options.Options().parse()
        print(args)
    except options.Usage as err:
        print(err.msg, file=sys.stderr)
        print("for help use --help", file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
