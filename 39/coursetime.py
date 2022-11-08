from datetime import timedelta
import os
import re
from typing import List
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(os.getenv("TMP", "/tmp"), "course_timings")
urllib.request.urlretrieve(
    "http://bites-data.s3.us-east-2.amazonaws.com/course_timings", COURSE_TIMES
)
with open(COURSE_TIMES) as f:
    COURSE_TIMES = f.readlines()


def get_all_timestamps() -> List[str]:
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
    Here is a snippet of the input file:

    Start  What is Practical JavaScript? (3:47)
    Start  The voice in your ear (4:41)
    Start  Is this course right for you? (1:21)
    ...

     Return a list of MM:SS timestamps
    """
    timestamp_list = []

    for line in COURSE_TIMES:
        if "(" in line:
            timestamp_str = line.split("(")[-1]
            timestamp_list.append((timestamp_str[: len(timestamp_str) - 2]))
    return timestamp_list


def calc_total_course_duration(timestamps) -> str:
    """Takes timestamps list as returned by get_all_timestamps
    and calculates the total duration as HH:MM:SS"""
    format: str = "%M:%S"
    total_duration = timedelta(minutes=0, seconds=0)
    for time in timestamps:

        time_stamp: timedelta = timedelta(
            minutes=int(time.split(":")[0]), seconds=int(time.split(":")[1])
        )
        total_duration += time_stamp
    return str(total_duration)
