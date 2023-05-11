import os
from datetime import datetime, timedelta


class date:
    _current_date = datetime.strptime(
        os.environ.get('GAPP_FIRST_DAY') or "1970-01-01",
        "%Y-%m-%d") - timedelta(days=1)

    @classmethod
    def current_date(cls):
        return cls._current_date.strftime("%Y-%m-%d")

    @classmethod
    def next_date(cls):
        cls._current_date += timedelta(days=1)
        return cls._current_date.strftime("%Y-%m-%d")
