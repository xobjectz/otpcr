# This file is placed in the Public Domain.
#
# pylint: disable=R0903


"table"


import importlib


from .object import Object


class Table:

    "Table"

    mods = Object()


def load(mname):
    "load module."
    setattr(Table.mods, mname, importlib.import_module(mname))


def ondemand(mname):
    "return module."
    mod = getattr(Table.mods, mname, None)
    if not mod:
        load(mname)
        mod = getattr(Table.mods, mname, None)
    return mod


def __dir__():
    return (
        'Table',
        'load',
        'ondemend'
    )
