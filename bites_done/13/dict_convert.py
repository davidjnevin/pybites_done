import json
from collections import namedtuple
from datetime import datetime

blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

# define namedtuple here


def dict2nt(dict_):
    blog_named_tuple = namedtuple(
        "Blog",
        ["name", "founders", "started", "tags", "location", "site"],
    )
    return blog_named_tuple(**dict_)


def nt2json(nt):
    """https://pythontic.com/containers/namedtuple/_replace"""
    nt = nt._replace(started=nt.started.strftime("%Y %m %d"))
    return json.dumps(nt._asdict())


print(dict2nt(blog))
print(nt2json(dict2nt(blog)))
