# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402


"todo list"


import time


from objects import Object
from handler import Client
from persist import Persist, fntime, find, laps, sync


class NoDate(Exception):

    pass


class Todo(Object):

    def __init__(self):
        Object.__init__(self)
        self.txt = ''


Persist.add(Todo)


def dne(event):
    if not event.args:
        event.reply("dne <txt>")
        return
    selector = {'txt': event.args[0]}
    nmr = 0
    for fnm, obj in find('todo', selector):
        nmr += 1
        obj.__deleted__ = True
        sync(obj, fnm)
        event.reply('ok')
        break
    if not nmr:
        event.reply("nothing todo")


Client.add(dne)


def tdo(event):
    if not event.rest:
        nmr = 0
        for fnm, obj in find('todo'):
            lap = laps(time.time()-fntime(fnm))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply("no todo")
        return
    obj = Todo()
    obj.txt = event.rest
    sync(obj)
    event.reply('ok')


Client.add(tdo)
