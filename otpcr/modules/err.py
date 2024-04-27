# This file is placed in the Public Domain.


"deferred exception handling"


from ..errors  import Errors, tostr


def err(event):
    "show errors."
    nmr = 0
    event.reply(f"status: {nmr} errors: {len(Errors.errors)}")
    for exc in Errors.errors:
        txt = tostr(exc)
        for line in txt.split():
            event.reply(line)
