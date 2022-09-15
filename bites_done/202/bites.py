import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / "bites.csv"

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
    output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.
    """
    with open(stats, newline="", encoding="utf-8-sig") as s:
        reader = csv.DictReader(s, delimiter=";")
        rows = list(reader)

        output = []
        for row in rows:
            if row["Difficulty"] != "None":
                row["Bite"] = int(row["Bite"].split()[1][:-1])
                row["Difficulty"] = float(row["Difficulty"])
                output.append({"Bite": [row["Bite"], row["Difficulty"]]})

        output = sorted(output, key=lambda row: row["Bite"][1], reverse=True)
        return [x["Bite"][0] for x in output][:N]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
