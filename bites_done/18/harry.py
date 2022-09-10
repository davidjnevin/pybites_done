import os
import string
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)

STOPWORDS = set()


def get_harry_most_common_word():
    HARRYWORDS = []
    with open(stopwords_file, "r") as stopwords:
        lines = stopwords.read()
        for line in lines.split():
            STOPWORDS.add(line.strip().lower())

    with open(harry_text, "r") as harry:
        lines = harry.read().lower()
        lines = lines.translate(str.maketrans("", "", string.punctuation))
        for line in lines.split():
            if line.isalnum() and not any(stop == line for stop in STOPWORDS):
                HARRYWORDS.append(line)

    HWORDS = Counter(HARRYWORDS)
    return HWORDS.most_common(1)[0]


print(get_harry_most_common_word())
