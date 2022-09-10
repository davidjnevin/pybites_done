from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: int, expires: datetime) -> bool:
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return NOW > self.expires
