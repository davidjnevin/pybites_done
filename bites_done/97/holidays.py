import os
from collections import defaultdict
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

# prep data
tmp = os.getenv("TMP", "/tmp")
page = "us_holidays.html"
holidays_page = os.path.join(tmp, page)
urlretrieve(f"https://bites-data.s3.us-east-2.amazonaws.com/{page}", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
    holiday table (css class = list-table), and return a dict of
    keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, "html.parser")
    us_holiday_table_rows = soup.select("table.list-table tr")

    for row in us_holiday_table_rows:
        try:
            year, month, day = row.find("time").get("datetime").split("-")
            holiday_name = row.find("a").text.rstrip()
        except Exception:
            continue
        holidays[month].append(holiday_name)
    return holidays
