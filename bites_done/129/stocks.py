from collections import Counter

import requests

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
    - strip off leading '$',
    - if 'M' in cap value, strip it off and return value as float,
    - if 'B', strip it off, multiply by 1,000 and return
      value as float"""
    if cap == "n/a":
        return 0
    else:
        cap_dollar = cap[1:]
        if "M" in cap_dollar:
            output = float(cap_dollar.replace("M", ""))
        if "B" in cap_dollar:
            output = float(cap_dollar.replace("B", "")) * 1000
    return output


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision"""
    return round(
        sum(
            _cap_str_to_mln_float(stock["cap"])
            for stock in data
            if stock["industry"] == industry
        ),
        2,
    )


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
    the _cap_str_to_mln_float to parse the cap values"""
    stock_symbol = ""
    highest_cap = 0.00
    for stock in data:
        curr_stock = stock["symbol"]
        curr_cap = _cap_str_to_mln_float(stock["cap"])
        if curr_cap > highest_cap:
            stock_symbol = curr_stock
            highest_cap = curr_cap

    return stock_symbol


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
    discard n/a"""
    sectors = [stock["sector"] for stock in data if stock["sector"] != "n/a"]

    return (Counter(sectors).most_common()[0][0], Counter(sectors).most_common()[-1][0])
