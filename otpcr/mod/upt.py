# This file is placed in the Public Domain.


"uptime"


import time


from ..ifc import laps


STARTTIME = time.time()


def upt(event):
    "show uptime."
    event.reply(laps(time.time() - STARTTIME))
