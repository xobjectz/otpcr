# This file is placed in the Public Domain.
#
# pylint: disable=R0903


"commands"


from .object import Object, construct, values
from .parse  import parse
from .table  import ondemand


MODNAMES = {
    "cmd": "otpcr.modules.cmd",
    "err": "otpcr.modules.err",
    "fnd": "otpcr.modules.fnd",
    "cfg": "otpcr.modules.irc",
    "mre": "otpcr.modules.irc",
    "pwd": "otpcr.modules.irc",
    "dpl": "otpcr.modules.rss",
    "nme": "otpcr.modules.rss",
    "rem": "otpcr.modules.rss",
    "res": "otpcr.modules.rss",
    "rss": "otpcr.modules.rss",
    "syn": "otpcr.modules.rss",
    "exp": "otpcr.modules.rss",
    "imp": "otpcr.modules.rss",
    "thr": "otpcr.modules.thr",
    "tmr": "otpcr.modules.tmr",
    "upt": "otpcr.modules.upt"
}


class Commands:

    "Commands"

    cmds     = Object()
    modnames = Object()
    construct(modnames, MODNAMES)


def add(func):
    "add command."
    setattr(Commands.cmds, func.__name__, func)
    if func.__module__ != "__main__":
        setattr(Commands.modnames, func.__name__, func.__module__)


def command(bot, evt):
    "check for and run a command."
    parse(evt)
    func = getattr(Commands.cmds, evt.cmd, None)
    if not func:
        mname = getattr(Commands.modnames, evt.cmd, None)
        if mname:
            mod = ondemand(mname)
            getattr(mod, evt.cmd, None)
        func = getattr(Commands.cmds, evt.cmd, None)
    if func:
        func(evt)
    bot.show(evt)
    evt.ready()


def modnames():
    "return list of modules."
    return sorted({x.split(".")[-1].lower() for x in values(Commands.modnames)})


def __dir__():
    return (
        'Commands',
        'add',
        'command',
        'modnames'
    )
