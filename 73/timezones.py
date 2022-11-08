from datetime import datetime
import pytz

MIN_MEETING_HOUR = 6
MAX_MEETING_HOUR = 22
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
    Receive a utc datetime and one or more timezones and check if
    they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
    (both included).
    """
    utc = pytz.utc.localize(utc)
    result = False
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError
    for tz in timezones:
        tz = pytz.timezone(tz)
        hour = utc.astimezone(tz).hour
        if hour in range(MIN_MEETING_HOUR, MAX_MEETING_HOUR + 1):
            result = True
        else:
            result = False
            break

    return result

    # if MIN_MEETING_HOUR <= utc_time.
    #
    #


within_schedule(datetime.now(), "Europe/Madrid", "Australia/Sydney", "America/Chicago")
