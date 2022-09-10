import csv
import os
from collections import defaultdict, namedtuple
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open(MOVIE_DATA, newline="") as movies_data:
        reader = csv.DictReader(movies_data)
        movie_dict = defaultdict(list)
        for row in reader:
            try:
                director = row["director_name"]
                title = row["movie_title"]
                year = int(row["title_year"])
                score = float(row["imdb_score"])
            except ValueError:
                continue
            if year >= MIN_YEAR:
                if movie_dict[director]:
                    movie_dict[director].append(
                        Movie(title=title, year=year, score=score)
                    )
                else:
                    movie_dict[director] = [Movie(title=title, year=year, score=score)]

    return movie_dict


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    score = 0.0
    number_of_movies = len(movies)
    for movie in movies:
        score += movie.score
    return round(score / number_of_movies, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    average_score_list = []
    for director in directors:
        if len(directors[director]) >= MIN_MOVIES:
            mean_score = calc_mean_score(directors[director])
            average_score_list.append((director, mean_score))  ### MIN_MOVIES!!
    sorted_average_score_list = sorted(
        average_score_list, key=lambda x: x[1], reverse=True
    )
    return sorted_average_score_list


# print(calc_mean_score(get_movies_by_director()["Sergio Leone"]))
print(get_average_scores(get_movies_by_director()))
