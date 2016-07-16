#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

from pyshould import it
from pyshould import should  # NOQA

from cli_app import output


def describe_output():

    def should_intialise_with_given_text():
        value = "test message"
        a = output.Output(value)
        it(a.text).should.equal(value)
