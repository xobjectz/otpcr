# This file is placed in the Public Domain.
#
# pylint: disable=C,R
# ruff: noqa: F401


"modules"


import os
import sys


PKGDIR = os.path.dirname(os.path.dirname(__file__))
LIBDIR = os.path.join(PKGDIR, "lib")
MODDIR = os.path.join(PKGDIR, "mod")

print(LIBDIR)


sys.path.insert(0, LIBDIR)


from otpcr.mod import cmd, err, flt, fnd, irc, log, mod, req, rss, rst
from otpcr.mod import tdo, thr, tmr, udp


def __dir__():
    return (
        'cmd',
        'err',
        'flt',
        'fnd',
        'irc',
        'log',
        'mod',
        'req',
        'rss',
        'tdo',
        'thr',
        'tmr'
    )


__all__ = __dir__()
