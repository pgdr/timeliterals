#!/usr/bin/env python

from timeliterals import *

import unittest

class TestLiterals(unittest.TestCase):
    def test_literals(self):
        delta = 2 * hours - 14 * minutes + 10 * seconds + 140 * ms - 3 * us
        self.assertEqual(delta.total_seconds(), 6370.139997)

    def test_shorts(self):
        from timeliterals import hours as h, minutes as m
        delta = 2*h - 14*m
        self.assertTrue(1*h+30*m < delta < 2 * hours)
        self.assertEqual(delta.total_seconds(), 6360)

    def test_mod(self):
        import timeliterals as t
        delta = 3*t.hours + 18*t.minutes
        self.assertEqual(delta.total_seconds(), 11880)

if __name__ == '__main__':
    unittest.main()
