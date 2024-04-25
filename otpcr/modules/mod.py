# This file is placed in the Public Domain.


"available modules"


from ..command import Command


from . import __dir__


def mod(event):
    "show available modules."
    event.reply(",".join(sorted(__dir__())))


Command.add(mod)
