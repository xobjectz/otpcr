#!/usr/bin/env python3
# This file is placed in the Public Domain
#
# pylint: disable=C0116


"build package"


import os


def popen(txt):
    for line in os.popen(txt).readlines():
        print(line.strip())


popen("python3 setup.py sdist")
print("")
popen("python3 -m pip wheel -e .")
popen("mv *.whl dist")
print("")
popen("twine check dist/*")