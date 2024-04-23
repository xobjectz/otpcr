# This file is placed in the Public Domain.
#
# pylint: disable=C0209,R0903


"log text"


import time


from ..client  import laps
from ..command import Command
from ..object  import Object
from ..find    import find, fntime
from ..workdir import  sync
from ..persist import whitelist


class Log(Object):

    "Log"

    def __init__(self):
        super().__init__()
        self.txt = ''


whitelist(Log)


def log(event):
    "log text."
    if not event.rest:
        nmr = 0
        for fnm, obj in find('log'):
            lap = laps(time.time() - fntime(fnm))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply('no log')
        return
    obj = Log()
    obj.txt = event.rest
    sync(obj)
    event.reply('ok')


Command.add(log)
