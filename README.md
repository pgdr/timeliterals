# timeliterals [![Build Status](https://travis-ci.org/pgdr/timeliterals.svg?branch=master)](https://travis-ci.org/pgdr/timeliterals)


The `timeliterals` module is a simple module containing literals

* `hours`
* `minutes`
* `seconds`
* `milliseconds`
* `microseconds`

Can be used as

```python
from timeliterals import *
delta = 2 * hours - 14 * minutes + 10 * seconds
delta += 140 * milliseconds - 3 * microseconds
assert delta < 2 * hours
```

```python
from timeliterals import hours as h, minutes as m
delta = 2*h - 14*m
assert 1*h+30*m < delta < 2 * hours
assert delta.total_seconds() == 6360
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
