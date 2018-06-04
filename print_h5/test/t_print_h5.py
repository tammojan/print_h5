#!/usr/bin/env python

"""
Test program for the print_h5 module
"""

import unittest
from print_h5 import print_h5

class Test_H5(unittest.TestCase):
    """Tests for print_h5"""

    def test_h5_zero_args(self):
        with self.assertRaises(TypeError):
            print_h5()

    def test_h5_nofile(self):
        with self.assertRaises(OSError):
            print_h5('NoNeXiStEnDfIlE.h5')


if __name__ == '__main__':
    unittest.main()
