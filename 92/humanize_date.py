from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)
format = "%m/%d/%y"


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
    using TIME_OFFSETS"""
    if not isinstance(date, datetime):
        raise ValueError()
    seconds_diff = (datetime.now() - date).total_seconds()
    if seconds_diff < 0:
        raise ValueError()
    for offset, phrase, divider in TIME_OFFSETS:
        if seconds_diff <= offset:
            seconds_passed = (
                int(seconds_diff) if divider is None else int(seconds_diff // divider)
            )
            return phrase.format(seconds_passed)
    else:
        return date.strftime(format)
