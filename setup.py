import os


class rabbitmq_setup:
    host = os.environ.get("RABBITMQ_HOST") or "rabbitmq"
    day = os.environ.get("TIMEPULSE_DAY_IN_SECS") or 10
    exchange = "timepulse"
    user = "gapp"
    password = "gapp"
