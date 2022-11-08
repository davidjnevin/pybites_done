from datetime import date, datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "http://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line: str) -> datetime:
    """TODO 1:
    Extract timestamp from logline and convert it to a datetime object.
    For example calling the function with:
    INFO 2014-07-03T23:27:51 supybot Shutdown complete.
    returns:
    datetime(2014, 7, 3, 23, 27, 51)
    """
    format: str = "%Y-%m-%dT%H:%M:%S"
    date_time_element: str = line.split(" ")[1]
    return datetime.strptime(date_time_element, format)


def time_between_shutdowns(loglines) -> timedelta:
    """TODO 2:
    Extract shutdown events ("Shutdown initiated") from loglines and
    calculate the timedelta between the first and last one.
    Return this datetime.timedelta object.
    """
    shutdown_initialed: list[datetime] = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            shutdown_initialed.append(convert_to_datetime(line))
    return shutdown_initialed[-1] - shutdown_initialed[0]


# print(convert_to_datetime("INFO 2014-07-03T23:27:51 supybot Shutdown complete."))
