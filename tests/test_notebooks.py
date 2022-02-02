# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '02 Feb 2022'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'

import unittest

import notebook_runner

class TestOpensearchNotebook(unittest.TestCase):

    def test_runner(self):
        nb, errors = notebook_runner.run_notebook('../notebooks/cci_opensearch_demo.ipynb')
        self.assertEqual(errors, [])


if __name__ == '__main__':
    unittest.main()