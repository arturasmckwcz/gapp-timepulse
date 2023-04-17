from enum import Enum


class Statuses(Enum):
    LOOP = 1
    STOP = 2


loop = {'status': Statuses.STOP}


def get_loop_status():
    return loop['status']


def set_loop_status(value):
    if value in Statuses:
        loop['status'] = value
