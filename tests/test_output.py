#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Module docstring.

This serves as a long usage message.
"""

from cli_app import output

from spec import Spec
from pyshould import it, should


class TestOutput(Spec):
    """class output.Output"""

    def test_should_intialise_with_given_text(self):
        value = "test message"
        a = output.Output(value)
        it(a.text).should.equal(value)
