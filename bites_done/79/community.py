import csv
from collections import Counter
from csv import DictReader

import requests

CSV_URL = "https://bites-data.s3.us-east-2.amazonaws.com/community.csv"


def get_csv():
    """Use requests to download the csv and return the
    decoded content"""
    raw = requests.get(CSV_URL)
    decoded_csv = raw.content.decode("utf-8")
    data = csv.DictReader(decoded_csv.splitlines(), delimiter=",")
    return list(data)


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
    and their corresponding member counts in pluses to standard output
    """
    counter_of_tz = Counter(row["tz"] for row in content)

    for tz, count in sorted(counter_of_tz.items()):
        print(f"{tz:21} | {'+' * count}")


create_user_bar_chart(get_csv())
