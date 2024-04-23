# This file is placed in the Public Domain.
#
#


"list of commands"


from ..command import Command


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(list(Command.cmds))))


Command.add(cmd)
