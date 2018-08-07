#!/usr/bin/env python

from timeliterals import *

import unittest

class TestLiterals(unittest.TestCase):
    def test_literals(self):
        delta = 2 * hours - 14 * minutes + 10 * seconds \
                + 140 * milliseconds - 3 * microseconds
        self.assertEqual(delta.total_seconds(), 6370.139997)

    def test_shorts(self):
        from timeliterals import days as d, hours as h, minutes as m
        delta = 2*h - 14*m
        self.assertTrue(1*h+30*m < delta < 2 * hours)
        self.assertEqual(delta.total_seconds(), 6360)
        self.assertEqual(2*d, 48*h)

    def test_mod(self):
        import timeliterals as t
        delta = 3*t.hours + 18*t.minutes
        self.assertEqual(delta.total_seconds(), 11880)
    
    def test_function(self):
        from datetime import timedelta
        self.assertEqual(timedelta(hours=5), hours(5))
        self.assertTrue(isinstance(hours, timedelta))

if __name__ == '__main__':
    unittest.main()
