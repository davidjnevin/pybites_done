from collections import Counter, defaultdict

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    most_prolific = defaultdict(list)
    for car_dict in data:
        most_prolific[car_dict["year"]].append(car_dict["automaker"])

    return max(set(most_prolific[year]), key=most_prolific[year].count)


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    models = set()
    models_dict = defaultdict(set)
    models = {
        line["model"]
        for line in data
        if line["automaker"] == automaker and line["year"] == year
    }

    return models


# most_prolific_automaker(1999)
get_models("Dodge", 1999)
