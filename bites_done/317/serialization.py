import os
import pickle
from datetime import date
from pathlib import Path
from typing import NamedTuple, Sequence
from urllib.request import urlretrieve

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
PICKLE_INFILE = TMP / "input.pkl"
PICKLE_OUTFILE = TMP / "output.pkl"


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


def download_pickle_file():
    """download a pickle file we created with a
    list of namedtuples
    """
    urlretrieve(f"{S3}/bite317.pkl", PICKLE_INFILE)


def deserialize(pkl_file: Path = PICKLE_INFILE) -> Sequence[NamedTuple]:
    """Load the list of namedtuples from the pickle file passed in"""
    with open(pkl_file, "rb") as f:
        return pickle.load(f)


def serialize(
    pkl_file: Path = PICKLE_OUTFILE, data: Sequence[NamedTuple] = None
) -> None:
    """Save the data passed in to the pickle file passed in"""
    if data is None:
        data = deserialize()

    with open(pkl_file, "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


# https://riptutorial.com/python/example/8651/using-pickle-to-serialize-and-deserialize-an-object
