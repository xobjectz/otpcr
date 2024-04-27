# This file is placed in the Public Domain.


"scan modules for commands."


import inspect


from .commands  import scan
from .whitelist import whitelist
    

def init(pkg, modstr, disable=""):
    "init"
    mds = []
    for modname in spl(modstr):
        if skip(modname, disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        if "init" in dir(module):
            module.init()
            mds.append(module)
    return mds


def skip(name, skipped):
    "check for skipping"
    for skp in spl(skipped):
        if skp in name:
            return True
    return False


def scanner(pkg, modstr, disable=""):
    "scan modules for commands and classes"
    mds = []
    for modname in spl(modstr):
        if skip(modname, disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        scan(module)
        scancls(module)
    return mds
