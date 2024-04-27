# This file is placed in the Public Domain.


"list of commands"


def cmd(event):
    "list commands."
    from ..command import Command
    event.reply(",".join(sorted(list(Command.cmds))))
