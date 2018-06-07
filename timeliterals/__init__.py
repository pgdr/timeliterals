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
    def milliseconds(self):
        return self.D(milliseconds=1)
    @property
    def microseconds(self):
        return self.D(microseconds=1)

__l = __literals()
hours = __l.hours
minutes = __l.minutes
seconds = __l.seconds
milliseconds = __l.milliseconds
microseconds = __l.microseconds

__all__ = ['hours', 'minutes', 'seconds', 'milliseconds', 'microseconds']
__version__ = '0.0.1'
