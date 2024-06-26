# This file is placed in the Public Domain.


"list of commands."


from ..run import Cfg


def ver(event):
    "list commands."
    if not Cfg.version:
        event.reply("version is not set.")
        return
    event.reply(f"{Cfg.name.upper()} {Cfg.version}")
