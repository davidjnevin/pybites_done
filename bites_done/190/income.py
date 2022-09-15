import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from urllib.request import urlretrieve

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/countries.xml", countries
    )

# https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-ElementTree
# https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    tree = ET.parse(xml)
    root = tree.getroot()
    ET.register_namespace("wb", "http://www.worldbank.org")
    ns = {"wb": "http://www.worldbank.org"}
    result = defaultdict(list)
    a = root.findall(".//wb:name", ns)
    b = root.findall(".//wb:incomeLevel", ns)
    for x, y in zip(b, a):
        result[x.text].append(y.text)

    return result


get_income_distribution(xml=countries)
