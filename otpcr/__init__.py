# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"OTP-CR-117/19"


import os
import sys


PKGDIR = os.path.dirname(__file__)
LIBDIR = os.path.join(PKGDIR, "lib")
MODDIR = os.path.join(PKGDIR, "mod")


sys.path.insert(0, LIBDIR)


from otpcr import lib
from otpcr import mod