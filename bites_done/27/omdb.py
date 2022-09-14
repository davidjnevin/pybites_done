import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    output = []
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
        output.append(data)

    return output


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominations = 0
    title = ""
    for movie in movies:
        no_of_nominations = int(movie["Awards"].split(" ")[-2])
        if no_of_nominations > nominations:
            title = movie["Title"]
            nominations = no_of_nominations
    return title


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtime = 0
    title = ""
    for movie in movies:
        movie_runtime = int(movie["Runtime"].split()[0])
        if movie_runtime > runtime:
            title = movie["Title"]
            runtime = movie_runtime

    return title
