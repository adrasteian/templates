#!/usr/bin/env python2

###############################################################################
# The MIT License (MIT)
#
# Copyright (c) 2021 F. Bar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################

from ...main.python import foo
from ...main.python import pretty_log as p_l

import sys
import unittest

class Printer:

    def out(self,msg):
        pass

class TestArgs(unittest.TestCase):

    def setUp(self):
        p_l.set_printer(Printer())

    def test_option_no_debug(self):

        # no -d/--debug option
        foo.set_argv(['foo.py','-t','.'])
        foo.main()

        # ...should not be any debug logs
        self.assertTrue(0==p_l.get_num_debug())

    def test_option_d_enabled(self):

        # specify -d option
        foo.set_argv(['foo.py','-d','-t','.'])
        foo.main()

        # ...should be at least one debug log
        self.assertTrue(0<p_l.get_num_debug())

    def test_option_debug_enabled(self):

        # specify -d option
        foo.set_argv(['foo.py','--debug','-t','.'])
        foo.main()

        # ...should be at least one debug log
        self.assertTrue(0<p_l.get_num_debug())

    def test_option_v_enabled(self):

        # specify -d option
        foo.set_argv(['foo.py','-v','-t','.'])
        foo.main()

        # ...should be no debug logs
        self.assertTrue(0==p_l.get_num_debug())
        # ...and at least 1 other log
        total_logs = p_l.get_num_error() + p_l.get_num_info() + p_l.get_num_success() + p_l.get_num_warning()

        self.assertTrue(0<total_logs)

# python -m src.test.python.test_args

if __name__ == "__main__":
    unittest.main()
