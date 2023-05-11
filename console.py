import os

environment = os.environ.get('ENV')


def log_debug(*args):
    if environment == "develop" or environment == "debug":
        print("DEBUG:", *args)


def log(*args):
    print("LOG:", *args)
