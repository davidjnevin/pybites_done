import collections
from datetime import date, datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = "http://bites-data.s3.us-east-2.amazonaws.com/"
RSS_FEED = "pybites_feed.rss.xml"
PUB_DATE = re.compile(r"<pubDate>(.*?)</pubDate>")
TMP = os.getenv("TMP", "/tmp")


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
    a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
    'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    format_template: str = "Thu, 04 May 2017 20:46:00 +0200"
    format: str = "%a, %d %b %Y %H:%M:%S %z"
    return datetime.strptime(date_str, format).replace(tzinfo=None)


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
    that occurs most"""
    format: str = "%Y-%m"
    freq_table = {}
    for date in dates:

        formatted_date = datetime.strptime(
            str(date.year) + "-" + str(date.month), format
        )
        formatted_date = datetime.strftime(formatted_date, format)
        if formatted_date in freq_table:
            freq_table[formatted_date] += 1
        else:
            freq_table[formatted_date] = 1
    return max(freq_table, key=freq_table.get)
