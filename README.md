# timeliterals [![Build Status](https://travis-ci.org/pgdr/timeliterals.svg?branch=master)](https://travis-ci.org/pgdr/timeliterals)


The `timeliterals` module is a simple module containing literals

* `hours`
* `minutes`
* `seconds`
* `milliseconds`
* `microseconds`
* `days`
* `weeks`

Can be used as a scalar or a function, for example `timedelta(seconds=5)` can be replaced by `seconds(5)` or `5 * seconds`.

```python
from timeliterals import *
duration = 2 * hours - 14 * minutes  # timedelta
duration += minutes(2)  # function
assert 1 * hours + 30 * minutes < duration < 2 * hours
assert duration / minutes == 108
assert duration / seconds == 6480
assert duration.total_seconds() == 6480
```

```python
from timeliterals import *
from datetime import timedelta
assert hours(2) == timedelta(hours=2)
```

```python
from timeliterals import hours as m, minutes as m, seconds as s, milliseconds as ms, microseconds as us
duration = 2*h - 14*m + 10*s + 140*ms - 3*us
assert duration < 2*h
```

## history
After a discussion on
the [python-ideas](https://mail.python.org/pipermail/python-ideas/) mailing list
on
[literals for datetime.timedelta](https://mail.python.org/pipermail/python-ideas/2018-June/051182.html),
[Chris Barker suggested](https://mail.python.org/pipermail/python-ideas/2018-June/051201.html) that

> [...] maybe you could propose adding:
>
> * `seconds`
> * `minutes`
> * `hours`
> * `days`
>
> to the datetime module, and then we could write:
>
> `60 * seconds == 1 * minutes`

This module is a proof-of-concept testing out that idea, but in its own module.
