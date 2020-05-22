#!/usr/bin/python3
"""
take max int
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestMaxInteger class"""

    def list_vide_test(self):
        self.assertEqual(max_integer([]), None)

    def max_milieu_test(self):
        self.assertEqual(max_integer([1, 16, 2]), 16)

    def max_fin_test(self):
        self.assertEqual(max_integer([0, 2, 1, 14]), 14)

    def max_seul_ele_test(self):
        self.assertEqual(max_integer([12]), 12)

    def neg_int_test(self):
        self.assertEqual(max_integer([-14, -7, -2]), -2)

    def float_only_test(self):
        self.assertEqual(max_integer([4.5, 8.7, -9.8, 7.1, -0.3]), 8.7)

    def string_test(self):
        self.assertEqual(max_integer(["na", "naa", "naanoua"]), "naanoua")

    def vide2_test(self):
        max_list = ["hi", "hello", "hello"]
        self.assertEqual(max_integer(), None)

    def string_mot_test(self):
        max_list = ["hamazbib"]
        self.assertEqual(max_integer(["zbib"]), "z")

if __name__ == "__main__":
    unittest.main()
