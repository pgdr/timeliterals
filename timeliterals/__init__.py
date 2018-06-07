class __literals:
    from datetime import timedelta as D
    @property
    def minutes(self):
        return self.D(minutes=1)
    @property
    def hours(self):
        return self.D(hours=1)
    @property
    def seconds(self):
        return self.D(seconds=1)
    @property
    def ms(self):
        return self.D(milliseconds=1)
    @property
    def us(self):
        return self.D(microseconds=1)

__l = __literals()
hours = __l.hours
minutes = __l.minutes
seconds = __l.seconds
ms = __l.ms
us = __l.us

__all__ = ['hours', 'minutes', 'seconds', 'ms', 'us']
__version__ = '0.0.1'
