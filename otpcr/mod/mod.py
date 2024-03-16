# This file is placed in the Public Domain.
#
# pylint: disable=C,R,E0402,W0105


"available modules"


from handler import Client


from . import __dir__


"commands"


def mod(event):
    res = []
    res.extend(__dir__())
    event.reply(",".join(sorted(res)))


Client.add(mod)
