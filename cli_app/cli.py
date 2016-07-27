#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

from cli_app import log
from cli_app import options
from cli_app import output


LOG = log.Logger.get('main')


def main():
    # configargparse raises a SystemExit on error
    args = options.Options().parse()
    LOG.debug(args)
    out = output.Output(args.text)
    out.printScreen()


if __name__ == '__main__':
    sys.exit(main())
