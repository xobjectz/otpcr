# This file is placed in the Public Domain.
#
#


"utilities"


import datetime
import os


def hms():
    return now().split(".")[0]


def date():
    return str(datetime.datetime.now())


def now():
    return date().split()[-1]
