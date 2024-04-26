# This file is placed in the Public Domain.


"command"


from .object import Object


class Command: # pylint: disable=R0903

    "Command"

    cmds = Object()

    @staticmethod
    def add(func):
        "add command."
        setattr(Command.cmds, func.__name__, func)


def __dir__():
    return (
        'Command',
    )
