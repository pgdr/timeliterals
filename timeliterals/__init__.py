"""
>>> from timeliterals import hours
>>> hours(5)
datetime.timedelta(0, 18000)
>>> 5 * hours + 2 * seconds
datetime.timedelta(0, 18002)
"""

__all__ = ('seconds', 'milliseconds', 'microseconds', 'weeks', 'days', 'hours', 'minutes')
__version__ = '0.0.4'

from datetime import timedelta

class CallableTimedelta(timedelta):
    def __call__(self, x):
        return self * x
    
seconds, milliseconds, microseconds, weeks, days, hours, minutes = (
    CallableTimedelta(**{x:1})
    for x in __all__)
