# This file is placed in the Public Domain.
#
# pylint: disable=R0903


"command"


from .object import Object


class Command:

    "Command"

    cmds = Object()

    @staticmethod
    def add(func):
        "add command."
        setattr(Command.cmds, func.__name__, func)
