# This file is placed in the Public Domain.


"list of commands"


from ..ifc import Commands


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(list(Commands.cmds))))
