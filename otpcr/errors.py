# This file is placed in the Public Domain.
#
# pylint: disable=R0903


"errors"


import io
import traceback


class Errors:

    "Errors"

    errors = []
    filter = []    

    @staticmethod
    def out(txt):
        "overload this."


def debug(txt):
    "print to console."
    for skp in Errors.filter:
        if skp in txt:
            return
    Errors.out(txt)


def enable(func):
    "set output function."
    Errors.out = func


def later(exc):
    "add an exception"
    excp = exc.with_traceback(exc.__traceback__)
    Errors.errors.append(excp)


def tostr(exc):
    "format an exception"
    res = ""
    stream = io.StringIO(
                         traceback.print_exception(
                                                   type(exc),
                                                   exc,
                                                   exc.__traceback__
                                                  )
                        )
    for line in stream.readlines():
        res += line + "\n"
    return res


def out(exc):
    "check if output function is set."
    txt = str(tostr(exc))
    Errors.out(txt)


def errors():
    "show exceptions"
    for exc in Errors.errors:
        out(exc)
