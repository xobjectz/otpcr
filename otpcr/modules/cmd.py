# This file is placed in the Public Domain.


"list of commands"


from ..cmds import Commands, add


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(list(Commands.cmds))))


add(cmd)
