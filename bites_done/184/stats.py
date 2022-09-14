import os
from collections import Counter
from csv import DictReader
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = "bite_output_log.txt"
DATA = os.path.join(TMP, LOGS)
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
if not os.path.isfile(DATA):
    urlretrieve(f"{S3}/{LOGS}", DATA)


class BiteStats:
    def __init__(self, data=DATA):
        self.rows = list(DictReader(open(data)))

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len({x["bite"] for x in self.rows})

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len({x["bite"] for x in self.rows if x["completed"] == "True"})

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len({x["user"] for x in self.rows})

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
        one or more Bites"""
        return len({x["user"] for x in self.rows if x["completed"] == "True"})

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
        (= in most rows)"""
        most_accessed = Counter(x["bite"] for x in self.rows).most_common()[0][0]
        return most_accessed

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        who_completed_most = Counter(
            x["user"] for x in self.rows if x["completed"] == "True"
        ).most_common()[0][0]
        return who_completed_most
