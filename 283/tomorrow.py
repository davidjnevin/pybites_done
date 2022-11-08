import datetime


def tomorrow(today=None):
    if type(today) is datetime.date:
        return today + datetime.timedelta(days=1)
    today = datetime.date(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
    )
    return today + datetime.timedelta(days=1)
