from enum import Enum


class loop_statuses(Enum):
    LOOP = 1
    STOP = 2


class loop_status:
    _status = loop_statuses.STOP

    @classmethod
    def get_status(cls):
        return cls._status

    @classmethod
    def set_status(cls, value):
        if isinstance(value, loop_statuses):
            cls._status = value
