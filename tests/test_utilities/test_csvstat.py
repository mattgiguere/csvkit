#!/usr/bin/env python

import six

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from csvkit.utilities.csvstat import CSVStat

class TestCSVStat(unittest.TestCase):
    def test_runs(self):
        args = ['examples/test_utf8.csv']
        output_file = six.StringIO()

        utility = CSVStat(args, output_file)
        utility.main()

    def test_encoding(self):
        args = ['-e', 'latin1', 'examples/test_latin1.csv']
        output_file = six.StringIO()

        utility = CSVStat(args, output_file)
        utility.main()

